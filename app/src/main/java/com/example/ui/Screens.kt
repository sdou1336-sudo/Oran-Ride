package com.example.ui

import androidx.compose.animation.*
import androidx.compose.animation.core.*
import androidx.compose.foundation.*
import com.example.data.PlaceResult
import com.example.data.RetrofitClient
import kotlinx.coroutines.launch
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import com.example.R
import com.example.data.RideEntity
import com.example.data.UserEntity

// Visual Brand Colors - High Density Design Palette
val TaxiYellow = Color(0xFF6366F1) // Primary Indigo
val DarkBackground = Color(0xFFFEF7FF) // Soft Light Canvas
val CardBackground = Color(0xFFFFFFFF) // Pristine Card Surface
val AlgerianGreen = Color(0xFF10B981) // Emerald Green
val Slate900 = Color(0xFF0F172A) // Dark Slate text
val Slate500 = Color(0xFF64748B) // Medium Slate secondary
val Slate100 = Color(0xFFF1F5F9) // Border highlight
val Slate50 = Color(0xFFF8FAFC) // Off-white grid bg
val StarGold = Color(0xFFFACC15) // Golden Stars
val AlertRose = Color(0xFFF43F5E) // Red alerts

// Main screen controller
@Composable
fun OranRideAppContent(viewModel: OranRideViewModel) {
    val currentScreen by viewModel.currentScreen.collectAsState()
    val currentUser by viewModel.currentUser.collectAsState()

    Surface(
        modifier = Modifier.fillMaxSize(),
        color = DarkBackground
    ) {
        Crossfade(targetState = currentScreen, label = "screen_transition") { screen ->
            when (screen) {
                "mode_select" -> ModeSelectScreen(viewModel)
                "register" -> RegisterScreen(viewModel)
                "rider_home" -> RiderHomeScreen(viewModel)
                "rider_tracking" -> RiderTrackingScreen(viewModel)
                "driver_home" -> DriverHomeScreen(viewModel)
                "driver_nav" -> DriverNavScreen(viewModel)
                "history" -> HistoryScreen(viewModel)
            }
        }
    }
}

// 1. Mode Select (Welcome & Role Choosing)
@Composable
fun ModeSelectScreen(viewModel: OranRideViewModel) {
    val context = LocalContext.current
    val isFirebaseReady = viewModel.isFirebaseReady

    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.SpaceBetween
    ) {
        // Upper Branding Section
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            modifier = Modifier.padding(top = 16.dp)
        ) {
            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.Center
            ) {
                Icon(
                    imageName = Icons.Filled.LocalTaxi,
                    contentDescription = "Taxi Icon",
                    tint = TaxiYellow,
                    modifier = Modifier.size(36.dp)
                )
                Spacer(modifier = Modifier.width(8.dp))
                Text(
                    text = "Oran Ride",
                    fontSize = 32.sp,
                    fontWeight = FontWeight.ExtraBold,
                    color = Slate900
                )
            }
            Text(
                text = "باهية وهران - Bahia Ride Sharing",
                fontSize = 14.sp,
                fontWeight = FontWeight.Bold,
                color = Slate500,
                modifier = Modifier.padding(top = 4.dp)
            )
        }

        // Generated Hero Image Banner
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(200.dp)
                .clip(RoundedCornerShape(24.dp))
                .shadow(8.dp, RoundedCornerShape(24.dp))
        ) {
            Image(
                painter = painterResource(id = R.drawable.oran_ride_banner),
                contentDescription = "Oran Bahia Ride Banner",
                contentScale = ContentScale.Crop,
                modifier = Modifier.fillMaxSize()
            )
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .background(
                        Brush.verticalGradient(
                            colors = listOf(Color.Transparent, Color.Black.copy(alpha = 0.75f))
                        )
                    )
            )
            Text(
                text = "Explore Oran with Comfort\nاستكشف وهران بكل راحة وأمان",
                color = Color.White,
                fontSize = 15.sp,
                fontWeight = FontWeight.Bold,
                textAlign = TextAlign.Center,
                modifier = Modifier
                    .align(Alignment.BottomCenter)
                    .padding(bottom = 12.dp)
            )
        }

        // Selection Cards
        Column(
            modifier = Modifier.fillMaxWidth(),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            Text(
                text = "Select your role to begin / اختر حسابك للبدء",
                color = Slate500,
                fontSize = 14.sp,
                fontWeight = FontWeight.SemiBold,
                textAlign = TextAlign.Center,
                modifier = Modifier.fillMaxWidth()
            )

            // Rider Selector Card
            Card(
                onClick = {
                    viewModel.register("Rider Bahia", "+213 555 01 02 03", "rider", null)
                },
                colors = CardDefaults.cardColors(containerColor = CardBackground),
                shape = RoundedCornerShape(20.dp),
                border = BorderStroke(1.dp, Slate100),
                modifier = Modifier
                    .fillMaxWidth()
                    .shadow(4.dp, RoundedCornerShape(20.dp))
                    .testTag("select_rider_role")
            ) {
                Row(
                    modifier = Modifier
                        .padding(20.dp)
                        .fillMaxWidth(),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Box(
                        modifier = Modifier
                            .size(54.dp)
                            .background(TaxiYellow.copy(alpha = 0.1f), CircleShape),
                        contentAlignment = Alignment.Center
                    ) {
                        Icon(Icons.Filled.Person, "Rider", tint = TaxiYellow, modifier = Modifier.size(30.dp))
                    }
                    Spacer(modifier = Modifier.width(16.dp))
                    Column {
                        Text("I am a Rider (أنا راكب)", color = Slate900, fontSize = 18.sp, fontWeight = FontWeight.Bold)
                        Text("Book rides instantly inside Oran", color = Slate500, fontSize = 13.sp)
                    }
                }
            }

            // Driver Selector Card
            Card(
                onClick = {
                    // Navigate to custom register to specify vehicle
                    viewModel.setScreen("register")
                },
                colors = CardDefaults.cardColors(containerColor = CardBackground),
                shape = RoundedCornerShape(20.dp),
                border = BorderStroke(1.dp, Slate100),
                modifier = Modifier
                    .fillMaxWidth()
                    .shadow(4.dp, RoundedCornerShape(20.dp))
                    .testTag("select_driver_role")
            ) {
                Row(
                    modifier = Modifier
                        .padding(20.dp)
                        .fillMaxWidth(),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Box(
                        modifier = Modifier
                            .size(54.dp)
                            .background(AlgerianGreen.copy(alpha = 0.1f), CircleShape),
                        contentAlignment = Alignment.Center
                    ) {
                        Icon(Icons.Filled.DriveEta, "Driver", tint = AlgerianGreen, modifier = Modifier.size(30.dp))
                    }
                    Spacer(modifier = Modifier.width(16.dp))
                    Column {
                        Text("I am a Driver (أنا سائق)", color = Slate900, fontSize = 18.sp, fontWeight = FontWeight.Bold)
                        Text("Accept requests & earn fares in DZD", color = Slate500, fontSize = 13.sp)
                    }
                }
            }
        }

        // Firebase Sync Status Footer
        Row(
            modifier = Modifier.padding(vertical = 12.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            Box(
                modifier = Modifier
                    .size(8.dp)
                    .background(if (isFirebaseReady) AlgerianGreen else TaxiYellow, CircleShape)
            )
            Spacer(modifier = Modifier.width(6.dp))
            Text(
                text = if (isFirebaseReady) "Firebase Cloud Connected" else "Local SQLite Mode Enabled",
                color = Slate500,
                fontSize = 11.sp
            )
        }
    }
}

