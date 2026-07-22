package com.oranride.app

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class RideViewModel(
    private val repository: RideRepository = RideRepository()
) : ViewModel() {

    private val _selectedRide = MutableStateFlow<RideRequest?>(null)

    val selectedRide: StateFlow<RideRequest?> = _selectedRide

    private val _rides =
        MutableStateFlow<List<RideRequest>>(emptyList())

    val rides: StateFlow<List<RideRequest>> = _rides

    fun loadRides() {
        viewModelScope.launch {
            _rides.value = repository.getRides()
        }
    }

    fun addRide(request: RideRequest) {
        viewModelScope.launch {
            repository.addRide(request)
            _rides.value = repository.getRides()
        }
    }

    fun acceptRide(id: String) {
        viewModelScope.launch {
            repository.acceptRide(id)
            val ride = repository.getRides()
                .firstOrNull { it.id == id }
            _selectedRide.value = ride
            _rides.value = repository.getRides()
        }
    }
}
