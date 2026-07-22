package com.oranride.app.debug

data class UIState(
    val currentScreen: String = "",
    val searchQuery: String = "",
    val searchResults: Int = 0,
    val selectedPlace: String = "",
    val mapLat: Double = 0.0,
    val mapLon: Double = 0.0,
    val lastError: String = ""
)

object UIStateHolder {
    var state = UIState()
}
