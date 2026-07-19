package com.example.data

import okhttp3.OkHttpClient
import okhttp3.Request
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitClient {

    val routeApi: RouteService by lazy {
        Retrofit.Builder()
            .baseUrl("https://router.project-osrm.org/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(RouteService::class.java)
    }

    private const val BASE_URL = "https://nominatim.openstreetmap.org/"

    private val client = OkHttpClient.Builder()
        .addInterceptor { chain ->
            val request: Request = chain.request().newBuilder()
                .header("User-Agent", "OranRider/1.0 (Android)")
                .header("Accept-Language", "ar,en")
                .build()
            chain.proceed(request)
        }
        .build()

    val api: PlaceSearchApi by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .client(client)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(PlaceSearchApi::class.java)
    }
}
