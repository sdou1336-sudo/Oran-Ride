package com.oranride.app

import retrofit2.Retrofit
import retrofit2.converter.moshi.MoshiConverterFactory

object NominatimClient {

    val api: NominatimApi by lazy {
        Retrofit.Builder()
            .baseUrl("https://nominatim.openstreetmap.org/")
            .addConverterFactory(MoshiConverterFactory.create())
            .build()
            .create(NominatimApi::class.java)
    }
}
