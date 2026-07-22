package com.oranride.app

object NominatimRepository {
    const val REPOSITORY_VERSION = 1

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
            val ranked = result
                            .sortedByDescending { it.importance ?: 0.0 }

                      lastError = "SUCCESS: ${ranked.size}"
                      ranked
                 }
                 catch (e: Exception) {
            lastError = "ERROR: ${e.stackTraceToString()}"
            emptyList()
        }
    }

    private fun formatAddress(place: NominatimPlace): String {
        val address = place.address ?: emptyMap()

        val parts = listOfNotNull(
            address["road"],
            address["suburb"] ?: address["neighbourhood"],
            address["city"] ?: address["town"],
            "Oran"
        )

        return if (parts.isNotEmpty()) {
            parts.joinToString(", ")
        } else {
            place.displayName
        }
    }

}
