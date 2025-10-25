package com.notesapp

import android.app.Application
import dagger.hilt.android.HiltAndroidApp

/**
 * Application class untuk Smooth Notes App
 * Setup Hilt dependency injection dan database initialization
 */
@HiltAndroidApp
class SmoothNotesApplication : Application() {
    
    override fun onCreate() {
        super.onCreate()
        
        // Setup any app-wide configurations here
        initializeApp()
    }
    
    private fun initializeApp() {
        // Initialize app-wide configurations
        // Example: Analytics, crashlytics, etc.
    }
}