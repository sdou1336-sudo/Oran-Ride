
package com.oranride.app

import android.content.Context
import com.google.android.gms.location.LocationServices

class LocationManager(context: Context) {

    private val client =
        LocationServices.getFusedLocationProviderClient(context)

    fun getClient() = client
}
