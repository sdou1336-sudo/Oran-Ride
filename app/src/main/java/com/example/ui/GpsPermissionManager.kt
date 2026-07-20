package com.example.ui

import android.Manifest
import android.content.Context
import android.content.Intent
import android.location.LocationManager
import android.provider.Settings
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.core.content.ContextCompat
import com.google.android.gms.location.LocationServices

@Composable
fun GpsPermissionManager(
    onLocationReady: (Double, Double) -> Unit
) {

    val context = androidx.compose.ui.platform.LocalContext.current

    var showGpsDialog by remember { mutableStateOf(false) }

    val permissionLauncher =
        rememberLauncherForActivityResult(
            ActivityResultContracts.RequestPermission()
        ) { granted ->

            if (granted) {
                getLocation(context, onLocationReady)
            }
        }


    LaunchedEffect(Unit) {

        val manager =
            context.getSystemService(Context.LOCATION_SERVICE) as LocationManager

        val enabled =
            manager.isProviderEnabled(LocationManager.GPS_PROVIDER)

        if (!enabled) {
            showGpsDialog = true
        } else {

            permissionLauncher.launch(
                Manifest.permission.ACCESS_FINE_LOCATION
            )
        }
    }


    if (showGpsDialog) {

        AlertDialog(
            onDismissRequest = {},
            title = {
                Text("تفعيل GPS")
            },
            text = {
                Text("يجب تفعيل الموقع حتى يعمل Oran Ride ويحدد مكانك على الخريطة")
            },
            confirmButton = {

                Button(
                    onClick = {

                        context.startActivity(
                            Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS)
                        )

                        showGpsDialog = false
                    }
                ) {

                    Text("تفعيل GPS")
                }
            }
        )
    }
}


private fun getLocation(
    context: Context,
    onLocationReady: (Double, Double) -> Unit
) {

    val client =
        LocationServices.getFusedLocationProviderClient(context)

    if (
        ContextCompat.checkSelfPermission(
            context,
            Manifest.permission.ACCESS_FINE_LOCATION
        ) ==
        android.content.pm.PackageManager.PERMISSION_GRANTED
    ) {

        client.lastLocation.addOnSuccessListener { location ->

            location?.let {

                onLocationReady(
                    it.latitude,
                    it.longitude
                )
            }
        }
    }
}
