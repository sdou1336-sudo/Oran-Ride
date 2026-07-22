// SIDOX_PATCH
package com.oranride.app

class DriverRepository {

    private val drivers = mutableListOf(
        Driver(
            id = "1",
            name = "سائق تجريبي",
            phone = "0000000000",
            carModel = "Toyota",
            plateNumber = "OR-001",
            available = true
        )
    )

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