// 2. Registration screen
@Composable
fun RegisterScreen(viewModel: OranRideViewModel) {
    var name by remember { mutableStateOf("") }
    var phone by remember { mutableStateOf("") }
    var vehicleInfo by remember { mutableStateOf("") }
    var isDriver by remember { mutableStateOf(true) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
            .padding(24.dp),
        verticalArrangement = Arrangement.spacedBy(18.dp)
    ) {
        IconButton(
            onClick = { viewModel.setScreen("mode_select") },
            modifier = Modifier.padding(top = 8.dp)
        ) {
            Icon(Icons.Filled.ArrowBack, "Back", tint = Slate900)
        }

        Text(
            text = "Create Profile\nإنشاء حساب جديد",
            color = Slate900,
            fontSize = 28.sp,
            fontWeight = FontWeight.ExtraBold
        )

        OutlinedTextField(if (searchResults.isNotEmpty()) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 12.dp)
            .align(Alignment.TopCenter),
        shape = RoundedCornerShape(16.dp),
        colors = CardDefaults.cardColors(
            containerColor = Color.White
        )
    ) {
        Column(
            modifier = Modifier.padding(8.dp)
        ) {
            searchResults.forEach { place ->

                Text(
                    text = place.display_name,
                    color = Slate900,
                    fontSize = 14.sp,
                    modifier = Modifier
                        .fillMaxWidth()
                        .clickable {
    searchText = place.display_name

    selectedLat = place.lat.toDouble()
    selectedLon = place.lon.toDouble()

    searchResults = emptyList()
}
                            
                        }
                        .padding(12.dp)
                )
            }
        }
    }
}
            value = name,
            onValueChange = { name = it },
            label = { Text("Full Name (الاسم الكامل)") },
            colors = OutlinedTextFieldDefaults.colors(
                focusedTextColor = Slate900,
                unfocusedTextColor = Slate900,
                focusedBorderColor = TaxiYellow,
                unfocusedBorderColor = Slate500,
                focusedLabelColor = TaxiYellow,
                unfocusedLabelColor = Slate500
            ),
            modifier = Modifier.fillMaxWidth().testTag("register_name_input")
        )

        OutlinedTextField(
            value = phone,
            onValueChange = { phone = it },
            label = { Text("Phone Number (رقم الهاتف)") },
            colors = OutlinedTextFieldDefaults.colors(
                focusedTextColor = Slate900,
                unfocusedTextColor = Slate900,
                focusedBorderColor = TaxiYellow,
                unfocusedBorderColor = Slate500,
                focusedLabelColor = TaxiYellow,
                unfocusedLabelColor = Slate500
            ),
            modifier = Modifier.fillMaxWidth().testTag("register_phone_input")
        )

        // Conditional Driver Fields
        if (isDriver) {
            OutlinedTextField(
                value = vehicleInfo,
                onValueChange = { vehicleInfo = it },
                placeholder = { Text("e.g. Dacia Logan - Yellow (31-105-19)") },
                label = { Text("Car details & Plate (تفاصيل السيارة ورقم اللوحة)") },
                colors = OutlinedTextFieldDefaults.colors(
                    focusedTextColor = Slate900,
                    unfocusedTextColor = Slate900,
                    focusedBorderColor = AlgerianGreen,
                    unfocusedBorderColor = Slate500,
                    focusedLabelColor = AlgerianGreen,
                    unfocusedLabelColor = Slate500
                ),
                modifier = Modifier.fillMaxWidth().testTag("register_vehicle_input")
            )
        }

        Button(
            onClick = {
                if (name.isNotEmpty() && phone.isNotEmpty()) {
                    viewModel.register(name, phone, if (isDriver) "driver" else "rider", vehicleInfo)
                }
            },
            colors = ButtonDefaults.buttonColors(containerColor = if (isDriver) AlgerianGreen else TaxiYellow),
            modifier = Modifier
                .fillMaxWidth()
                .padding(top = 12.dp)
                .height(54.dp)
                .testTag("submit_registration"),
            shape = RoundedCornerShape(12.dp),
            enabled = name.isNotEmpty() && phone.isNotEmpty() && (!isDriver || vehicleInfo.isNotEmpty())
        ) {
            Text(
                "Register Profile (تسجيل)",
                color = Color.White,
                fontWeight = FontWeight.Bold,
                fontSize = 16.sp
            )
        }
    }
}

