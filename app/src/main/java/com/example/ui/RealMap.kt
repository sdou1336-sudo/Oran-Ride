package com.example.ui

import android.content.Context
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.viewinterop.AndroidView
import org.osmdroid.config.Configuration
import org.osmdroid.tileprovider.tilesource.TileSourceFactory
import org.osmdroid.util.GeoPoint
import org.osmdroid.views.MapView

@Composable
fun RealMap(
    modifier: Modifier = Modifier,
    targetLat: Double? = null,
    targetLon: Double? = null
) {
    AndroidView(
        modifier = modifier,
        factory = { context: Context ->

            Configuration.getInstance().userAgentValue = context.packageName

            MapView(context).apply {
                setTileSource(TileSourceFactory.MAPNIK)
                setMultiTouchControls(true)

                controller.setZoom(13.5)

                    GeoPoint(35.6971, -0.6308)
)if (targetLat != null && targetLon != null) {
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
