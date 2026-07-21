# Project Brain


## MainActivity.kt
Classes:
- MainActivity
Functions:
- onCreate

## LocationHelper.kt
Classes:
- LocationHelper
Functions:
- start
- onLocationResult

## OranMap.kt
Classes:
- OranLandmark
Composable:
- OranMap
Functions:
- getPixelX
- getPixelY

## OranRideViewModel.kt
Classes:
- OranRideViewModel
Functions:
- startRiderLocation
- loadHistory
- setScreen
- register
- selectProfile
- setDriverOnline
- logout
- getEstimatedFare
- getEstimatedDistance
- getDistanceKm
- requestRide
- cancelActiveRide
- startRiderSimulation
- rateRide
- simulateRiderRequestForDriver

## RealMap.kt
Composable:
- RealMap

## Screens.kt
Composable:
- OranRideAppContent
- ModeSelectScreen
- RegisterScreen
- RiderHomeScreen
- LandmarkSelectorDialog
- RiderTrackingScreen
- DriverHomeScreen
- DriverNavScreen
- HistoryScreen
- Icon

## Color.kt

## Theme.kt
Composable:
- MyApplicationTheme

## Type.kt

## LocalPlaces.kt
Classes:
- LocalPlace

## OranRideDatabase.kt
Classes:
- UserEntity
- RideEntity
- OranRideDatabase
Functions:
- getUserById
- getOnlineDrivers
- insertUser
- updateUser
- deleteUserById
- getAllRides
- getRideById
- getRidesForRider
- getRidesForDriver
- getActiveRequests
- insertRide
- updateRide
- clearAllRides
- userDao
- rideDao

## OranRideRepository.kt
Classes:
- OranRideRepository
Functions:
- registerUser
- selectUserProfile
- toggleDriverOnline
- logout
- requestRide
- cancelActiveRide
- acceptRideRequest
- updateRideStatus
- rateRide
- observeActiveRide
- getActiveRequests
- getRideHistory
- insertMockDrivers

## PlaceSearch.kt
Classes:
- PlaceResult
Functions:
- searchPlaces

## RetrofitClient.kt

## RouteService.kt
Classes:
- OsrmResponse
- OsrmRoute
- OsrmGeometry
Functions:
- getRoute