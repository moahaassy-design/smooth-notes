package com.notesapp.data.database

import androidx.room.Entity
import androidx.room.PrimaryKey
import androidx.room.ColumnInfo

/**
 * Entity untuk tabel notes dalam database Room
 * Menyimpan data catatan dengan fields: id, title, content, timestamp, dan color
 */
@Entity(tableName = "notes")
data class NoteEntity(
    
    @PrimaryKey(autoGenerate = true)
    @ColumnInfo(name = "id")
    val id: Long = 0,
    
    @ColumnInfo(name = "title")
    val title: String,
    
    @ColumnInfo(name = "content")
    val content: String,
    
    @ColumnInfo(name = "timestamp")
    val timestamp: Long,
    
    @ColumnInfo(name = "color")
    val color: Int
)