// 3. Rider Home (Map and Booking Panel)
@Composable
fun RiderHomeScreen(viewModel: OranRideViewModel) {
    val currentUser by viewModel.currentUser.collectAsState()
    val pickup by viewModel.pickupLandmark
    val destination by viewModel.destinationLandmark
    val category by viewModel.selectedCategory

    var showPickupDialog by remember { mutableStateOf(false) }
    var showDestDialog by remember { mutableStateOf(false) }var searchText by remember { mutableStateOf("") }
var searchResults by remember { mutableStateOf<List<PlaceResult>>(emptyList()) }
var selectedLat by remember { mutableStateOf<Double?>(null) }
var selectedLon by remember { mutableStateOf<Double?>(null) }
val scope = rememberCoroutineScope()
    Column(modifier = Modifier.fillMaxSize()) {
        // App bar
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 20.dp, vertical = 12.dp)
                .padding(top = 16.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Column {
                Text(
                    "Bahia Rider (الراكب)",
                    color = Slate900,
                    fontSize = 20.sp,
                    fontWeight = FontWeight.ExtraBold
                )
                Text(
                    "Hello, ${currentUser?.name ?: "Guest"}",
                    color = Slate500,
                    fontSize = 13.sp
                )
            }
            
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                // Wallet indicator
                Box(
                    modifier = Modifier
                        .background(CardBackground, RoundedCornerShape(12.dp))
                        .border(1.dp, Slate100, RoundedCornerShape(12.dp))
                        .padding(horizontal = 12.dp, vertical = 8.dp)
                ) {
                    Text(
                        "${currentUser?.walletBalance?.toInt() ?: 0} DZD",
                        color = AlgerianGreen,
                        fontWeight = FontWeight.Bold,
                        fontSize = 13.sp
                    )
                }
                
                IconButton(onClick = { viewModel.logout() }) {
                    Icon(Icons.Filled.ExitToApp, "Logout", tint = AlertRose)
                }
            }
        }

        // Live Vector Map of Oran (Takes upper/center area)
        Box(
            modifier = Modifier
                .weight(1.0f)
                .padding(horizontal = 16.dp)
                .clip(RoundedCornerShape(20.dp))
                .border(1.dp, Slate100, RoundedCornerShape(20.dp))
        ) {
                modifier = Modifier.fillMaxSize()
)RealMap(
    modifier = Modifier.fillMaxSize(),
    targetLat = selectedLat,
    targetLon = selectedLon
)

OutlinedTextField(
    value = searchText,
    onValueChange = { text ->
        searchText = text

        if (text.length > 2) {
            scope.launch {
                try {
                    searchResults = RetrofitClient.api.searchPlaces(text)
                } catch (e: Exception) {
                    searchResults = emptyList()
                }
            }
        }
    },
    placeholder = {
        Text("إلى أين؟ ابحث عن مكان")
    },
    leadingIcon = {
        Icon(Icons.Filled.Search, "Search")
    },
    modifier = Modifier
        .fillMaxWidth()
        .padding(12.dp)
        .align(Alignment.TopCenter),
    shape = RoundedCornerShape(20.dp)
)

