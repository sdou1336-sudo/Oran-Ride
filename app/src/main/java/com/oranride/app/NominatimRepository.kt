package com.oranride.app

object NominatimRepository {

    suspend fun search(query: String): List<NominatimPlace> {
        println("SEARCH QUERY: $query")

        return try {
            val result = NominatimClient.api.search(query)
            println("RESULT COUNT: ${result.size}")
            result
        } catch (e: Exception) {
            println("ERROR: ${e.message}")
            emptyList()
        }
    }
}
