package com.example.ui
import android.content.Context

import android.app.Application
import android.util.Log
import androidx.compose.runtime.mutableStateOf
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.example.data.OranRideRepository
import com.example.data.RideEntity
import com.example.data.UserEntity
import com.example.data.PlaceResult

import com.example.data.RetrofitClient
import com.example.data.oranPlaces
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

class OranRideViewModel(application: Application) : AndroidViewModel(application) {

    private val repository = OranRideRepository(application)
    private val TAG = "OranRideViewModel"

    // Current screen navigation: "mode_select", "register", "rider_home", "rider_tracking", "driver_home", "driver_nav", "history"
    private val _currentScreen = MutableStateFlow("mode_select")
    val currentScreen: StateFlow<String> = _currentScreen.asStateFlow()

    // Active User profiles
    val currentUser: StateFlow<UserEntity?> = repository.currentUser
    val activeRide: StateFlow<RideEntity?> = repository.activeRide
    val activeRequests: StateFlow<List<RideEntity>> = repository.getActiveRequests()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())

    // Selected Landmarks for Booking
    val pickupLandmark = mutableStateOf<OranLandmark?>(oranLandmarks[1]) // Default: Front de Mer
    val destinationLandmark = mutableStateOf<OranLandmark?>(oranLandmarks[0]) // Default: Fort Santa Cruz

    // Category Select
    val selectedCategory = mutableStateOf("Standard") // Standard, Luxe, Comfort, Moto
    val categoryFares = mapOf(
        "Standard" to 1.0, // Multiplier
        "Luxe" to 1.8,
        "Comfort" to 1.4,
        "Moto" to 0.7
    )


    // Start real GPS tracking
    fun startRiderLocation() {
        val helper = LocationHelper(getApplication())
        helper.start { lat, lon ->
            _riderLocation.value = Pair(
                lat.toFloat(),
                lon.toFloat()
            )
        }
    }

    // Live driver coordinates (Grid coordinates 0 to 100)
    private val _driverLocation = MutableStateFlow<Pair<Float, Float>?>(null)
    val driverLocation: StateFlow<Pair<Float, Float>?> = _driverLocation.asStateFlow()

    // Live Rider coordinates during driver tracking
    private val _riderLocation = MutableStateFlow<Pair<Float, Float>?>(null)
    val riderLocation: StateFlow<Pair<Float, Float>?> = _riderLocation.asStateFlow()

    private val _etaSeconds = MutableStateFlow(0)
    val etaSeconds: StateFlow<Int> = _etaSeconds.asStateFlow()

    // Ride history list
    private val _rideHistory = MutableStateFlow<List<RideEntity>>(emptyList())
    val rideHistory: StateFlow<List<RideEntity>> = _rideHistory.asStateFlow()

    // Is Firebase actually initialized and connected
    val isFirebaseReady = repository.isFirebaseEnabled

    // Simulation job handler
    private var simulationJob: Job? = null

    private var locationHelper: LocationHelper? = null

    // Incoming simulated request for Driver mode
    private val _incomingDriverRequest = MutableStateFlow<RideEntity?>(null)
    val incomingDriverRequest: StateFlow<RideEntity?> = _incomingDriverRequest.asStateFlow()

    init {
        viewModelScope.launch {
            // Observe current user changes to query history and setup
            currentUser.collect { user ->
                if (user != null) {
                    repository.insertMockDrivers() // Pre-populate mock drivers
                    loadHistory()
                    
                    // Route to correct home based on role
                    if (_currentScreen.value == "mode_select" || _currentScreen.value == "register") {
                        _currentScreen.value = if (user.role == "driver") "driver_home" else "rider_home"
                    }
                }
            }
        }
        
        // Listen to active ride updates
        viewModelScope.launch {
            activeRide.collect { ride ->
                if (ride != null) {
                    // Update live locations when tracking
                    if (ride.status == "searching") {
                        _driverLocation.value = null
                    }
                }
            }
        }
    }

    fun loadHistory() {
        viewModelScope.launch {
            repository.getRideHistory().collect { history ->
                _rideHistory.value = history
            }
        }
    }

    fun setScreen(screenName: String) {
        _currentScreen.value = screenName
    }

    // Register profile
    fun register(name: String, phone: String, role: String, vehicleInfo: String?) {
        viewModelScope.launch {
            repository.registerUser(name, phone, role, vehicleInfo)
        }
    }

    // Select standard profile for quick start
    fun selectProfile(user: UserEntity) {
        viewModelScope.launch {
            repository.selectUserProfile(user)
        }
    }

    // Toggle Driver state
    fun setDriverOnline(isOnline: Boolean) {
        viewModelScope.launch {
            repository.toggleDriverOnline(isOnline)
            
            if (isOnline) {
                // Periodically trigger a simulated rider request to give driver user something to accept!
                simulateRiderRequestForDriver()
            } else {
                _incomingDriverRequest.value = null
            }
        }
    }

    // Logout
    fun logout() {
        viewModelScope.launch {
            repository.logout()
            _currentScreen.value = "mode_select"
        }
    }

    // Calculate Fare Estimate
    fun getEstimatedFare(): Double {
        val p = pickupLandmark.value ?: return 0.0
        val d = destinationLandmark.value ?: return 0.0
        val distance = getDistanceKm(p.gridX, p.gridY, d.gridX, d.gridY)
        val multiplier = categoryFares[selectedCategory.value] ?: 1.0
        // Base fare: 150 DZD + 80 DZD per KM
        val base = 150.0 + (distance * 80.0)
        return (base * multiplier)
    }

    fun getEstimatedDistance(): Float {
        val p = pickupLandmark.value ?: return 0.0f
        val d = destinationLandmark.value ?: return 0.0f
        return getDistanceKm(p.gridX, p.gridY, d.gridX, d.gridY)
    }

    private fun getDistanceKm(x1: Float, y1: Float, x2: Float, y2: Float): Float {
        val dx = x2 - x1
        val dy = y2 - y1
        // Map grid coordinates to roughly Oran's physical width (approx 12km)
        return (Math.hypot(dx.toDouble(), dy.toDouble()).toFloat() * 0.15f)
    }

    // Requesting ride (Rider flow)
    fun requestRide() {
        val p = pickupLandmark.value ?: return
        val d = destinationLandmark.value ?: return
        val fare = getEstimatedFare()
        val dist = getEstimatedDistance()

        viewModelScope.launch {
            val result = repository.requestRide(
                pickupName = p.name,
                pickupLat = p.gridX,
                pickupLng = p.gridY,
                destinationName = d.name,
                destinationLat = d.gridX,
                destinationLng = d.gridY,
                fare = fare,
                distanceKm = dist
            )
            
            if (result.isSuccess) {
                setScreen("rider_tracking")
                startRiderSimulation(result.getOrThrow())
            }
        }
    }

    // Cancel dynamic active ride
    fun cancelActiveRide() {
        simulationJob?.cancel()
        viewModelScope.launch {
            repository.cancelActiveRide()
            setScreen("rider_home")
        }
    }

    // Simulation Engine for Rider screen live tracking
    private fun startRiderSimulation(ride: RideEntity) {
        simulationJob?.cancel()
        simulationJob = viewModelScope.launch {
            // 1. Searching for drivers (3 seconds)
            delay(3000)
            
            // Choose random mock driver
            val driverName = listOf("Amine Oran", "Yacine Belkaid", "Sid Ahmed").random()
            val driverVehicle = listOf("Dacia Logan - Yellow (31-409-12)", "Renault Symbol - White (31-105-19)", "Peugeot 301 - Grey (31-205-15)").random()
            val driverId = "driver_sim_" + (100..999).random()

            val acceptedRide = ride.copy(
                driverId = driverId,
                driverName = driverName,
                driverVehicle = driverVehicle,
                status = "accepted"
            )
            repository.rideDao.insertRide(acceptedRide)
            repository.updateRideStatus(acceptedRide.id, "accepted")

            // Driver starts at a random grid point
            var startX = (10..90).random().toFloat()
            var startY = (10..90).random().toFloat()
            _driverLocation.value = Pair(startX, startY)

            // 2. Driver Arriving: Move from random position to Rider's Pickup coordinate
            repository.updateRideStatus(acceptedRide.id, "arriving")
            _etaSeconds.value = 10
            val arrivingSteps = 20
            for (i in 1..arrivingSteps) {
                delay(500)
                val t = i.toFloat() / arrivingSteps
                val x = startX + (ride.pickupLat - startX) * t
                val y = startY + (ride.pickupLng - startY) * t
                _driverLocation.value = Pair(x, y)
                _etaSeconds.value = maxOf(0, 10 - (i / 2))
            }

            // 3. Driver Arrived (Wait for rider to hop on)
            repository.updateRideStatus(acceptedRide.id, "arrived")
            delay(3000)

            // 4. In Progress: Move from Pickup coordinate to Destination coordinate
            repository.updateRideStatus(acceptedRide.id, "inprogress")
            _etaSeconds.value = 12
            val progressSteps = 24
            for (i in 1..progressSteps) {
                delay(500)
                val t = i.toFloat() / progressSteps
                val x = ride.pickupLat + (ride.destinationLat - ride.pickupLat) * t
                val y = ride.pickupLng + (ride.destinationLng - ride.pickupLng) * t
                _driverLocation.value = Pair(x, y)
                _etaSeconds.value = maxOf(0, 12 - (i / 2))
            }

            // 5. Trip Completed
            repository.updateRideStatus(acceptedRide.id, "completed")
            loadHistory()
        }
    }

    // Submit rating for completed ride
    fun rateRide(rating: Float) {
        val active = activeRide.value ?: return
        viewModelScope.launch {
            repository.rateRide(active.id, rating)
            loadHistory()
            setScreen("rider_home")
        }
    }

    // --- DRIVER INTERACTIVE OPERATIONS ---

    // Triggered periodically when Driver toggles online
    private fun simulateRiderRequestForDriver() {
        viewModelScope.launch {
            delay(4000)
            if (currentUser.value?.isOnline == true && _currentScreen.value == "driver_home") {
                // Simulate an incoming rider request
                val startLandmark = oranLandmarks.random()
                var endLandmark = oranLandmarks.random()
                while (endLandmark.id == startLandmark.id) {
                    endLandmark = oranLandmarks.random()
                }

                val distance = getDistanceKm(startLandmark.gridX, startLandmark.gridY, endLandmark.gridX, endLandmark.gridY)
                val fare = 150.0 + (distance * 80.0)

                val simulatedRide = RideEntity(
                    id = "ride_sim_" + (1000..9999).random(),
                    riderId = "rider_sim_customer",
                    riderName = listOf("Sonia Algiers", "Kamel Oran", "Fouad Bahia", "Yasmine").random(),
                    pickupName = startLandmark.name,
                    pickupLat = startLandmark.gridX,
                    pickupLng = startLandmark.gridY,
                    destinationName = endLandmark.name,
                    destinationLat = endLandmark.gridX,
                    destinationLng = endLandmark.gridY,
                    status = "searching",
                    fare = fare,
                    distanceKm = distance
                )
                _incomingDriverRequest.value = simulatedRide
            }
        }
    }

    // Driver accepts request
    fun driverAcceptRequest() {
        val request = _incomingDriverRequest.value ?: return
        viewModelScope.launch {
            val result = repository.acceptRideRequest(request.id)
            if (result.isSuccess) {
                _incomingDriverRequest.value = null
                _currentScreen.value = "driver_nav"
                
                // Set initial driver position
                _driverLocation.value = Pair(50f, 50f) // Starts downtown
            }
        }
    }

    // Reject incoming driver alert
    fun driverRejectRequest() {
        _incomingDriverRequest.value = null
        // Trigger another request later
        simulateRiderRequestForDriver()
    }

    // Driver updates: Arrived at pickup
    fun driverNotifyArrived() {
        val ride = activeRide.value ?: return
        viewModelScope.launch {
            repository.updateRideStatus(ride.id, "arrived")
            // Instantly snap driver to the exact pickup coordinates
            _driverLocation.value = Pair(ride.pickupLat, ride.pickupLng)
        }
    }

    // Driver updates: Start customer transit
    fun driverStartRide() {
        val ride = activeRide.value ?: return
        viewModelScope.launch {
            repository.updateRideStatus(ride.id, "inprogress")
            
            // Animate moving from Pickup to Destination automatically so map displays real driving progress!
            simulationJob?.cancel()
            simulationJob = viewModelScope.launch {
                val progressSteps = 20
                for (i in 1..progressSteps) {
                    delay(500)
                    val t = i.toFloat() / progressSteps
                    val x = ride.pickupLat + (ride.destinationLat - ride.pickupLat) * t
                    val y = ride.pickupLng + (ride.destinationLng - ride.pickupLng) * t
                    _driverLocation.value = Pair(x, y)
                }
            }
        }
    }

    // Driver completes ride
    fun driverCompleteRide() {
        val ride = activeRide.value ?: return
        simulationJob?.cancel()
        viewModelScope.launch {
            repository.updateRideStatus(ride.id, "completed")
            _driverLocation.value = Pair(ride.destinationLat, ride.destinationLng)
            delay(1500)
            
            // Return to driver home
            repository.logout() // Auto logout active ride state
            _currentScreen.value = "driver_home"
            // Reload user state
            loadHistory()
        }
    }
    // ===== Place Search =====

    private val _searchResults = MutableStateFlow<List<PlaceResult>>(emptyList())
    val searchResults: StateFlow<List<PlaceResult>> = _searchResults.asStateFlow()


    fun selectSearchPlace(place: PlaceResult) {
        val lat = place.lat.toFloatOrNull() ?: return
        val lon = place.lon.toFloatOrNull() ?: return

        val landmark = OranLandmark(
            id = "search_${lat}_${lon}",
            name = place.display_name,
            gridX = ((lat - 35.60f) * 250f).coerceIn(0f,100f),
            gridY = ((lon + 0.70f) * 200f).coerceIn(0f,100f),
            description = "Search result"
        )

        destinationLandmark.value = landmark
    }

    fun searchPlaces(query: String) {
        if (query.isBlank()) {
            _searchResults.value = emptyList()
            return
        }

        viewModelScope.launch {
            try {
                val onlineResults = RetrofitClient.api.searchPlaces(
                    "$query, Oran, Algeria"
                )

                val localResults = oranPlaces
                    .filter {
                        it.name.contains(query, ignoreCase = true)
                    }
                    .map {
                        PlaceResult(
                            display_name = it.name,
                            lat = it.lat.toString(),
                            lon = it.lon.toString()
                        )
                    }

                _searchResults.value = localResults + onlineResults
            } catch (e: Exception) {
                Log.e(TAG, "Place search failed", e)
                _searchResults.value = emptyList()
            }
        }
    }
    
    fun startGps(context: Context) {
        locationHelper = LocationHelper(context)

        locationHelper?.start { lat, lon ->
            _riderLocation.value =
                Pair(lat.toFloat(), lon.toFloat())
        }
    }
}

