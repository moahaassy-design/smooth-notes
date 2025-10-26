package com.notesapp.presentation.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.notesapp.domain.model.Note
import com.notesapp.domain.repository.NotesRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import java.util.*
import javax.inject.Inject

/**
 * AddEditNoteViewModel - ViewModel untuk AddEditNoteScreen
 * Bertanggung jawab untuk managing state form dan operations untuk tambah/edit notes
 */
@HiltViewModel
class AddEditNoteViewModel @Inject constructor(
    private val notesRepository: NotesRepository
) : ViewModel() {
    
    private val _state = MutableStateFlow<NoteFormState?>(null)
    val state: StateFlow<NoteFormState?> = _state.asStateFlow()
    
    init {
        // Initialize with empty form
        _state.value = NoteFormState()
    }
    
    /**
     * Load note untuk editing
     */
    fun loadNote(noteId: Long) {
        viewModelScope.launch {
            val note = notesRepository.getNoteById(noteId)
            note?.let {
                _state.value = _state.value?.copy(
                    id = it.id,
                    title = it.title,
                    content = it.content,
                    color = it.color
                )
            }
        }
    }
    
    /**
     * Update title dalam form
     */
    fun updateTitle(title: String) {
        _state.value = _state.value?.copy(title = title)
    }
    
    /**
     * Update content dalam form
     */
    fun updateContent(content: String) {
        _state.value = _state.value?.copy(content = content)
    }
    
    /**
     * Update color dalam form
     */
    fun updateColor(color: Int) {
        _state.value = _state.value?.copy(color = color)
    }
    
    /**
     * Save note (insert atau update)
     */
    fun saveNote() {
        val currentState = _state.value ?: return
        
        viewModelScope.launch {
            val timestamp = System.currentTimeMillis()
            
            if (currentState.title.isBlank() && currentState.content.isBlank()) {
                // Cannot save empty note
                return@launch
            }
            
            val note = Note(
                id = currentState.id,
                title = currentState.title.trim().ifEmpty { "Catatan Tanpa Judul" },
                content = currentState.content.trim(),
                timestamp = timestamp,
                color = currentState.color
            )
            
            if (currentState.id == 0L) {
                // Insert new note
                notesRepository.insertNote(note)
            } else {
                // Update existing note
                notesRepository.updateNote(note)
            }
        }
    }
    
    /**
     * Delete note
     */
    fun deleteNote(note: Note) {
        viewModelScope.launch {
            notesRepository.deleteNote(note)
        }
    }
    
    /**
     * Reset form to empty state
     */
    fun resetForm() {
        _state.value = NoteFormState()
    }
    
    /**
     * Get current note ID (0 jika new note)
     */
    fun getCurrentNoteId(): Long = _state.value?.id ?: 0L
}

/**
 * Data class untuk form state dalam AddEditNoteScreen
 */
data class NoteFormState(
    val id: Long = 0L,
    val title: String = "",
    val content: String = "",
    val color: Int = Note.defaultColors.first()
)