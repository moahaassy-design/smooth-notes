package com.notesapp

import android.app.Application
import dagger.hilt.android.HiltAndroidApp

/**
 * Main Application class untuk inisialisasi Hilt
 * Wajib ada untuk dependency injection dengan Hilt
 */
@HiltAndroidApp
class NotesApplication : Application() {
    
    override fun onCreate() {
        super.onCreate()
        
        // Inisialisasi aplikasi
        // Setup configurations, logging, etc.
    }
}
