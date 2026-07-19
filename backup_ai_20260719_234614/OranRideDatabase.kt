package com.example.data

import androidx.room.*
import kotlinx.coroutines.flow.Flow

@Entity(tableName = "users")
data class UserEntity(
    @PrimaryKey val id: String,
    val name: String,
    val phone: String,
    val role: String, // "rider" or "driver"
    val vehicleInfo: String? = null, // e.g. "Dacia Logan - Black (31-102-45)"
    val isOnline: Boolean = false,
    val rating: Float = 5.0f,
    val walletBalance: Double = 0.0
)

@Entity(tableName = "rides")
data class RideEntity(
    @PrimaryKey val id: String,
    val riderId: String,
    val riderName: String,
    val driverId: String? = null,
    val driverName: String? = null,
    val driverVehicle: String? = null,
    val pickupName: String,
    val pickupLat: Float,
    val pickupLng: Float,
    val destinationName: String,
    val destinationLat: Float,
    val destinationLng: Float,
    val status: String, // "searching", "accepted", "arriving", "arrived", "inprogress", "completed", "cancelled"
    val fare: Double, // in DZD (Algerian Dinar)
    val distanceKm: Float,
    val timestamp: Long = System.currentTimeMillis(),
    val ratingGiven: Float? = null
)

@Dao
interface UserDao {
    @Query("SELECT * FROM users WHERE id = :id LIMIT 1")
    suspend fun getUserById(id: String): UserEntity?

    @Query("SELECT * FROM users WHERE role = 'driver' AND isOnline = 1")
    fun getOnlineDrivers(): Flow<List<UserEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertUser(user: UserEntity)

    @Update
    suspend fun updateUser(user: UserEntity)

    @Query("DELETE FROM users WHERE id = :id")
    suspend fun deleteUserById(id: String)
}

@Dao
interface RideDao {
    @Query("SELECT * FROM rides ORDER BY timestamp DESC")
    fun getAllRides(): Flow<List<RideEntity>>

    @Query("SELECT * FROM rides WHERE id = :id LIMIT 1")
    suspend fun getRideById(id: String): RideEntity?

    @Query("SELECT * FROM rides WHERE riderId = :riderId ORDER BY timestamp DESC")
    fun getRidesForRider(riderId: String): Flow<List<RideEntity>>

    @Query("SELECT * FROM rides WHERE driverId = :driverId ORDER BY timestamp DESC")
    fun getRidesForDriver(driverId: String): Flow<List<RideEntity>>

    @Query("SELECT * FROM rides WHERE status = 'searching' ORDER BY timestamp DESC")
    fun getActiveRequests(): Flow<List<RideEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertRide(ride: RideEntity)

    @Update
    suspend fun updateRide(ride: RideEntity)

    @Query("DELETE FROM rides")
    suspend fun clearAllRides()
}

@Database(entities = [UserEntity::class, RideEntity::class], version = 1, exportSchema = false)
abstract class OranRideDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
    abstract fun rideDao(): RideDao
}
