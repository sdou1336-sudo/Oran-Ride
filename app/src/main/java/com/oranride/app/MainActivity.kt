
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
