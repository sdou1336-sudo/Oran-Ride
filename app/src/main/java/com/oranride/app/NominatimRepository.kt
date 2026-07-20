package com.oranride.app

object NominatimRepository {

    suspend fun search(query: String): List<NominatimPlace> {
        return try {
            NominatimClient.api.search(query)
        } catch (e: Exception) {
            emptyList()
        }
    }
}
