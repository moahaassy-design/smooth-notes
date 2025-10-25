package com.notesapp.data.repository

import com.notesapp.data.database.NoteEntity
import com.notesapp.data.database.NotesDao
import com.notesapp.domain.model.Note
import com.notesapp.domain.repository.NotesRepository
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map
import javax.inject.Inject
import javax.inject.Singleton

/**
 * Implementation dari NotesRepository
 * Menggunakan NotesDao untuk akses database dan mapper untuk konversi data
 */
@Singleton
class NotesRepositoryImpl @Inject constructor(
    private val notesDao: NotesDao
) : NotesRepository {
    
    override fun getAllNotes(): Flow<List<Note>> {
        return notesDao.getAllNotes().map { entities ->
            entities.map { it.toDomain() }
        }
    }
    
    override suspend fun getNoteById(id: Long): Note? {
        return notesDao.getNoteById(id)?.toDomain()
    }
    
    override fun searchNotes(query: String): Flow<List<Note>> {
        return notesDao.searchNotes(query).map { entities ->
            entities.map { it.toDomain() }
        }
    }
    
    override suspend fun insertNote(note: Note): Long {
        return notesDao.insertNote(note.toEntity())
    }
    
    override suspend fun updateNote(note: Note) {
        notesDao.updateNote(note.toEntity())
    }
    
    override suspend fun deleteNote(note: Note) {
        notesDao.deleteNote(note.toEntity())
    }
    
    override suspend fun getNotesCount(): Int {
        return notesDao.getNotesCount()
    }
    
    /**
     * Extension function untuk konversi NoteEntity ke Note
     */
    private fun NoteEntity.toDomain(): Note {
        return Note(
            id = id,
            title = title,
            content = content,
            timestamp = timestamp,
            color = color
        )
    }
    
    /**
     * Extension function untuk konversi Note ke NoteEntity
     */
    private fun Note.toEntity(): NoteEntity {
        return NoteEntity(
            id = id,
            title = title,
            content = content,
            timestamp = timestamp,
            color = color
        )
    }
}