
package com.example.ui

import android.content.Context
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.viewinterop.AndroidView
import org.osmdroid.config.Configuration
import org.osmdroid.tileprovider.tilesource.TileSourceFactory
import org.osmdroid.util.GeoPoint
import org.osmdroid.views.MapView
import org.osmdroid.views.overlay.Polyline
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import com.example.data.RetrofitClient

@Composable
fun RealMap(
    modifier: Modifier = Modifier,
    targetLat: Double? = null,
    targetLon: Double? = null,
    riderLat: Double? = null,
    riderLon: Double? = null
) {
    AndroidView(
        modifier = modifier,
        factory = { context: Context ->

            Configuration.getInstance().userAgentValue = context.packageName

            MapView(context).apply {
                setTileSource(TileSourceFactory.MAPNIK)
                setMultiTouchControls(true)

                controller.setZoom(13.5)

                if (riderLat != null && riderLon != null &&
                    targetLat != null && targetLon != null) {

                    CoroutineScope(Dispatchers.IO).launch {
                        try {
                            val coords = "${riderLon},${riderLat};${targetLon},${targetLat}"

                            val route = RetrofitClient.routeApi.getRoute(coords)

                            val points = route.routes[0].geometry.coordinates.map {
                                GeoPoint(it[1], it[0])
                            }

                            val line = Polyline().apply {
                                setPoints(points)
                                width = 8f
                            }

                            post {
                                overlays.add(line)
                                invalidate()
                            }

                        } catch (e: Exception) {
                            e.printStackTrace()
                        }
                    }
                }

                if (targetLat != null && targetLon != null) {
                    controller.animateTo(
                        GeoPoint(targetLat, targetLon)
                    )
                } else {
                    controller.setCenter(
                        GeoPoint(35.6971, -0.6308)
                    )
                }
            }
        }
    )
}
// Sidox generated code
// Task: أضف زر البحث في الصفحة الرئيسية
