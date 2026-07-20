package com.oranride.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
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

                "الخريطة" -> MapPage()

                "الرحلات" -> TripsPage()

                "البحث" -> SearchPage()

                "الرسائل" -> MessagesPage()

                "الحساب" -> ProfilePage()
            }
        }
    }
}


@Composable
fun MapPage() {

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
fun SearchPage() {
    Text("صفحة البحث عن الوجهة")
}

@Composable
fun MessagesPage() {
    Text("صفحة الرسائل")
}

@Composable
fun ProfilePage() {
    Text("صفحة الحساب")
}
