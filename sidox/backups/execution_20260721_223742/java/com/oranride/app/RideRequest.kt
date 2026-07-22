package com.oranride.app

data class RideRequest(
    val id: String,
    val passengerName: String,
    val pickup: String,
    val destination: String,
    val pickupLat: Double = 35.6969,
    val pickupLon: Double = -0.6331,
    val destinationLat: Double = 35.6510,
    val destinationLon: Double = -0.6400,
    val price: Double,
    val accepted: Boolean = false
)
