TEMPLATES = {
"Driver.kt": """
package com.oranride.app

data class Driver(
    val id: String,
    val name: String
)
""",

"DriverViewModel.kt": """
package com.oranride.app

class DriverViewModel {
}
"""
}

TEMPLATES.update({
"RealMap.kt": """
package com.oranride.app

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.ui.viewinterop.AndroidView
import org.osmdroid.views.MapView
import org.osmdroid.util.GeoPoint

@Composable
fun RealMap() {
    AndroidView(
        modifier = Modifier.fillMaxSize(),
        factory = { context ->
            MapView(context).apply {
                setMultiTouchControls(true)
                controller.setZoom(14.0)
                controller.setCenter(
                    GeoPoint(35.6971, -0.6308)
                )
            }
        }
    )
}
""",
"LocationManager.kt": """
package com.oranride.app

import android.content.Context
import com.google.android.gms.location.LocationServices

class LocationManager(context: Context) {

    private val client =
        LocationServices.getFusedLocationProviderClient(context)

    fun getClient() = client
}
""",
"SearchBar.kt": """
package com.oranride.app

import androidx.compose.runtime.*
import androidx.compose.material3.*
import androidx.compose.ui.Modifier

@Composable
fun SearchBar(
    onSearch: (String) -> Unit
) {
    var text by remember { mutableStateOf("") }

    OutlinedTextField(
        value = text,
        onValueChange = { text = it },
        modifier = Modifier,
        label = { Text("ابحث عن مكان") },
        singleLine = true
    )
}
""",
"NominatimRepository.kt": """
package com.oranride.app

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

class NominatimRepository {

    suspend fun search(query: String): List<String> {
        return withContext(Dispatchers.IO) {
            listOf(query)
        }
    }
}
""",
"RideRequest.kt": """
package com.oranride.app

data class RideRequest(
    val id: String,
    val passengerName: String,
    val pickup: String,
    val destination: String,
    val pickupLat: Double,
    val pickupLon: Double,
    val price: Double,
    var accepted: Boolean = false
)
""",
"RideViewModel.kt": """
package com.oranride.app

class RideViewModel {
}
"""
})

TEMPLATES.update({
"MainActivity.kt": """
package com.oranride.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.*

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            OranRideApp()
        }
    }
}

@Composable
fun OranRideApp() {
    Scaffold(
        bottomBar = {
            NavigationBar {
                NavigationBarItem(
                    selected = true,
                    onClick = {},
                    icon = {},
                    label = { Text("الخريطة") }
                )
            }
        }
    ) {
        RealMap()
    }
}
"""
})

TEMPLATES.update({
"DriverViewModel.kt": """
package com.oranride.app

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow

class DriverViewModel : ViewModel() {

    private val _drivers =
        MutableStateFlow<List<Driver>>(emptyList())

    val drivers = _drivers.asStateFlow()

    fun loadDrivers() {
        _drivers.value = listOf(
            Driver("1","Driver")
        )
    }
}
""",

"RideViewModel.kt": """
package com.oranride.app

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow

class RideViewModel : ViewModel() {

    private val _rides =
        MutableStateFlow<List<RideRequest>>(emptyList())

    val rides = _rides.asStateFlow()

    fun requestRide(ride: RideRequest) {
        _rides.value = _rides.value + ride
    }
}
"""
})
