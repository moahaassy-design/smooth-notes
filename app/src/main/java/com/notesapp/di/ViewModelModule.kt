package com.notesapp.di

import dagger.Module
import dagger.hilt.InstallIn
import dagger.hilt.android.components.ViewModelComponent

/**
 * Hilt module untuk ViewModel dependencies
 * Installed in ViewModelComponent untuk ViewModel lifecycle
 */
@Module
@InstallIn(ViewModelComponent::class)
object ViewModelModule {
    // ViewModels will be provided through @HiltViewModel annotation
    // This module can be extended for additional ViewModel dependencies
}