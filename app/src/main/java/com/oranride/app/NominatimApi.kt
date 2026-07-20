package com.oranride.app

import com.squareup.moshi.Json
import retrofit2.http.GET
import retrofit2.http.Headers
import retrofit2.http.Query

data class NominatimPlace(
    @Json(name = "display_name")
    val displayName: String,

    @Json(name = "lat")
    val lat: String,

    @Json(name = "lon")
    val lon: String
)

interface NominatimApi {

    @Headers(
    "User-Agent: OranRide/1.0",
    "Accept: application/json"
)
    @GET("search")
    suspend fun search(
        @Query("q") query: String,
        @Query("format") format: String = "jsonv2",
        @Query("limit") limit: Int = 10,
        @Query("addressdetails") addressDetails: Int = 1,
    ): List<NominatimPlace>
}
