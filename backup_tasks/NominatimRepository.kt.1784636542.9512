package com.oranride.app

object NominatimRepository {

    var lastError = ""

    suspend fun search(query: String): List<NominatimPlace> {
        return try {
            val searchQuery = if (query.contains("oran", ignoreCase = true) || query.contains("وهران")) {
            query
        } else {
            "$query, Oran, Algeria"
        }

        val improvedQuery = searchQuery
                .trim()
                .replace("  ", " ")

            val result = NominatimClient.api.search(
                "$improvedQuery, Oran, Algeria",
                limit = 20,
                addressDetails = 1
            )
            lastError = "SUCCESS: ${result.size}"
            result
        } catch (e: Exception) {
            lastError = "ERROR: ${e::class.simpleName} ${e.message}"
            emptyList()
        }
    }
}
