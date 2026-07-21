package com.oranride.app

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class DriverViewModel(
    private val repository: DriverRepository = DriverRepository()
) : ViewModel() {

    private val _drivers =
        MutableStateFlow<List<Driver>>(emptyList())

    val drivers: StateFlow<List<Driver>> = _drivers

    fun loadDrivers() {
        viewModelScope.launch {
            _drivers.value = repository.getDrivers()
        }
    }

    fun addDriver(driver: Driver) {
        viewModelScope.launch {
            repository.addDriver(driver)
            _drivers.value = repository.getDrivers()
        }
    }

    fun setDriverAvailability(
        id: String,
        available: Boolean
    ) {
        viewModelScope.launch {
            repository.updateDriverAvailability(
                id,
                available
            )
            _drivers.value = repository.getDrivers()
        }
    }
}
