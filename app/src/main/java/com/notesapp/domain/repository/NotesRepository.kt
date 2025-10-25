package com.notesapp.domain.repository

import com.notesapp.domain.model.Note
import kotlinx.coroutines.flow.Flow

/**
 * Repository interface untuk operations pada notes
 * Menentukan contract untuk data layer implementation
 */
interface NotesRepository {
    
    /**
     * Get semua notes dari database dalam bentuk Flow
     */
    fun getAllNotes(): Flow<List<Note>>
    
    /**
     * Get note berdasarkan ID
     */
    suspend fun getNoteById(id: Long): Note?
    
    /**
     * Search notes berdasarkan query
     */
    fun searchNotes(query: String): Flow<List<Note>>
    
    /**
     * Insert note baru
     */
    suspend fun insertNote(note: Note): Long
    
    /**
     * Update note existing
     */
    suspend fun updateNote(note: Note)
    
    /**
     * Delete note
     */
    suspend fun deleteNote(note: Note)
    
    /**
     * Get jumlah total notes
     */
    suspend fun getNotesCount(): Int
}