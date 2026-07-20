package com.oranride.app

object NominatimRepository {

    suspend fun search(query: String): List<NominatimPlace> {
        return try {
            val result = NominatimClient.api.search(query)
            println("NOMINATIM RESULT: ${result.size}")
            result
        } catch (e: Exception) {
            println("NOMINATIM ERROR: ${e.message}")
            emptyList()
        }
    }
}
