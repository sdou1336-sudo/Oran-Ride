package com.oranride.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.ui.unit.dp
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.platform.LocalSoftwareKeyboardController
import androidx.compose.material3.OutlinedTextField
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.ui.Modifier
import androidx.compose.ui.viewinterop.AndroidView
import org.osmdroid.views.MapView
import org.osmdroid.util.GeoPoint
import org.osmdroid.config.Configuration

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

    AndroidView(
        modifier = Modifier.fillMaxSize(),
        factory = { context ->

            Configuration.getInstance().userAgentValue =
                context.packageName

            val map = MapView(context)

            map.setMultiTouchControls(true)

            map.controller.setZoom(14.0)

            map.controller.setCenter(
                GeoPoint(35.6969, -0.6331)
            )

            map
        }
    )
}

@Composable
fun TripsPage() {
    Text("صفحة الرحلات")
}

@Composable
fun SearchPage(
    onPlaceSelected: (Double, Double) -> Unit
) {

    var query by remember { mutableStateOf("") }
    var results by remember { mutableStateOf(listOf<Place>()) }

    val keyboardController = LocalSoftwareKeyboardController.current

    val places = PlacesDatabase.places

    Column(
        modifier = Modifier.fillMaxSize()
    ) {

        OutlinedTextField(
            value = query,
            onValueChange = {
                query = it
            },
            label = { Text("أين تريد الذهاب؟") },
            singleLine = true,

            keyboardOptions = KeyboardOptions(
                imeAction = ImeAction.Search
            ),

            keyboardActions = KeyboardActions(
                onSearch = {
                    results = places.filter {
                        it.contains(query)
                    }
                    keyboardController?.hide()
                }
            )
        )

        LazyColumn {
            items(results) { place ->
                Text(
                    text = place.name,
                    modifier = Modifier.padding(16.dp).clickable {
                        onPlaceSelected(
                                                        place.latitude,
                                                        place.longitude
                                                    )
                    }
                )
            }
        }
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
