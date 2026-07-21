package com.example.data

import android.content.Context
import android.util.Log
import androidx.room.Room
import com.google.firebase.FirebaseApp
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.firestore.FirebaseFirestore
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.launch
import kotlinx.coroutines.tasks.await
import kotlinx.coroutines.withContext
import java.util.UUID

class OranRideRepository(private val context: Context) {

    private val TAG = "OranRideRepository"

    // Initialize Room Database
    private val db: OranRideDatabase by lazy {
        Room.databaseBuilder(
            context.applicationContext,
            OranRideDatabase::class.java,
            "oran_ride_db"
        ).fallbackToDestructiveMigration().build()
    }

    val userDao by lazy { db.userDao() }
    val rideDao by lazy { db.rideDao() }

    // Firebase state detection
    val isFirebaseEnabled: Boolean by lazy {
        try {
            FirebaseApp.getInstance()
            true
        } catch (e: Exception) {
            Log.w(TAG, "Firebase is not initialized. Operating in local-offline mode. Add google-services.json for live cloud storage.")
            false
        }
    }

    private val firebaseAuth: FirebaseAuth? by lazy {
        if (isFirebaseEnabled) FirebaseAuth.getInstance() else null
    }

    private val firestore: FirebaseFirestore? by lazy {
        if (isFirebaseEnabled) FirebaseFirestore.getInstance() else null
    }

    // Current logged-in user state
    private val _currentUser = MutableStateFlow<UserEntity?>(null)
    val currentUser: StateFlow<UserEntity?> = _currentUser.asStateFlow()

    // Track active ride in real-time
    private val _activeRide = MutableStateFlow<RideEntity?>(null)
    val activeRide: StateFlow<RideEntity?> = _activeRide.asStateFlow()

    init {
        // Pre-populate mock driver profile and some initial local data if database is empty
        CoroutineScope(Dispatchers.IO).launch {
            try {
                // Check if current user is saved in Room
                val savedUserId = context.getSharedPreferences("oran_ride_prefs", Context.MODE_PRIVATE)
                    .getString("current_user_id", null)
                
                if (savedUserId != null) {
                    val user = userDao.getUserById(savedUserId)
                    if (user != null) {
                        _currentUser.value = user
                    }
                }
            } catch (e: Exception) {
                Log.e(TAG, "Error loading saved user", e)
            }
        }
    }

    // Register user (rider/driver)
    suspend fun registerUser(name: String, phone: String, role: String, vehicleInfo: String?): Result<UserEntity> = withContext(Dispatchers.IO) {
        try {
            val userId = if (isFirebaseEnabled && firebaseAuth?.currentUser != null) {
                firebaseAuth!!.currentUser!!.uid
            } else {
                "local_" + UUID.randomUUID().toString().take(8)
            }

            val user = UserEntity(
                id = userId,
                name = name,
                phone = phone,
                role = role,
                vehicleInfo = if (role == "driver") vehicleInfo else null,
                isOnline = false,
                rating = 4.9f,
                walletBalance = if (role == "driver") 1500.0 else 500.0 // Give some starting balance in DZD
            )

            // Save to Room
            userDao.insertUser(user)

            // Save to Firebase Firestore if enabled
            if (isFirebaseEnabled && firestore != null) {
                try {
                    firestore!!.collection("users").document(userId).set(user).await()
                    Log.d(TAG, "Saved profile to Firestore")
                } catch (fe: Exception) {
                    Log.e(TAG, "Failed to save profile to Firestore, saved locally", fe)
                }
            }

            // Save ID locally
            context.getSharedPreferences("oran_ride_prefs", Context.MODE_PRIVATE)
                .edit()
                .putString("current_user_id", userId)
                .apply()

            _currentUser.value = user
            Result.success(user)
        } catch (e: Exception) {
            Log.e(TAG, "Registration error", e)
            Result.failure(e)
        }
    }