OutlinedTextField(
    value = "",
    onValueChange = {},
    placeholder = { Text("إلى أين؟ ابحث عن مكان") },
    leadingIcon = {
        Icon(Icons.Filled.Search, "Search")
    },
    modifier = Modifier
        .fillMaxWidth()
        .padding(12.dp)
        .align(Alignment.TopCenter),
   shape = RoundedCornerShape(20.dp),
colors = OutlinedTextFieldDefaults.colors(
    focusedContainerColor = Color.White,
    unfocusedContainerColor = Color.White,
    focusedBorderColor = TaxiYellow,
    unfocusedBorderColor = Slate100
)
)
        // Slide-up Booking Panel
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp)
                .shadow(6.dp, RoundedCornerShape(24.dp)),
            colors = CardDefaults.cardColors(containerColor = CardBackground),
            shape = RoundedCornerShape(24.dp),
            border = BorderStroke(1.dp, Slate100)
        ) {
            Column(
                modifier = Modifier.padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(14.dp)
            ) {
                // Pickup Select Button
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .clickable { showPickupDialog = true }
                        .background(Slate50, RoundedCornerShape(12.dp))
                        .padding(12.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Icon(Icons.Filled.TripOrigin, "Pickup", tint = AlgerianGreen, modifier = Modifier.size(18.dp))
                    Spacer(modifier = Modifier.width(12.dp))
                    Column {
                        Text("Pickup From (من):", color = Slate500, fontSize = 11.sp)
                        Text(pickup?.name ?: "Tap to select pickup landmark", color = Slate900, fontSize = 14.sp, fontWeight = FontWeight.Bold)
                    }
                }

                // Destination Select Button
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .clickable { showDestDialog = true }
                        .background(Slate50, RoundedCornerShape(12.dp))
                        .padding(12.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Icon(Icons.Filled.Place, "Destination", tint = AlertRose, modifier = Modifier.size(18.dp))
                    Spacer(modifier = Modifier.width(12.dp))
                    Column {
                        Text("Dropoff To (إلى):", color = Slate500, fontSize = 11.sp)
                        Text(destination?.name ?: "Tap to select destination landmark", color = Slate900, fontSize = 14.sp, fontWeight = FontWeight.Bold)
                    }
                }

                // Category Slider
                Row(
                    modifier = Modifier.fillMaxWidth().horizontalScroll(rememberScrollState()),
                    horizontalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    listOf("Standard", "Luxe", "Comfort", "Moto").forEach { cat ->
                        val isSelected = category == cat
                        Box(
                            modifier = Modifier
                                .background(
                                    if (isSelected) TaxiYellow else Slate50,
                                    RoundedCornerShape(12.dp)
                                )
                                .border(
                                    BorderStroke(1.dp, if (isSelected) TaxiYellow else Slate100),
                                    RoundedCornerShape(12.dp)
                                )
                                .clickable { viewModel.selectedCategory.value = cat }
                                .padding(horizontal = 16.dp, vertical = 10.dp)
                        ) {
                            Text(
                                cat,
                                color = if (isSelected) Color.White else Slate500,
                                fontWeight = FontWeight.Bold,
                                fontSize = 13.sp
                            )
                        }
                    }
                }

                // Estimated fare details
                if (pickup != null && destination != null) {
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Column {
                            Text("Estimated Fare (الأجرة المقدرة)", color = Slate500, fontSize = 12.sp)
                            Text("${viewModel.getEstimatedFare().toInt()} DZD", color = AlgerianGreen, fontSize = 22.sp, fontWeight = FontWeight.ExtraBold)
                        }
                        Text(
                            "${String.format("%.1f", viewModel.getEstimatedDistance())} KM | ~${(viewModel.getEstimatedDistance() * 2).toInt()} mins",
                            color = Slate500,
                            fontSize = 13.sp,
                            fontWeight = FontWeight.Bold
                        )
                    }
                }

                // Request Ride Button
                Button(
                    onClick = { viewModel.requestRide() },
                    colors = ButtonDefaults.buttonColors(containerColor = TaxiYellow),
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(52.dp)
                        .testTag("request_ride_button"),
                    shape = RoundedCornerShape(14.dp),
                    enabled = pickup != null && destination != null && pickup?.id != destination?.id
                ) {
                    Text(
                        "REQUEST BAHA RIDE (طلب رحلة)",
                        color = Color.White,
                        fontWeight = FontWeight.ExtraBold,
                        fontSize = 15.sp
                    )
                }
            }
        }
    }

    // Landmark Choice Dialogs
    if (showPickupDialog) {
        LandmarkSelectorDialog(onDismiss = { showPickupDialog = false }) { selected ->
            viewModel.pickupLandmark.value = selected
            showPickupDialog = false
        }
    }
    if (showDestDialog) {
        LandmarkSelectorDialog(onDismiss = { showDestDialog = false }) { selected ->
            viewModel.destinationLandmark.value = selected
            showDestDialog = false
        }
    }
}

// Dialog picker for Landmarks
@Composable
fun LandmarkSelectorDialog(onDismiss: () -> Unit, onSelect: (OranLandmark) -> Unit) {
    Dialog(onDismissRequest = onDismiss) {
        Card(
            colors = CardDefaults.cardColors(containerColor = CardBackground),
            shape = RoundedCornerShape(24.dp),
            border = BorderStroke(1.dp, Slate100),
            modifier = Modifier.padding(16.dp).shadow(12.dp, RoundedCornerShape(24.dp))
        ) {
            Column(
                modifier = Modifier
                    .padding(20.dp)
                    .fillMaxWidth(),
                verticalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                Text(
                    "Select Location / اختر المكان",
                    color = Slate900,
                    fontSize = 18.sp,
                    fontWeight = FontWeight.Bold,
                    modifier = Modifier.padding(bottom = 8.dp)
                )

                LazyColumn(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                    items(oranLandmarks) { landmark ->
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .clickable { onSelect(landmark) }
                                .background(Slate50, RoundedCornerShape(12.dp))
                                .padding(12.dp),
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Icon(Icons.Filled.LocationOn, "Icon", tint = TaxiYellow, modifier = Modifier.size(20.dp))
                            Spacer(modifier = Modifier.width(12.dp))
                            Column {
                                Text(landmark.name, color = Slate900, fontSize = 14.sp, fontWeight = FontWeight.Bold)
                                Text(landmark.description, color = Slate500, fontSize = 11.sp)
                            }
                        }
                    }
                }
            }
        }
    }
}

