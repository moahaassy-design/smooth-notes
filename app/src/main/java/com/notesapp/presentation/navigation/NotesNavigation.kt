package com.notesapp.presentation.navigation

import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import com.notesapp.presentation.screens.HomeScreen
import com.notesapp.presentation.screens.AddEditNoteScreen

/**
 * Object untuk mendefinisikan route names
 */
object NotesScreens {
    const val HOME = "home"
    const val ADD_NOTE = "add_note"
    const val EDIT_NOTE = "edit_note/{noteId}"
}

/**
 * Composable untuk mengatur Navigation graph aplikasi
 * Menangani semua routing antar screens dengan proper navigation
 */
@Composable
fun NotesNavigation(
    navController: NavHostController,
    paddingValues: PaddingValues,
    modifier: Modifier = Modifier
) {
    NavHost(
        navController = navController,
        startDestination = NotesScreens.HOME,
        modifier = modifier
    ) {
        // Home Screen - Menampilkan daftar semua notes
        composable(NotesScreens.HOME) {
            HomeScreen(
                paddingValues = paddingValues,
                onAddNote = {
                    navController.navigate(NotesScreens.ADD_NOTE)
                },
                onEditNote = { noteId ->
                    navController.navigate("${NotesScreens.EDIT_NOTE}/$noteId")
                }
            )
        }
        
        // Add Note Screen - Form untuk menambah note baru
        composable(NotesScreens.ADD_NOTE) {
            AddEditNoteScreen(
                paddingValues = paddingValues,
                onBack = {
                    navController.popBackStack()
                }
            )
        }
        
        // Edit Note Screen - Form untuk mengedit note existing
        composable(
            route = NotesScreens.EDIT_NOTE
        ) { backStackEntry ->
            val noteId = backStackEntry.arguments?.getString("noteId")?.toLongOrNull()
            AddEditNoteScreen(
                paddingValues = paddingValues,
                noteId = noteId,
                onBack = {
                    navController.popBackStack()
                }
            )
        }
    }
}