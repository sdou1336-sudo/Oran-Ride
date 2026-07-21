package com.oranride.app

class DriverRepository {

    private val drivers = mutableListOf<Driver>()

    fun getDrivers(): List<Driver> {
        return drivers
    }

    fun addDriver(driver: Driver) {
        drivers.add(driver)
    }

    fun updateDriverAvailability(
        id: String,
        available: Boolean
    ) {
        val index = drivers.indexOfFirst { it.id == id }

        if (index != -1) {
            val old = drivers[index]

            drivers[index] = old.copy(
                available = available
            )
        }
    }
}