// 4. Rider Tracking & Live Map Simulation
@Composable
fun RiderTrackingScreen(viewModel: OranRideViewModel) {
    val activeRide by viewModel.activeRide.collectAsState()
    val driverLoc by viewModel.driverLocation.collectAsState()
    val eta by viewModel.etaSeconds.collectAsState()

    var ratingScore by remember { mutableStateOf(5f) }
    var showRatingDialog by remember { mutableStateOf(false) }

    LaunchedEffect(activeRide?.status) {
        if (activeRide?.status == "completed") {
            showRatingDialog = true
        }
    }

    Column(modifier = Modifier.fillMaxSize()) {
        // App bar / status
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 20.dp, vertical = 12.dp)
                .padding(top = 16.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Text(
                "Tracking Bahia Ride (تتبع الرحلة)",
                color = Slate900,
                fontSize = 18.sp,
                fontWeight = FontWeight.Bold
            )
            IconButton(
                onClick = { viewModel.cancelActiveRide() },
                modifier = Modifier.testTag("cancel_ride")
            ) {
                Icon(Icons.Filled.Close, "Cancel", tint = AlertRose)
            }
        }

        // Map takes major area
        Box(
            modifier = Modifier
                .weight(1f)
                .padding(horizontal = 16.dp)
                .clip(RoundedCornerShape(20.dp))
                .border(1.dp, Slate100, RoundedCornerShape(20.dp))
        ) {
            OranMap(
                pickupLandmarkId = oranLandmarks.firstOrNull { it.name == activeRide?.pickupName }?.id,
                destinationLandmarkId = oranLandmarks.firstOrNull { it.name == activeRide?.destinationName }?.id,
                driverGridX = driverLoc?.first,
                driverGridY = driverLoc?.second
            )
        }

        // Live Progress details panel
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp)
                .shadow(6.dp, RoundedCornerShape(24.dp)),
            colors = CardDefaults.cardColors(containerColor = CardBackground),
            shape = RoundedCornerShape(24.dp),
            border = BorderStroke(1.dp, Slate100)
        ) {
            Column(
                modifier = Modifier.padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(14.dp)
            ) {
                // Status header
                val statusTitle = when (activeRide?.status) {
                    "searching" -> "Finding drivers near you... (البحث عن سائق)"
                    "accepted", "arriving" -> "Driver is arriving in ${eta}s (وصول السائق)"
                    "arrived" -> "Your Taxi is Here! (لقد وصل السائق)"
                    "inprogress" -> "In Transit to destination (أنت في الطريق)"
                    "completed" -> "You have arrived! (وصلت بالسلامة)"
                    else -> "Processing..."
                }

                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Text(
                        statusTitle,
                        color = TaxiYellow,
                        fontWeight = FontWeight.Bold,
                        fontSize = 15.sp,
                        modifier = Modifier.weight(1f)
                    )
                    
                    if (activeRide?.status == "searching") {
                        CircularProgressIndicator(color = TaxiYellow, modifier = Modifier.size(20.dp), strokeWidth = 2.dp)
                    } else {
                        Icon(
                            imageVector = if (activeRide?.status == "inprogress") Icons.Filled.Navigation else Icons.Filled.LocalTaxi,
                            contentDescription = "Active",
                            tint = AlgerianGreen
                        )
                    }
                }

                // Show matched driver info
                if (activeRide?.driverId != null) {
                    HorizontalDivider(color = Slate100)
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Box(
                            modifier = Modifier
                                .size(48.dp)
                                .background(TaxiYellow.copy(alpha = 0.1f), CircleShape),
                            contentAlignment = Alignment.Center
                        ) {
                            Icon(Icons.Filled.AccountCircle, "Driver", tint = TaxiYellow, modifier = Modifier.size(36.dp))
                        }
                        Spacer(modifier = Modifier.width(12.dp))
                        Column(modifier = Modifier.weight(1f)) {
                            Text(activeRide?.driverName ?: "Bahia Driver", color = Slate900, fontWeight = FontWeight.Bold, fontSize = 15.sp)
                            Text(activeRide?.driverVehicle ?: "Yellow Taxi", color = Slate500, fontSize = 12.sp)
                        }
                        Column(horizontalAlignment = Alignment.End) {
                            Text("Fare (الأجرة)", color = Slate500, fontSize = 11.sp)
                            Text("${activeRide?.fare?.toInt()} DZD", color = AlgerianGreen, fontWeight = FontWeight.Bold, fontSize = 15.sp)
                        }
                    }
                }

                // Step progress indicators
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {
                    val statusOrder = listOf("searching", "arriving", "inprogress", "completed")
                    val currentIdx = statusOrder.indexOf(activeRide?.status ?: "searching")

                    statusOrder.forEachIndexed { idx, stat ->
                        val isDone = currentIdx >= idx
                        Box(
                            modifier = Modifier
                                .weight(1f)
                                .height(4.dp)
                                .padding(horizontal = 2.dp)
                                .background(
                                    if (isDone) AlgerianGreen else Slate100,
                                    RoundedCornerShape(2.dp)
                                )
                        )
                    }
                }
            }
        }
    }

    // Rating pop-up on completion
    if (showRatingDialog) {
        Dialog(onDismissRequest = { showRatingDialog = false }) {
            Card(
                colors = CardDefaults.cardColors(containerColor = CardBackground),
                shape = RoundedCornerShape(24.dp),
                border = BorderStroke(1.dp, Slate100),
                modifier = Modifier.padding(16.dp).shadow(12.dp, RoundedCornerShape(24.dp))
            ) {
                Column(
                    modifier = Modifier.padding(20.dp),
                    horizontalAlignment = Alignment.CenterHorizontally,
                    verticalArrangement = Arrangement.spacedBy(16.dp)
                ) {
                    Text(
                        "How was your Oran ride?\nكيف كانت رحلتك؟",
                        color = Slate900,
                        fontSize = 18.sp,
                        fontWeight = FontWeight.Bold,
                        textAlign = TextAlign.Center
                    )

                    // Draw 5 stars
                    Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                        for (i in 1..5) {
                            val active = ratingScore >= i
                            Icon(
                                imageVector = if (active) Icons.Filled.Star else Icons.Filled.StarBorder,
                                contentDescription = "Star",
                                tint = StarGold,
                                modifier = Modifier
                                    .size(36.dp)
                                    .clickable { ratingScore = i.toFloat() }
                            )
                        }
                    }

                    Button(
                        onClick = {
                            viewModel.rateRide(ratingScore)
                            showRatingDialog = false
                        },
                        colors = ButtonDefaults.buttonColors(containerColor = TaxiYellow),
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(48.dp)
                            .testTag("submit_rating"),
                        shape = RoundedCornerShape(12.dp)
                    ) {
                        Text("SUBMIT RATING", color = Color.White, fontWeight = FontWeight.Bold)
                    }
                }
            }
        }
    }
}

