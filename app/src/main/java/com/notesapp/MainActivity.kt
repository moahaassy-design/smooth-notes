package com.notesapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.runtime.remember
import androidx.navigation.compose.rememberNavController
import com.notesapp.presentation.navigation.AppNavigation
import com.notesapp.presentation.theme.NotesAppTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        setContent {
            // Use dynamic Material You colors by default
            val darkTheme = isSystemInDarkTheme()
            
            NotesAppTheme(
                darkTheme = darkTheme,
                dynamicColor = true // Enable Material You dynamic colors on Android 12+
            ) {
                val navController = rememberNavController()
                
                AppNavigation(navController = navController)
            }
        }
    }
}