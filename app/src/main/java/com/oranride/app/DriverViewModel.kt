
package com.oranride.app

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow

class DriverViewModel : ViewModel() {

    private val _drivers =
        MutableStateFlow<List<Driver>>(emptyList())

    val drivers = _drivers.asStateFlow()

    fun loadDrivers() {
        _drivers.value = listOf(
            Driver("1","Driver")
        )
    }
}
