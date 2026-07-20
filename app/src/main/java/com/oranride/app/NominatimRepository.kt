package com.oranride.app

object NominatimRepository {

    var lastError = ""

    suspend fun search(query: String): List<NominatimPlace> {
        return try {
            if (query == "test") {
                return listOf(
                    NominatimPlace(
                        "Oran Test",
                        "35.7044",
                        "-0.6502"
                    )
                )
            }
            val result = NominatimClient.api.search(query)
            lastError = "OK ${result.size}"
            result
        } catch (e: Exception) {
            lastError = e.toString()
            emptyList()
        }
    }
}
