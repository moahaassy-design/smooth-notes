package com.notesapp.presentation.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.Save
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.hilt.navigation.compose.hiltViewModel
import com.notesapp.domain.model.Note
import com.notesapp.presentation.viewmodel.AddEditNoteViewModel

/**
 * AddEditNoteScreen - Form untuk menambah dan mengedit notes
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AddEditNoteScreen(
    paddingValues: PaddingValues,
    noteId: Long? = null,
    onBack: () -> Unit,
    viewModel: AddEditNoteViewModel = hiltViewModel()
) {
    val isEditing = noteId != null
    val state by viewModel.state.collectAsState()
    
    // Initialize form with note data if editing
    LaunchedEffect(noteId) {
        noteId?.let {
            viewModel.loadNote(it)
        }
    }
    
    Scaffold(
        modifier = Modifier
            .fillMaxSize()
            .padding(paddingValues),
        topBar = {
            TopAppBar(
                title = { 
                    Text(
                        if (isEditing) "Edit Catatan" else "Catatan Baru",
                        fontWeight = FontWeight.Bold
                    ) 
                },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Kembali")
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = MaterialTheme.colorScheme.primaryContainer
                ),
                actions = {
                    if (isEditing) {
                        IconButton(onClick = { 
                            state?.let { viewModel.deleteNote(it) }
                            onBack()
                        }) {
                            Icon(Icons.Default.Delete, contentDescription = "Hapus")
                        }
                    }
                    IconButton(onClick = { 
                        viewModel.saveNote()
                        onBack()
                    }) {
                        Icon(Icons.Default.Save, contentDescription = "Simpan")
                    }
                }
            )
        }
    ) { innerPadding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
                .padding(16.dp)
        ) {
            // Title Input
            OutlinedTextField(
                value = state?.title ?: "",
                onValueChange = { viewModel.updateTitle(it) },
                label = { Text("Judul") },
                placeholder = { Text("Masukkan judul catatan") },
                modifier = Modifier.fillMaxWidth(),
                textStyle = MaterialTheme.typography.titleLarge
            )
            
            Spacer(modifier = Modifier.height(16.dp))
            
            // Content Input
            OutlinedTextField(
                value = state?.content ?: "",
                onValueChange = { viewModel.updateContent(it) },
                label = { Text("Konten") },
                placeholder = { Text("Tulis catatan Anda...") },
                modifier = Modifier.fillMaxSize(),
                textStyle = MaterialTheme.typography.bodyLarge
            )
            
            Spacer(modifier = Modifier.height(24.dp))
            
            // Color Selection
            Text(
                text = "Pilih Warna",
                style = MaterialTheme.typography.titleMedium,
                color = MaterialTheme.colorScheme.onSurface
            )
            
            Spacer(modifier = Modifier.height(8.dp))
            
            LazyRow(
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                items(Note.defaultColors) { color ->
                    ColorPickerItem(
                        color = Color(color),
                        isSelected = state?.color == color,
                        onClick = { viewModel.updateColor(color) }
                    )
                }
            }
        }
    }
}

/**
 * ColorPickerItem - UI untuk picker warna catatan
 */
@Composable
fun ColorPickerItem(
    color: Color,
    isSelected: Boolean,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    Box(
        modifier = modifier
            .size(40.dp)
            .clip(androidx.compose.foundation.shape.CircleShape)
            .background(color)
            .clickable { onClick() },
        contentAlignment = Alignment.Center
    ) {
        if (isSelected) {
            androidx.compose.foundation.Canvas(
                modifier = Modifier.size(16.dp)
            ) {
                drawCircle(
                    color = Color.White,
                    radius = size.minDimension / 2
                )
            }
        }
    }
}