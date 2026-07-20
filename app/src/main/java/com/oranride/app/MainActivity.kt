package com.oranride.app

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import org.osmdroid.config.Configuration
import org.osmdroid.views.MapView

class MainActivity : AppCompatActivity() {

    private lateinit var map: MapView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        Configuration.getInstance().userAgentValue = packageName

        map = MapView(this)
        map.setMultiTouchControls(true)

        map.controller.setZoom(14.0)
        map.controller.setCenter(
            org.osmdroid.util.GeoPoint(35.6969, -0.6331)
        )

        setContentView(map)
    }

    override fun onResume() {
        super.onResume()
        map.onResume()
    }

    override fun onPause() {
        super.onPause()
        map.onPause()
    }
}