    // Login/Select active user profile
    suspend fun selectUserProfile(user: UserEntity) = withContext(Dispatchers.IO) {
        userDao.insertUser(user)
        context.getSharedPreferences("oran_ride_prefs", Context.MODE_PRIVATE)
            .edit()
            .putString("current_user_id", user.id)
            .apply()
        _currentUser.value = user
    }

    // Toggle Driver Online Status
    suspend fun toggleDriverOnline(isOnline: Boolean) = withContext(Dispatchers.IO) {
        val user = _currentUser.value ?: return@withContext
        if (user.role != "driver") return@withContext

        val updatedUser = user.copy(isOnline = isOnline)
        userDao.insertUser(updatedUser)
        _currentUser.value = updatedUser

        if (isFirebaseEnabled && firestore != null) {
            try {
                firestore!!.collection("users").document(user.id)
                    .update("online", isOnline).await()
            } catch (e: Exception) {
                Log.e(TAG, "Failed to update online status in Firestore", e)
            }
        }
    }

    // Log out / clear session
    suspend fun logout() = withContext(Dispatchers.IO) {
        val user = _currentUser.value
        if (user != null && user.role == "driver") {
            toggleDriverOnline(false)
        }
        
        context.getSharedPreferences("oran_ride_prefs", Context.MODE_PRIVATE)
            .edit()
            .remove("current_user_id")
            .apply()

        _currentUser.value = null
        _activeRide.value = null
    }

