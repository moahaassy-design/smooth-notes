package com.notesapp.di

import android.content.Context
import androidx.room.Room
import com.notesapp.data.database.NotesDatabase
import com.notesapp.data.database.NotesDao
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.android.qualifiers.ApplicationContext
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

/**
 * Hilt module untuk database dependencies
 * Provides database instance dan DAO
 */
@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {
    
    /**
     * Provide NotesDatabase instance
     */
    @Provides
    @Singleton
    fun provideNotesDatabase(
        @ApplicationContext context: Context
    ): NotesDatabase {
        return Room.databaseBuilder(
            context.applicationContext,
            NotesDatabase::class.java,
            "notes_database"
        )
            .fallbackToDestructiveMigration()
            .build()
    }
    
    /**
     * Provide NotesDao instance
     */
    @Provides
    fun provideNotesDao(database: NotesDatabase): NotesDao {
        return database.notesDao()
    }
}