// 5. Driver Home Dashboard
@Composable
fun DriverHomeScreen(viewModel: OranRideViewModel) {
    val currentUser by viewModel.currentUser.collectAsState()
    val incomingReq by viewModel.incomingDriverRequest.collectAsState()
    val isOnline = currentUser?.isOnline ?: false

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        // Driver header
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(top = 16.dp, bottom = 12.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Column {
                Text(
                    "Bahia Driver Dashboard",
                    color = Slate900,
                    fontSize = 20.sp,
                    fontWeight = FontWeight.ExtraBold
                )
                Text(
                    "Pilot: ${currentUser?.name ?: "Professional Driver"}",
                    color = Slate500,
                    fontSize = 13.sp
                )
            }
            IconButton(onClick = { viewModel.logout() }) {
                Icon(Icons.Filled.ExitToApp, "Logout", tint = AlertRose)
            }
        }

        // Live map to display background driver hub
        Box(
            modifier = Modifier
                .weight(0.8f)
                .fillMaxWidth()
                .clip(RoundedCornerShape(20.dp))
                .border(1.dp, Slate100, RoundedCornerShape(20.dp))
        ) {
            OranMap()
            
            // Online Floating Trigger Overlay
            Card(
                modifier = Modifier
                    .align(Alignment.BottomCenter)
                    .padding(12.dp)
                    .shadow(8.dp, RoundedCornerShape(14.dp)),
                colors = CardDefaults.cardColors(containerColor = CardBackground),
                shape = RoundedCornerShape(14.dp),
                border = BorderStroke(1.dp, Slate100)
            ) {
                Row(
                    modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(12.dp)
                ) {
                    Text(
                        if (isOnline) "ONLINE & WAITING (متصل)" else "OFFLINE (غير متصل)",
                        color = if (isOnline) AlgerianGreen else Slate500,
                        fontWeight = FontWeight.Bold,
                        fontSize = 13.sp
                    )
                    Switch(
                        checked = isOnline,
                        onCheckedChange = { viewModel.setDriverOnline(it) },
                        colors = SwitchDefaults.colors(
                            checkedThumbColor = AlgerianGreen,
                            checkedTrackColor = AlgerianGreen.copy(alpha = 0.3f),
                            uncheckedThumbColor = Slate500,
                            uncheckedTrackColor = Slate100
                        ),
                        modifier = Modifier.testTag("driver_status_switch")
                    )
                }
            }
        }

        Spacer(modifier = Modifier.height(14.dp))

        // Driver Performance Metrics Card
        Card(
            modifier = Modifier.fillMaxWidth().shadow(4.dp, RoundedCornerShape(20.dp)),
            colors = CardDefaults.cardColors(containerColor = CardBackground),
            shape = RoundedCornerShape(20.dp),
            border = BorderStroke(1.dp, Slate100)
        ) {
            Row(
                modifier = Modifier
                    .padding(16.dp)
                    .fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text("Total Earned", color = Slate500, fontSize = 11.sp)
                    Text("${currentUser?.walletBalance?.toInt()} DZD", color = AlgerianGreen, fontSize = 18.sp, fontWeight = FontWeight.Bold)
                }
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text("Rating", color = Slate500, fontSize = 11.sp)
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Icon(Icons.Filled.Star, "Star", tint = StarGold, modifier = Modifier.size(16.dp))
                        Spacer(modifier = Modifier.width(4.dp))
                        Text("4.9", color = Slate900, fontSize = 18.sp, fontWeight = FontWeight.Bold)
                    }
                }
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text("Active Status", color = Slate500, fontSize = 11.sp)
                    Text(
                        if (isOnline) "Searching" else "Resting",
                        color = if (isOnline) AlgerianGreen else AlertRose,
                        fontSize = 16.sp,
                        fontWeight = FontWeight.Bold
                    )
                }
            }
        }

        // Active Alert Overlay for new requests
        if (incomingReq != null) {
            Dialog(onDismissRequest = { viewModel.driverRejectRequest() }) {
                Card(
                    colors = CardDefaults.cardColors(containerColor = CardBackground),
                    shape = RoundedCornerShape(24.dp),
                    border = BorderStroke(2.dp, TaxiYellow),
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(16.dp)
                        .shadow(12.dp, RoundedCornerShape(24.dp))
                        .testTag("incoming_request_dialog")
                ) {
                    Column(
                        modifier = Modifier.padding(20.dp),
                        verticalArrangement = Arrangement.spacedBy(14.dp)
                    ) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Text("NEW RIDE IN ORAN!", color = TaxiYellow, fontSize = 16.sp, fontWeight = FontWeight.ExtraBold)
                            Text("10s left", color = AlertRose, fontSize = 11.sp, fontWeight = FontWeight.Bold)
                        }

                        Column {
                            Text("RIDER (الراكب):", color = Slate500, fontSize = 11.sp)
                            Text(incomingReq?.riderName ?: "Customer Bahia", color = Slate900, fontSize = 15.sp, fontWeight = FontWeight.Bold)
                        }

                        Column {
                            Text("PICKUP (مكان الإنطلاق):", color = Slate500, fontSize = 11.sp)
                            Text(incomingReq?.pickupName ?: "Front de Mer", color = AlgerianGreen, fontSize = 14.sp, fontWeight = FontWeight.Bold)
                        }

                        Column {
                            Text("DROPOFF (مكان الوصول):", color = Slate500, fontSize = 11.sp)
                            Text(incomingReq?.destinationName ?: "Santa Cruz", color = AlertRose, fontSize = 14.sp, fontWeight = FontWeight.Bold)
                        }

                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            Column {
                                Text("DISTANCE", color = Slate500, fontSize = 10.sp)
                                Text("${String.format("%.1f", incomingReq?.distanceKm)} KM", color = Slate900, fontWeight = FontWeight.Bold)
                            }
                            Column(horizontalAlignment = Alignment.End) {
                                Text("EST. PAYOUT", color = Slate500, fontSize = 10.sp)
                                Text("${incomingReq?.fare?.toInt()} DZD", color = AlgerianGreen, fontSize = 18.sp, fontWeight = FontWeight.Bold)
                            }
                        }

                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.spacedBy(12.dp)
                        ) {
                            OutlinedButton(
                                onClick = { viewModel.driverRejectRequest() },
                                colors = ButtonDefaults.outlinedButtonColors(contentColor = Slate900),
                                border = BorderStroke(1.dp, Slate100),
                                modifier = Modifier.weight(1f),
                                shape = RoundedCornerShape(12.dp)
                            ) {
                                Text("Reject", fontWeight = FontWeight.Bold)
                            }

                            Button(
                                onClick = { viewModel.driverAcceptRequest() },
                                colors = ButtonDefaults.buttonColors(containerColor = AlgerianGreen),
                                modifier = Modifier
                                    .weight(1f)
                                    .testTag("accept_ride_button"),
                                shape = RoundedCornerShape(12.dp)
                            ) {
                                Text("ACCEPT", color = Color.White, fontWeight = FontWeight.Bold)
                            }
                        }
                    }
                }
            }
        }
    }
}

