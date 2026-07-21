package com.example.ui

import androidx.compose.animation.core.*
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.LocationOn
import androidx.compose.material.icons.filled.Navigation
import androidx.compose.material.icons.filled.Place
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.StrokeCap
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.drawText
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.rememberTextMeasurer
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlin.math.atan2
import kotlin.math.cos
import kotlin.math.sin

data class OranLandmark(
    val id: String,
    val name: String,
    val gridX: Float, // 0 to 100
    val gridY: Float, // 0 to 100
    val description: String
)

val oranLandmarks = listOf(
    OranLandmark("santa_cruz", "Fort Santa Cruz (قلعة سانتا كروز)", 15f, 25f, "Ottoman-Spanish fort on Mt. Murdjadjo"),
    OranLandmark("front_de_mer", "Front de Mer (واجهة البحر)", 60f, 15f, "Scenic waterfront boulevard"),
    OranLandmark("place_1er_nov", "Place 1er Novembre (ساحة أول نوفمبر)", 45f, 35f, "Historic downtown plaza"),
    OranLandmark("cathedral", "Cathedral of Oran (كاتدرائية وهران)", 50f, 48f, "Historic Cathedral of Sacré-Cœur"),
    OranLandmark("meridien", "Le Méridien Hotel (الفندق الجديد)", 85f, 22f, "Modern coastal convention area"),
    OranLandmark("usto", "University USTO (جامعة إيسطو)", 80f, 55f, "University of Science & Technology"),
    OranLandmark("airport", "Airport Es-Senia (مطار السانية)", 40f, 85f, "Oran Ahmed Ben Bella Airport")
)

