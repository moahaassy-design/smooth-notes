package com.notesapp.data.database

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import androidx.room.Delete
import kotlinx.coroutines.flow.Flow

/**
 * DAO interface untuk operasi database notes
 * Menyediakan CRUD operations dan queries untuk Room database
 */
@Dao
interface NotesDao {
    
    /**
     * Ambil semua catatan dari database dalam bentuk Flow untuk reactive updates
     */
    @Query("SELECT * FROM notes ORDER BY timestamp DESC")
    fun getAllNotes(): Flow<List<NoteEntity>>
    
    /**
     * Ambil catatan berdasarkan ID
     */
    @Query("SELECT * FROM notes WHERE id = :noteId")
    suspend fun getNoteById(noteId: Long): NoteEntity?
    
    /**
     * Cari catatan berdasarkan query di title atau content
     */
    @Query("SELECT * FROM notes WHERE title LIKE '%' || :query || '%' OR content LIKE '%' || :query || '%' ORDER BY timestamp DESC")
    fun searchNotes(query: String): Flow<List<NoteEntity>>
    
    /**
     * Hitung total jumlah catatan
     */
    @Query("SELECT COUNT(*) FROM notes")
    suspend fun getNotesCount(): Int
    
    /**
     * Tambah catatan baru
     */
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertNote(note: NoteEntity): Long
    
    /**
     * Update catatan existing
     */
    @Update
    suspend fun updateNote(note: NoteEntity)
    
    /**
     * Hapus catatan
     */
    @Delete
    suspend fun deleteNote(note: NoteEntity)
    
    /**
     * Hapus catatan berdasarkan ID
     */
    @Query("DELETE FROM notes WHERE id = :noteId")
    suspend fun deleteNoteById(noteId: Long)
}