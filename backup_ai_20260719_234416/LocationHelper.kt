
package com.example.ui

import android.annotation.SuppressLint
import android.content.Context
import android.location.Location
import com.google.android.gms.location.*

class LocationHelper(
    private val context: Context
) {

    private val client =
        LocationServices.getFusedLocationProviderClient(context)

    @SuppressLint("MissingPermission")
    fun start(
        onLocation: (Double, Double) -> Unit
    ) {

        val request = LocationRequest.Builder(
            Priority.PRIORITY_HIGH_ACCURACY,
            3000
        ).build()

        client.requestLocationUpdates(
            request,
            object : LocationCallback() {
                override fun onLocationResult(
                    result: LocationResult
                ) {
                    val loc = result.lastLocation ?: return
                    onLocation(
                        loc.latitude,
                        loc.longitude
                    )
                }
            },
            context.mainLooper
        )
    }
}
