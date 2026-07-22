
package com.oranride.app

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

class NominatimRepository {

    suspend fun search(query: String): List<String> {
        return withContext(Dispatchers.IO) {
            listOf(query)
        }
    }
}
