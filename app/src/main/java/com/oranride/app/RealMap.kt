
package com.oranride.app

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.ui.viewinterop.AndroidView
import org.osmdroid.views.MapView
import org.osmdroid.util.GeoPoint

@Composable
fun RealMap() {
    AndroidView(
        modifier = Modifier.fillMaxSize(),
        factory = { context ->
            MapView(context).apply {
                setMultiTouchControls(true)
                controller.setZoom(14.0)
                controller.setCenter(
                    GeoPoint(35.6971, -0.6308)
                )
            }
        }
    )
}
