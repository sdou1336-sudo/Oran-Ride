package com.oranride.app

object NominatimRepository {

    var lastError = ""

    suspend fun search(query: String): List<NominatimPlace> {
        return try {
            val result = NominatimClient.api.search(query)
            lastError = "SUCCESS: ${result.size}"
            result
        } catch (e: Exception) {
            lastError = "ERROR: ${e::class.simpleName} ${e.message}"
            emptyList()
        }
    }
}
