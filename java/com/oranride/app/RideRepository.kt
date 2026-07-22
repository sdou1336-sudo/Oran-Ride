package com.oranride.app

class RideRepository {

    private val rides = mutableListOf(
        RideRequest(
            id = "1",
            passengerName = "راكب تجريبي",
            pickup = "وهران",
            destination = "السانية",
            pickupLat = 35.6969,
            pickupLon = -0.6331,
            destinationLat = 35.6510,
            destinationLon = -0.6400,
            price = 500.0
        )
    )

    fun getRides(): List<RideRequest> {
        return rides
    }

    fun addRide(request: RideRequest) {
        rides.add(request)
    }

    fun acceptRide(id: String) {
        val index = rides.indexOfFirst { it.id == id }

        if (index != -1) {
            val old = rides[index]
            rides[index] = old.copy(
                accepted = true
            )
        }
    }
}
