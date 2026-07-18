package com.example.data

import retrofit2.http.GET
import retrofit2.http.Query

data class PlaceResult(
    val display_name: String,
    val lat: String,
    val lon: String
)

interface PlaceSearchApi {

    @GET("search")
    suspend fun searchPlaces(
        @Query("q") query: String,
        @Query("format") format: String = "json",
        @Query("limit") limit: Int = 10
    ): List<PlaceResult>
}