// 6. Driver Turn-by-Turn Navigation Screen
@Composable
fun DriverNavScreen(viewModel: OranRideViewModel) {
    val activeRide by viewModel.activeRide.collectAsState()
    val driverLoc by viewModel.driverLocation.collectAsState()

    Column(modifier = Modifier.fillMaxSize()) {
        // App header
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 20.dp, vertical = 12.dp)
                .padding(top = 16.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Text(
                "Driver Navigation Map",
                color = Slate900,
                fontSize = 18.sp,
                fontWeight = FontWeight.Bold
            )
            Icon(Icons.Filled.Navigation, "Nav", tint = AlgerianGreen)
        }

        // Live tracking map takes major center
        Box(
            modifier = Modifier
                .weight(1f)
                .padding(horizontal = 16.dp)
                .clip(RoundedCornerShape(20.dp))
                .border(1.dp, Slate100, RoundedCornerShape(20.dp))
        ) {
            OranMap(
                pickupLandmarkId = oranLandmarks.firstOrNull { it.name == activeRide?.pickupName }?.id,
                destinationLandmarkId = oranLandmarks.firstOrNull { it.name == activeRide?.destinationName }?.id,
                driverGridX = driverLoc?.first,
                driverGridY = driverLoc?.second
            )
        }

        // Action controls Panel
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp)
                .shadow(6.dp, RoundedCornerShape(24.dp)),
            colors = CardDefaults.cardColors(containerColor = CardBackground),
            shape = RoundedCornerShape(24.dp),
            border = BorderStroke(1.dp, Slate100)
        ) {
            Column(
                modifier = Modifier.padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(14.dp)
            ) {
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {
                    Column {
                        Text("PASSENGER (الراكب)", color = Slate500, fontSize = 11.sp)
                        Text(activeRide?.riderName ?: "Bahia Rider", color = Slate900, fontWeight = FontWeight.Bold, fontSize = 16.sp)
                    }
                    Column(horizontalAlignment = Alignment.End) {
                        Text("EARNINGS", color = Slate500, fontSize = 11.sp)
                        Text("${activeRide?.fare?.toInt()} DZD", color = AlgerianGreen, fontWeight = FontWeight.ExtraBold, fontSize = 18.sp)
                    }
                }

                HorizontalDivider(color = Slate100)

                // Navigation targets info
                Row(modifier = Modifier.fillMaxWidth()) {
                    Column(modifier = Modifier.weight(1f)) {
                        Text("FROM (من)", color = Slate500, fontSize = 10.sp)
                        Text(activeRide?.pickupName ?: "Front de Mer", color = Slate900, fontSize = 13.sp, fontWeight = FontWeight.SemiBold)
                    }
                    Column(modifier = Modifier.weight(1f), horizontalAlignment = Alignment.End) {
                        Text("TO (إلى)", color = Slate500, fontSize = 10.sp)
                        Text(activeRide?.destinationName ?: "Santa Cruz", color = Slate900, fontSize = 13.sp, fontWeight = FontWeight.SemiBold)
                    }
                }

                // Dynamic buttons based on transit step
                val currentStatus = activeRide?.status ?: "accepted"
                
                when (currentStatus) {
                    "accepted", "arriving" -> {
                        Button(
                            onClick = { viewModel.driverNotifyArrived() },
                            colors = ButtonDefaults.buttonColors(containerColor = TaxiYellow),
                            modifier = Modifier
                                .fillMaxWidth()
                                .height(50.dp)
                                .testTag("driver_arrived_button"),
                            shape = RoundedCornerShape(14.dp)
                        ) {
                            Text("I HAVE ARRIVED (لقد وصلت مكان الزبون)", color = Color.White, fontWeight = FontWeight.Bold)
                        }
                    }
                    "arrived" -> {
                        Button(
                            onClick = { viewModel.driverStartRide() },
                            colors = ButtonDefaults.buttonColors(containerColor = AlgerianGreen),
                            modifier = Modifier
                                .fillMaxWidth()
                                .height(50.dp)
                                .testTag("driver_start_ride_button"),
                            shape = RoundedCornerShape(14.dp)
                        ) {
                            Text("START TRANSIT (بدء الرحلة الآن)", color = Color.White, fontWeight = FontWeight.Bold)
                        }
                    }
                    "inprogress" -> {
                        Button(
                            onClick = { viewModel.driverCompleteRide() },
                            colors = ButtonDefaults.buttonColors(containerColor = AlertRose),
                            modifier = Modifier
                                .fillMaxWidth()
                                .height(50.dp)
                                .testTag("driver_complete_ride_button"),
                            shape = RoundedCornerShape(14.dp)
                        ) {
                            Text("COMPLETE TRIP (إنهاء الرحلة وتحصيل المبلغ)", color = Color.White, fontWeight = FontWeight.Bold)
                        }
                    }
                }
            }
        }
    }
}

