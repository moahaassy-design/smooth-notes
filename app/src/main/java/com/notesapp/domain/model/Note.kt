package com.notesapp.domain.model

/**
 * Domain model untuk Note
 * Tidak bergantung pada database framework atau UI libraries
 */
data class Note(
    val id: Long = 0,
    val title: String,
    val content: String,
    val timestamp: Long,
    val color: Int
) {
    companion object {
        /**
         * Default color options untuk notes
         */
        val defaultColors = listOf(
            0xFF2196F3.toInt(), // Blue
            0xFF4CAF50.toInt(), // Green
            0xFFFF9800.toInt(), // Orange
            0xFF9C27B0.toInt(), // Purple
            0xFFF44336.toInt(), // Red
            0xFF00BCD4.toInt(), // Cyan
            0xFFFFEB3B.toInt(), // Yellow
            0xFF607D8B.toInt()  // Blue Grey
        )
    }
}