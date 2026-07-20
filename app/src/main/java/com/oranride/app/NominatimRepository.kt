package com.oranride.app

object NominatimRepository {

    var lastError = ""

    suspend fun search(query: String): List<NominatimPlace> {
        return try {
            
            val result = NominatimClient.api.search(query)
            lastError = "OK ${result.size}"
            result
        } catch (e: Exception) {
            lastError = e.toString()
            emptyList()
        }
    }
}
