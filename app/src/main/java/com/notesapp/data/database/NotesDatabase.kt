package com.notesapp.data.database

import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import androidx.room.migration.Migration
import android.content.Context

/**
 * Room database class untuk aplikasi Notes
 * Singleton database yang menyediakan akses ke NoteDao
 */
@Database(
    entities = [NoteEntity::class],
    version = 1,
    exportSchema = true
)
abstract class NotesDatabase : RoomDatabase() {
    
    /**
     * Mendapatkan DAO untuk operasi database notes
     */
    abstract fun notesDao(): NotesDao
    
    companion object {
        @Volatile
        private var INSTANCE: NotesDatabase? = null
        
        /**
         * Get singleton instance dari database
         */
        fun getDatabase(context: Context): NotesDatabase {
            return INSTANCE ?: synchronized(this) {
                val instance = Room.databaseBuilder(
                    context.applicationContext,
                    NotesDatabase::class.java,
                    "notes_database"
                )
                    .fallbackToDestructiveMigration() // For development - remove in production
                    .build()
                INSTANCE = instance
                instance
            }
        }
    }
}