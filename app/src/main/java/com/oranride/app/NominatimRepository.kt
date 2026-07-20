package com.oranride.app

object NominatimRepository {

    var lastError = ""

    suspend fun search(query: String): List<NominatimPlace> {
        return try {
            lastError = ""
            val result = NominatimClient.api.search(query)
            println("RESULT: ${result.size}")
            result
        } catch (e: Exception) {
            lastError = e.message ?: "Unknown error"
            println("ERROR: $lastError")
            emptyList()
        }
    }
}
