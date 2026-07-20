package com.oranride.app

import retrofit2.http.GET
import retrofit2.http.Query

data class NominatimPlace(
    val display_name: String,
    val lat: String,
    val lon: String
)

interface NominatimApi {

    @GET("search")
    suspend fun search(
        @Query("q") query: String,
        @Query("format") format: String = "jsonv2",
        @Query("limit") limit: Int = 10,
        @Query("addressdetails") addressDetails: Int = 1,
        @Query("countrycodes") countryCodes: String = "dz",
        @Query("accept-language") language: String = "ar"
    ): List<NominatimPlace>
}
