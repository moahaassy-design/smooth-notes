package com.notesapp.presentation.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.notesapp.domain.model.Note
import com.notesapp.domain.repository.NotesRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.*
import kotlinx.coroutines.launch
import javax.inject.Inject

/**
 * HomeViewModel - ViewModel untuk HomeScreen
 * Bertanggung jawab untuk managing state dan operations untuk daftar notes
 */
@HiltViewModel
class HomeViewModel @Inject constructor(
    private val notesRepository: NotesRepository
) : ViewModel() {
    
    private val _searchQuery = MutableStateFlow("")
    val searchQuery: StateFlow<String> = _searchQuery.asStateFlow()
    
    private val _isSearching = MutableStateFlow(false)
    val isSearching: StateFlow<Boolean> = _isSearching.asStateFlow()
    
    val notes: StateFlow<List<Note>> = combine(
        notesRepository.getAllNotes(),
        _searchQuery,
        _isSearching
    ) { allNotes, query, isSearching ->
        if (isSearching && query.isNotEmpty()) {
            // Note: This will be implemented with search functionality
            allNotes.filter { it.title.contains(query, ignoreCase = true) }
        } else {
            allNotes
        }
    }.stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5000),
        initialValue = emptyList()
    )
    
    init {
        // Load notes dari database
        loadNotes()
    }
    
    /**
     * Load semua notes dari repository
     */
    private fun loadNotes() {
        viewModelScope.launch {
            notesRepository.getAllNotes()
                .collect { notes ->
                    // Data akan di-handle oleh StateFlow
                }
        }
    }
    
    /**
     * Update search query dan trigger search
     */
    fun updateSearchQuery(query: String) {
        _searchQuery.value = query
        _isSearching.value = query.isNotEmpty()
    }
    
    /**
     * Clear search dan reset to show all notes
     */
    fun clearSearch() {
        _searchQuery.value = ""
        _isSearching.value = false
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
     * Get total notes count
     */
    suspend fun getNotesCount(): Int {
        return notesRepository.getNotesCount()
    }
}