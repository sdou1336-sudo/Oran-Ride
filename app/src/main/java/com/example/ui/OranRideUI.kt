package com.example.ui

import androidx.compose.animation.Crossfade
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color

@Composable
fun OranRideNewUI(viewModel: OranRideViewModel) {

    val currentScreen by viewModel.currentScreen.collectAsState()

    GpsPermissionManager { lat, lon ->
        // GPS location ready
    }

    Surface(
        modifier = Modifier.fillMaxSize(),
        color = Color(0xFFFEF7FF)
    ) {

        Crossfade(
            targetState = currentScreen,
            label = "main_ui_transition"
        ) { screen ->

            when (screen) {

                "indrive_home" -> InDriveMainScreen()

                "mode_select" -> ModeSelectScreen(viewModel)

                "register" -> RegisterScreen(viewModel)

                "rider_home" -> RiderHomeScreen(viewModel)

                "rider_tracking" -> RiderTrackingScreen(viewModel)

                "driver_home" -> DriverHomeScreen(viewModel)

                "driver_nav" -> DriverNavScreen(viewModel)

                "history" -> HistoryScreen(viewModel)

                else -> ModeSelectScreen(viewModel)
            }
        }
    }
}
