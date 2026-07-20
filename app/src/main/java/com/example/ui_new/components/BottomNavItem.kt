package com.example.ui_new.components

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AccountBalanceWallet
import androidx.compose.material.icons.filled.DirectionsCar
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Person
import androidx.compose.ui.graphics.vector.ImageVector

data class BottomNavItem(
    val route: String,
    val title: String,
    val icon: ImageVector
)

val BottomNavItems = listOf(
    BottomNavItem(
        route = "home",
        title = "الرئيسية",
        icon = Icons.Default.Home
    ),
    BottomNavItem(
        route = "trips",
        title = "الرحلات",
        icon = Icons.Default.DirectionsCar
    ),
    BottomNavItem(
        route = "wallet",
        title = "المحفظة",
        icon = Icons.Default.AccountBalanceWallet
    ),
    BottomNavItem(
        route = "profile",
        title = "الحساب",
        icon = Icons.Default.Person
    )
)