// Main interactive Canvas Map of Oran
@Composable
fun OranMap(
    modifier: Modifier = Modifier,
    pickupLandmarkId: String? = null,
    destinationLandmarkId: String? = null,
    driverGridX: Float? = null,
    driverGridY: Float? = null,
    onLandmarkSelected: ((OranLandmark) -> Unit)? = null
) {
    val textMeasurer = rememberTextMeasurer()
    
    // Theme Colors
    val isDarkTheme = true // Dark premium theme feels high-tech and sleek for ride apps
    val backgroundColor = if (isDarkTheme) Color(0xFF12141C) else Color(0xFFF6F8FC)
    val roadColor = if (isDarkTheme) Color(0xFF262D3D) else Color(0xFFE2E8F0)
    val gridLineColor = if (isDarkTheme) Color(0xFF1E2330) else Color(0xFFEDF2F7)
    val primaryAccent = Color(0xFFFFC107) // Vibrant Algerian Taxi Yellow
    val secondaryAccent = Color(0xFF00C853) // Green of Algerian Flag
    val textOnMapColor = if (isDarkTheme) Color(0xFF8E9BAE) else Color(0xFF64748B)

    // Infinitely pulsating circle for active route indicators
    val infiniteTransition = rememberInfiniteTransition(label = "map_waves")
    val pulseScale by infiniteTransition.animateFloat(
        initialValue = 10f,
        targetValue = 28f,
        animationSpec = infiniteRepeatable(
            animation = tween(1500, easing = LinearEasing),
            repeatMode = RepeatMode.Restart
        ),
        label = "pulse"
    )
    val pulseAlpha by infiniteTransition.animateFloat(
        initialValue = 0.6f,
        targetValue = 0f,
        animationSpec = infiniteRepeatable(
            animation = tween(1500, easing = LinearEasing),
            repeatMode = RepeatMode.Restart
        ),
        label = "pulse_alpha"
    )

    Box(
        modifier = modifier
            .fillMaxSize()
            .background(backgroundColor)
            .clip(RoundedCornerShape(16.dp))
    ) {
        Canvas(
            modifier = Modifier
                .fillMaxSize()
                .pointerInput(Unit) {
                    detectTapGestures { offset ->
                        // Reverse engineer grid coords from raw pixels to check tap hits
                        val width = size.width.toFloat()
                        val height = size.height.toFloat()
                        if (width > 0 && height > 0) {
                            oranLandmarks.forEach { landmark ->
                                val lx = (landmark.gridX / 100f) * width
                                val ly = (landmark.gridY / 100f) * height
                                val distance = Math.hypot((offset.x - lx).toDouble(), (offset.y - ly).toDouble())
                                if (distance < 50.dp.toPx() && onLandmarkSelected != null) {
                                    onLandmarkSelected(landmark)
                                }
                            }
                        }
                    }
                }
        ) {
            val width = size.width
            val height = size.height

            // 1. Draw Subtle Grid Pattern
            val gridSpacing = 60.dp.toPx()
            var x = 0f
            while (x < width) {
                drawLine(gridLineColor, Offset(x, 0f), Offset(x, height), strokeWidth = 1f)
                x += gridSpacing
            }
            var y = 0f
            while (y < height) {
                drawLine(gridLineColor, Offset(0f, y), Offset(width, y), strokeWidth = 1f)
                y += gridSpacing
            }

            // Helpers to convert normalized 0-100 coordinates to actual canvas pixels
            fun getPixelX(gridX: Float): Float = (gridX / 100f) * width
            fun getPixelY(gridY: Float): Float = (gridY / 100f) * height

            // 2. Draw Simulated Sea / Mediterranean Coast (Top left / top edge of Oran)
            val seaPath = Path().apply {
                moveTo(0f, 0f)
                lineTo(width, 0f)
                quadraticTo(width * 0.75f, height * 0.08f, width * 0.5f, height * 0.12f)
                quadraticTo(width * 0.25f, height * 0.05f, 0f, height * 0.22f)
                close()
            }
            drawPath(
                path = seaPath,
                brush = Brush.verticalGradient(
                    colors = listOf(
                        Color(0xFF1E3A8A).copy(alpha = 0.35f),
                        Color(0xFF3B82F6).copy(alpha = 0.05f)
                    )
                )
            )

            // Draw Coastal label (Mediterranean Sea)
            drawText(
                textMeasurer = textMeasurer,
                text = "MEDITERRANEAN SEA (البحر الأبيض المتوسط)",
                topLeft = Offset(width * 0.25f, height * 0.03f),
                style = TextStyle(
                    color = Color(0xFF3B82F6).copy(alpha = 0.4f),
                    fontSize = 11.sp,
                    fontWeight = FontWeight.Bold
                )
            )

            // 3. Draw Road Network (As beautiful interconnected bezier curves)
            val roads = listOf(
                // Coast highway: Santa Cruz -> Place 1er Nov -> Front de Mer -> Meridien
                listOf("santa_cruz", "place_1er_nov", "front_de_mer", "meridien"),
                // Airport Highway: Airport -> Cathedral -> Place 1er Nov
                listOf("airport", "cathedral", "place_1er_nov"),
                // Southern Rocade: Airport -> USTO -> Meridien
                listOf("airport", "usto", "meridien"),
                // Local Connectors
                listOf("cathedral", "usto")
            )

            roads.forEach { roadList ->
                val roadPath = Path().apply {
                    val first = oranLandmarks.firstOrNull { it.id == roadList[0] }
                    if (first != null) {
                        moveTo(getPixelX(first.gridX), getPixelY(first.gridY))
                        for (i in 1 until roadList.size) {
                            val next = oranLandmarks.firstOrNull { it.id == roadList[i] }
                            if (next != null) {
                                lineTo(getPixelX(next.gridX), getPixelY(next.gridY))
                            }
                        }
                    }
                }
                // Underline/Outer glow for roads
                drawPath(roadPath, roadColor, style = Stroke(width = 6.dp.toPx(), cap = StrokeCap.Round))
                drawPath(roadPath, backgroundColor, style = Stroke(width = 2.dp.toPx(), cap = StrokeCap.Round))
            }

            // 4. Draw Highlighted Route if Pickup and Destination are selected
            val pId = pickupLandmarkId
            val dId = destinationLandmarkId
            if (pId != null && dId != null) {
                val p = oranLandmarks.firstOrNull { it.id == pId }
                val d = oranLandmarks.firstOrNull { it.id == dId }
                if (p != null && d != null) {
                    val routePath = Path().apply {
                        moveTo(getPixelX(p.gridX), getPixelY(p.gridY))
                        // Draw path (with a subtle curved bypass to look realistic)
                        val midX = (p.gridX + d.gridX) / 2
                        val midY = (p.gridY + d.gridY) / 2 - 4f // curve upwards slightly
                        quadraticTo(getPixelX(midX), getPixelY(midY), getPixelX(d.gridX), getPixelY(d.gridY))
                    }
                    // Outer glow for the route
                    drawPath(
                        path = routePath,
                        color = primaryAccent.copy(alpha = 0.3f),
                        style = Stroke(width = 10.dp.toPx(), cap = StrokeCap.Round)
                    )
                    // Core active route line
                    drawPath(
                        path = routePath,
                        color = primaryAccent,
                        style = Stroke(width = 4.dp.toPx(), cap = StrokeCap.Round)
                    )
                }
            }

            // 5. Draw Landmark Markers
            oranLandmarks.forEach { landmark ->
                val px = getPixelX(landmark.gridX)
                val py = getPixelY(landmark.gridY)
                val isPickup = landmark.id == pickupLandmarkId
                val isDest = landmark.id == destinationLandmarkId

                // Draw highlighted effects
                if (isPickup) {
                    drawCircle(secondaryAccent.copy(alpha = pulseAlpha), radius = pulseScale.dp.toPx(), center = Offset(px, py))
                    drawCircle(secondaryAccent, radius = 6.dp.toPx(), center = Offset(px, py))
                } else if (isDest) {
                    drawCircle(Color.Red.copy(alpha = pulseAlpha), radius = pulseScale.dp.toPx(), center = Offset(px, py))
                    drawCircle(Color.Red, radius = 6.dp.toPx(), center = Offset(px, py))
                } else {
                    // Regular landmark marker
                    drawCircle(
                        color = if (isDarkTheme) Color(0xFF2E3B52) else Color(0xFFCBD5E1),
                        radius = 4.dp.toPx(),
                        center = Offset(px, py)
                    )
                }

                // Landmark Labels
                val isSelected = isPickup || isDest
                val nameLines = landmark.name.split(" ")
                val shortName = nameLines.firstOrNull() ?: landmark.name
                
                drawText(
                    textMeasurer = textMeasurer,
                    text = shortName,
                    topLeft = Offset(px - 25.dp.toPx(), py + 8.dp.toPx()),
                    style = TextStyle(
                        color = if (isSelected) {
                            if (isPickup) secondaryAccent else Color.Red
                        } else textOnMapColor,
                        fontSize = if (isSelected) 11.sp else 9.sp,
                        fontWeight = if (isSelected) FontWeight.ExtraBold else FontWeight.SemiBold
                    )
                )
            }

            // 6. Draw Live Moving Driver (Simulated Car)
            if (driverGridX != null && driverGridY != null) {
                val cx = getPixelX(driverGridX)
                val cy = getPixelY(driverGridY)

                // Outer neon pulsing aura
                drawCircle(
                    color = primaryAccent.copy(alpha = 0.35f),
                    radius = 16.dp.toPx(),
                    center = Offset(cx, cy)
                )

                // Vehicle outline circle
                drawCircle(
                    color = if (isDarkTheme) Color(0xFF1E1E2C) else Color.White,
                    radius = 10.dp.toPx(),
                    center = Offset(cx, cy),
                    style = Stroke(width = 2.dp.toPx())
                )

                // Vehicle inner color (Yellow cab theme)
                drawCircle(
                    color = primaryAccent,
                    radius = 8.dp.toPx(),
                    center = Offset(cx, cy)
                )

                // Dynamic car symbol center
                drawCircle(
                    color = Color.Black,
                    radius = 3.dp.toPx(),
                    center = Offset(cx, cy)
                )
            }
        }

        // Overlay Legend / Info
        Card(
            modifier = Modifier
                .align(Alignment.TopEnd)
                .padding(12.dp),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.85f)
            ),
            shape = RoundedCornerShape(8.dp)
        ) {
            Column(
                modifier = Modifier.padding(8.dp),
                verticalArrangement = Arrangement.spacedBy(4.dp)
            ) {
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(6.dp)
                ) {
                    Box(modifier = Modifier.size(8.dp).background(secondaryAccent, CircleShape))
                    Text("Pickup (الإنطلاق)", fontSize = 10.sp, fontWeight = FontWeight.Bold)
                }
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(6.dp)
                ) {
                    Box(modifier = Modifier.size(8.dp).background(Color.Red, CircleShape))
                    Text("Dropoff (الوصول)", fontSize = 10.sp, fontWeight = FontWeight.Bold)
                }
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(6.dp)
                ) {
                    Box(modifier = Modifier.size(8.dp).background(primaryAccent, CircleShape))
                    Text("Taxi (السائق)", fontSize = 10.sp, fontWeight = FontWeight.Bold)
                }
            }
        }
    }
}


// تحسين الخريطة
// تحسينات الخريطة القادمة: Marker + Camera + Route

// Driver Marker Enhancement
// تحسين مؤشر السائق
// سيتم ربطه لاحقاً بالحركة الحية والاتجاه

// Driver Marker Enhancement
// تحسين مؤشر السائق
// سيتم ربطه لاحقاً بالحركة الحية والاتجاه
