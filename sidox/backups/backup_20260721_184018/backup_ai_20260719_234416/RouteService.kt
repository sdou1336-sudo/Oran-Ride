
package com.example.data

import retrofit2.http.GET
import retrofit2.http.Path

data class OsrmResponse(
    val routes: List<OsrmRoute>
)

data class OsrmRoute(
    val geometry: OsrmGeometry
)

data class OsrmGeometry(
    val coordinates: List<List<Double>>
)

interface RouteService {

    @GET("route/v1/driving/{coords}")
    suspend fun getRoute(
        @Path("coords", encoded = true) coords: String
    ): OsrmResponse
}
