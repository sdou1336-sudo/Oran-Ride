package com.oranride.app

data class LocationState(
    val latitude: Double? = null,
    val longitude: Double? = null,
    val isLocationAvailable: Boolean = false
)
