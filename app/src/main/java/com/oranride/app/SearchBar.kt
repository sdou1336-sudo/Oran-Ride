package com.oranride.app

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalSoftwareKeyboardController
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.unit.dp
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
@Composable
fun SearchBar(
    onPlaceSelected: (Double, Double) -> Unit
) {

    var query by remember { mutableStateOf("") }
    var results by remember { mutableStateOf(listOf<NominatimPlace>()) }

    LaunchedEffect(query) {
    if (query.length >= 3) {
        results = withContext(Dispatchers.IO) {
            NominatimRepository.search(query)
        }
    } else {
        results = emptyList()
    }
}

val keyboardController = LocalSoftwareKeyboardController.current

    Surface(
        modifier = Modifier
            .fillMaxWidth()
            .padding(12.dp),
        shadowElevation = 8.dp,
        tonalElevation = 4.dp
    ) {

        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(8.dp)
        ) {

            OutlinedTextField(
                value = query,
                onValueChange = {
    query = it
},
                modifier = Modifier.fillMaxWidth(),

                label = {
                    Text("أين تريد الذهاب؟")
                },

                singleLine = true,

                keyboardOptions = KeyboardOptions(
                    imeAction = ImeAction.Search
                ),

                keyboardActions = KeyboardActions(
                    onSearch = {

                        keyboardController?.hide()
                    }
                )
            )


            if (results.isNotEmpty()) {

                Spacer(
                    modifier = Modifier.height(8.dp)
                )

                LazyColumn(
                    modifier = Modifier
                        .fillMaxWidth()
                        .heightIn(max = 300.dp)
                ) {

                    items(results) { place ->

                        Card(
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(vertical = 4.dp)
                                .clickable {

                                    onPlaceSelected(
    place.lat.toDouble(),
    place.lon.toDouble()
)

results = emptyList()
query = ""
keyboardController?.hide()
                                }
                        ) {

                            Text(
                                text = place.display_name,
                                modifier = Modifier.padding(16.dp)
                            )
                        }
                    }
                }
            }
        }
    }
}
