package com.oranride.app
import com.oranride.app.NominatimRepository

import android.os.Bundle
import androidx.activity.result.contract.ActivityResultContracts
import android.Manifest
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.ui.unit.dp
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.foundation.text.KeyboardActions
import kotlinx.coroutines.launch
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.platform.LocalSoftwareKeyboardController
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.ui.Modifier
import androidx.compose.ui.viewinterop.AndroidView
import org.osmdroid.views.MapView
import org.osmdroid.views.overlay.Marker
import org.osmdroid.util.GeoPoint
import org.osmdroid.config.Configuration

class MainActivity : ComponentActivity() {

    private val requestLocationPermission =
        registerForActivityResult(ActivityResultContracts.RequestPermission()) { }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        requestLocationPermission.launch(Manifest.permission.ACCESS_FINE_LOCATION)

        setContent {
            OranRideApp()
        }
    }
}

@Composable
fun OranRideApp() {

    var currentPage by remember { mutableStateOf("الخريطة") }
    var selectedLat by remember { mutableStateOf(35.6969) }
    var selectedLon by remember { mutableStateOf(-0.6331) }

    Scaffold(
        bottomBar = {
            NavigationBar {

                val pages = listOf(
                    "الخريطة",
                    "الرحلات",
                    "البحث",
                    "الرسائل",
                    "الحساب"
                )

                pages.forEach { page ->

                    NavigationBarItem(
                        selected = currentPage == page,
                        onClick = {
                            currentPage = page
                        },
                        icon = {},
                        label = {
                            Text(page)
                        }
                    )
                }
            }
        }
    ) { padding ->

        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding),
            contentAlignment = Alignment.Center
        ) {

            when(currentPage) {

                "الخريطة" -> MapPage(
                    selectedLat,
                    selectedLon
                )

                "الرحلات" -> TripsPage()

                "البحث" -> SearchPage(
                    onPlaceSelected = { lat, lon ->
                        selectedLat = lat
                        selectedLon = lon
                        currentPage = "الخريطة"
                    }
                )

                "الرسائل" -> MessagesPage()

                "الحساب" -> ProfilePage()
            }
        }
    }
}


@Composable
fun MapPage(
    latitude: Double,
    longitude: Double
) {

    var mapView: MapView? = null
    var selectedMarker: Marker? = null

    Box(
        modifier = Modifier.fillMaxSize()
    ) {

        AndroidView(
            modifier = Modifier.fillMaxSize(),
            factory = { context ->

                Configuration.getInstance().userAgentValue =
                    context.packageName

                val map = MapView(context)
                mapView = map

                map.setMultiTouchControls(true)

                map.controller.setZoom(14.0)

                map.controller.setCenter(
                    GeoPoint(latitude, longitude)
                )

                map
            }
        )

        SearchBar(
            onPlaceSelected = { lat, lon ->
                mapView?.let { map ->

                    val point = GeoPoint(lat, lon)

                    selectedMarker?.let {
                        map.overlays.remove(it)
                    }

                    selectedMarker = Marker(map).apply {
                        position = point
                        title = "الوجهة"
                    }

                    map.overlays.add(selectedMarker)

                    map.controller.setZoom(17.0)
                    map.controller.animateTo(point)
                    map.invalidate()
                }
            }
        )
    }
}

@Composable
fun TripsPage() {
    Text("صفحة الرحلات")
}

@Composable
fun SearchPage(
    onPlaceSelected: (Double, Double) -> Unit
) {
    Column(
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text("البحث عن الأماكن")
        Text("نتائج البحث")
    
    var searchResults = remember { mutableStateListOf<String>() }
    
    // ربط نتائج Nominatim
    // سيتم تحديث القائمة عند تنفيذ البحث
    val nominatimRepository = NominatimRepository

    fun moveMapToLocation(latitude: Double, longitude: Double) {
        // تحريك الخريطة إلى نتيجة البحث
        println("Move map: $latitude,$longitude")
    }
    
    
    fun searchPlaces(query: String) {
        searchResults.clear()

        println("Searching: $query")

        kotlinx.coroutines.CoroutineScope(kotlinx.coroutines.Dispatchers.Main).launch {
            val results = NominatimRepository.search(query)

            results.forEach {
                searchResults.add(
                    it.displayName ?: "${it.lat}, ${it.lon}"
                )
            }
        }
    }
    
    
    
        Spacer(modifier = Modifier.height(16.dp))

        searchResults.forEach { place ->
            Text(
                text = place,
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(8.dp)
                    .clickable {
                        println("Selected place: $place")
                    }
            )
        }

        Text("جاهز لعرض نتائج الأماكن من Nominatim")
    }
}

@Composable
fun MessagesPage() {
    Text("صفحة الرسائل")
}

@Composable
fun ProfilePage() {
    Text("صفحة الحساب")
}
