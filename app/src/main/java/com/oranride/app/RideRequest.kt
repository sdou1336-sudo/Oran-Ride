
package com.oranride.app

data class RideRequest(
    val id: String,
    val passengerName: String,
    val pickup: String,
    val destination: String,
    val pickupLat: Double,
    val pickupLon: Double,
    val price: Double,
    var accepted: Boolean = false
)