// 7. Ride History / Archive Screen
@Composable
fun HistoryScreen(viewModel: OranRideViewModel) {
    val history by viewModel.rideHistory.collectAsState()

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        IconButton(
            onClick = { viewModel.setScreen("mode_select") },
            modifier = Modifier.padding(top = 16.dp)
        ) {
            Icon(Icons.Filled.ArrowBack, "Back", tint = Slate900)
        }

        Text(
            "Trips Archive (أرشيف الرحلات)",
            color = Slate900,
            fontSize = 24.sp,
            fontWeight = FontWeight.Bold,
            modifier = Modifier.padding(vertical = 12.dp)
        )

        if (history.isEmpty()) {
            Box(
                modifier = Modifier.fillMaxSize(),
                contentAlignment = Alignment.Center
            ) {
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Icon(Icons.Filled.History, "Empty", tint = Slate500, modifier = Modifier.size(64.dp))
                    Spacer(modifier = Modifier.height(12.dp))
                    Text("No rides recorded yet\nلا توجد رحلات مسجلة حالياً", color = Slate500, textAlign = TextAlign.Center)
                }
            }
        } else {
            LazyColumn(
                verticalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                items(history) { ride ->
                    Card(
                        colors = CardDefaults.cardColors(containerColor = CardBackground),
                        shape = RoundedCornerShape(16.dp),
                        border = BorderStroke(1.dp, Slate100),
                        modifier = Modifier.fillMaxWidth().shadow(2.dp, RoundedCornerShape(16.dp))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween
                            ) {
                                Text(
                                    text = if (ride.status == "completed") "Completed (مكتملة)" else "Cancelled (ملغاة)",
                                    color = if (ride.status == "completed") AlgerianGreen else AlertRose,
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 12.sp
                                )
                                Text("${ride.fare.toInt()} DZD", color = AlgerianGreen, fontWeight = FontWeight.Bold)
                            }
                            Text("Pickup: ${ride.pickupName}", color = Slate900, fontSize = 13.sp)
                            Text("Dropoff: ${ride.destinationName}", color = Slate900, fontSize = 13.sp)
                            
                            if (ride.ratingGiven != null) {
                                Row(verticalAlignment = Alignment.CenterVertically) {
                                    Text("Rating: ", color = Slate500, fontSize = 11.sp)
                                    for (i in 1..5) {
                                        Icon(
                                            Icons.Filled.Star,
                                            "Star",
                                            tint = if (ride.ratingGiven >= i) StarGold else Slate100,
                                            modifier = Modifier.size(12.dp)
                                        )
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

// Utility Composable to use named icons easily
@Composable
fun Icon(imageName: Any, contentDescription: String, tint: Color, modifier: Modifier = Modifier) {
    when (imageName) {
        is androidx.compose.ui.graphics.vector.ImageVector -> {
            Icon(
                imageVector = imageName,
                contentDescription = contentDescription,
                tint = tint,
                modifier = modifier
            )
        }
    }
}
