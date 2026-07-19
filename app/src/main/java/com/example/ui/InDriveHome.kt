package com.example.ui

import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier

@Composable
fun InDriveHome() {
    Scaffold(
        bottomBar = {
            NavigationBar {
                NavigationBarItem(
                    selected = true,
                    onClick = {},
                    icon = {},
                    label = { Text("خريطة") }
                )
                NavigationBarItem(
                    selected = false,
                    onClick = {},
                    icon = {},
                    label = { Text("بحث") }
                )
                NavigationBarItem(
                    selected = false,
                    onClick = {},
                    icon = {},
                    label = { Text("رحلات") }
                )
            }
        }
    ) { padding ->

        Surface(modifier = Modifier) {

            Text(
                text = "🗺️ Oran-Ride\n\nGPS\nبحث عن المكان\nاختيار الوجهة\nطلب رحلة",
                modifier = Modifier
            )
        }
    }
}
