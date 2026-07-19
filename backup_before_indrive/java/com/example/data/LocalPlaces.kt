package com.example.data

data class LocalPlace(
    val name: String,
    val lat: Double,
    val lon: Double,
    val category: String
)

val oranPlaces = listOf(
    LocalPlace("Place d'Armes - ساحة أول نوفمبر", 35.6971, -0.6333, "landmark"),
    LocalPlace("Gare d'Oran - محطة القطار", 35.7047, -0.6507, "station"),
    LocalPlace("Aéroport Ahmed Ben Bella", 35.6239, -0.6212, "airport"),
    LocalPlace("Université d'Oran", 35.6998, -0.6315, "university"),
    LocalPlace("CHU Oran - المستشفى الجامعي", 35.7085, -0.6360, "hospital"),
    LocalPlace("Es Senia - السانية", 35.6547, -0.6238, "area"),
    LocalPlace("Akid Lotfi", 35.7205, -0.5900, "area")
)