    // Request a ride (Rider)
    suspend fun requestRide(
        pickupName: String, pickupLat: Float, pickupLng: Float,
        destinationName: String, destinationLat: Float, destinationLng: Float,
        fare: Double, distanceKm: Float
    ): Result<RideEntity> = withContext(Dispatchers.IO) {
        try {
            val rider = _currentUser.value ?: throw Exception("No logged-in user")
            val rideId = "ride_" + UUID.randomUUID().toString().take(8)

            val ride = RideEntity(
                id = rideId,
                riderId = rider.id,
                riderName = rider.name,
                pickupName = pickupName,
                pickupLat = pickupLat,
                pickupLng = pickupLng,
                destinationName = destinationName,
                destinationLat = destinationLat,
                destinationLng = destinationLng,
                status = "searching",
                fare = fare,
                distanceKm = distanceKm
            )

            // Save locally
            rideDao.insertRide(ride)
            _activeRide.value = ride

            // Save to Firestore
            if (isFirebaseEnabled && firestore != null) {
                try {
                    firestore!!.collection("rides").document(rideId).set(ride).await()
                } catch (e: Exception) {
                    Log.e(TAG, "Failed to save ride to Firestore", e)
                }
            }

            Result.success(ride)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // Cancel dynamic active ride
    suspend fun cancelActiveRide() = withContext(Dispatchers.IO) {
        val ride = _activeRide.value ?: return@withContext
        val updatedRide = ride.copy(status = "cancelled")
        rideDao.insertRide(updatedRide)
        _activeRide.value = null

        if (isFirebaseEnabled && firestore != null) {
            try {
                firestore!!.collection("rides").document(ride.id).update("status", "cancelled").await()
            } catch (e: Exception) {
                Log.e(TAG, "Failed to cancel ride in Firestore", e)
            }
        }
    }

    // Driver: Accept a ride request
    suspend fun acceptRideRequest(rideId: String): Result<RideEntity> = withContext(Dispatchers.IO) {
        try {
            val driver = _currentUser.value ?: throw Exception("No driver logged in")
            if (driver.role != "driver") throw Exception("User is not a driver")

            val ride = rideDao.getRideById(rideId) ?: throw Exception("Ride not found")
            val updatedRide = ride.copy(
                driverId = driver.id,
                driverName = driver.name,
                driverVehicle = driver.vehicleInfo ?: "Standard Vehicle",
                status = "accepted"
            )

            rideDao.insertRide(updatedRide)
            _activeRide.value = updatedRide

            if (isFirebaseEnabled && firestore != null) {
                try {
                    firestore!!.collection("rides").document(rideId).set(updatedRide).await()
                } catch (e: Exception) {
                    Log.e(TAG, "Failed to accept ride in Firestore", e)
                }
            }

            Result.success(updatedRide)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    // Update ride status (both driver and simulated flow)
    suspend fun updateRideStatus(rideId: String, newStatus: String) = withContext(Dispatchers.IO) {
        val ride = rideDao.getRideById(rideId) ?: _activeRide.value ?: return@withContext
        if (ride.id == rideId || _activeRide.value?.id == rideId) {
            val updatedRide = ride.copy(status = newStatus)
            rideDao.insertRide(updatedRide)
            _activeRide.value = updatedRide

            if (isFirebaseEnabled && firestore != null) {
                try {
                    firestore!!.collection("rides").document(rideId).update("status", newStatus).await()
                } catch (e: Exception) {
                    Log.e(TAG, "Failed to update ride status in Firestore", e)
                }
            }

            // Deduct or add money upon completion
            if (newStatus == "completed") {
                val riderId = ride.riderId
                val driverId = ride.driverId
                
                // Deduct from rider (if local profile)
                val current = _currentUser.value
                if (current != null) {
                    if (current.id == riderId) {
                        val updated = current.copy(walletBalance = maxOf(0.0, current.walletBalance - ride.fare))
                        userDao.insertUser(updated)
                        _currentUser.value = updated
                    } else if (driverId != null && current.id == driverId) {
                        val updated = current.copy(walletBalance = current.walletBalance + ride.fare)
                        userDao.insertUser(updated)
                        _currentUser.value = updated
                    }
                }
            }
        }
    }

    // Submit rating for completed ride
    suspend fun rateRide(rideId: String, rating: Float) = withContext(Dispatchers.IO) {
        val ride = rideDao.getRideById(rideId) ?: return@withContext
        val updatedRide = ride.copy(ratingGiven = rating)
        rideDao.insertRide(updatedRide)
        if (_activeRide.value?.id == rideId) {
            _activeRide.value = null
        }

        if (isFirebaseEnabled && firestore != null) {
            try {
                firestore!!.collection("rides").document(rideId).update("ratingGiven", rating).await()
            } catch (e: Exception) {
                Log.e(TAG, "Failed to submit rating in Firestore", e)
            }
        }
    }

    // Query active ride updates (Rider listening to updates)
    fun observeActiveRide(rideId: String): Flow<RideEntity?> = flow {
        // Emit current active ride from repository first
        emit(_activeRide.value)
        // Then continuously query the database
        while (true) {
            kotlinx.coroutines.delay(1000)
            val updatedRide = rideDao.getRideById(rideId)
            emit(updatedRide)
            if (updatedRide == null || updatedRide.status == "completed" || updatedRide.status == "cancelled") {
                break
            }
        }
    }

    // Listen to active open requests for drivers
    fun getActiveRequests(): Flow<List<RideEntity>> = rideDao.getActiveRequests()

    // Get ride history
    fun getRideHistory(): Flow<List<RideEntity>> {
        val user = _currentUser.value
        return if (user == null) {
            flow { emit(emptyList<RideEntity>()) }
        } else if (user.role == "driver") {
            rideDao.getRidesForDriver(user.id)
        } else {
            rideDao.getRidesForRider(user.id)
        }
    }

    // Insert mock drivers for local map density
    suspend fun insertMockDrivers() = withContext(Dispatchers.IO) {
        val driver1 = UserEntity("driver_mock1", "Yacine Belkaid", "+213 555 12 34 56", "driver", "Renault Symbol - White (31-105-19)", true, 4.8f, 2500.0)
        val driver2 = UserEntity("driver_mock2", "Amine Oran", "+213 661 98 76 54", "driver", "Dacia Logan - Yellow (31-409-12)", true, 4.9f, 3200.0)
        val driver3 = UserEntity("driver_mock3", "Sid Ahmed", "+213 770 45 61 23", "driver", "Peugeot 301 - Grey (31-205-15)", true, 4.7f, 1800.0)
        
        userDao.insertUser(driver1)
        userDao.insertUser(driver2)
        userDao.insertUser(driver3)
    }
}
