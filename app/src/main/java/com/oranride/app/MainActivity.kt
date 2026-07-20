package com.oranride.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.foundation.layout.*
import androidx.compose.ui.Alignment

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

    var page by remember { mutableStateOf("الخريطة") }

    Scaffold(
        bottomBar = {
            NavigationBar {
                listOf("الخريطة", "الرحلات", "البحث", "الرسائل", "الحساب")
                    .forEach { item ->
                        NavigationBarItem(
                            selected = page == item,
                            onClick = { page = item },
                            icon = {},
                            label = { Text(item) }
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
            Text(
                text = page,
                style = MaterialTheme.typography.headlineMedium
            )
        }
    }
}
