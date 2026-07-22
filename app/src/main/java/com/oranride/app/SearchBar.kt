
package com.oranride.app

import androidx.compose.runtime.*
import androidx.compose.material3.*
import androidx.compose.ui.Modifier

@Composable
fun SearchBar(
    onSearch: (String) -> Unit
) {
    var text by remember { mutableStateOf("") }

    OutlinedTextField(
        value = text,
        onValueChange = { text = it },
        modifier = Modifier,
        label = { Text("ابحث عن مكان") },
        singleLine = true
    )
}
