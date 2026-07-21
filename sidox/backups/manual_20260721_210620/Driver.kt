package com.oranride.app

data class Driver(
    val id: String,
    val name: String,
    val phone: String,
    val carModel: String,
    val plateNumber: String,
    val available: Boolean = false
)
