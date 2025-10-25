package com.notesapp.di

import com.notesapp.data.repository.NotesRepositoryImpl
import com.notesapp.domain.repository.NotesRepository
import dagger.Binds
import dagger.Module
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

/**
 * Hilt module untuk repository dependencies
 * Binds implementation ke interface
 */
@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {
    
    /**
     * Bind NotesRepositoryImpl ke NotesRepository interface
     */
    @Binds
    @Singleton
    abstract fun bindNotesRepository(
        notesRepositoryImpl: NotesRepositoryImpl
    ): NotesRepository
}