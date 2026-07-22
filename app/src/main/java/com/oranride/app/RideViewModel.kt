
package com.oranride.app

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow

class RideViewModel : ViewModel() {

    private val _rides =
        MutableStateFlow<List<RideRequest>>(emptyList())

    val rides = _rides.asStateFlow()

    fun requestRide(ride: RideRequest) {
        _rides.value = _rides.value + ride
    }
}
