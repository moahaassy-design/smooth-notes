# 📝 Notes App

[![Android CI/CD](https://github.com/moahaassy-design/smooth-notes/workflows/Android%20CI/CD/badge.svg)](https://github.com/moahaassy-design/smooth-notes/actions)
[![Kotlin](https://img.shields.io/badge/Kotlin-1.9.20-blue.svg)](https://kotlinlang.org/)
[![Android](https://img.shields.io/badge/Android-8.1.4-green.svg)](https://developer.android.com/)
[![API](https://img.shields.io/badge/API-21%2B-brightgreen.svg)](https://developer.android.com/studio/releases/platforms)

Notes App adalah aplikasi Android moderno untuk mencatat dan mengelola catatan pribadi dengan Material You design dan fitur-fitur canggih.

## ✨ Fitur

### 🚀 Fitur Utama
- ✅ **CRUD Notes**: Buat, baca, update, dan hapus catatan dengan mudah
- 🔍 **Pencarian**: Cari catatan berdasarkan judul atau konten
- 📅 **Sorting**: Urutkan catatan berdasarkan tanggal (terbaru/terlama)
- 🎨 **Material You**: Dynamic color theme dengan dukungan dark mode
- 💾 **Local Storage**: Penyimpanan lokal menggunakan Room Database
- 🏗️ **Clean Architecture**: Struktur kode yang clean dan maintainable
- 📱 **Responsive**: UI yang responsif untuk berbagai ukuran layar

### 🔧 Teknologi & Arsitektur
- **Architecture Pattern**: MVVM + Clean Architecture
- **UI Framework**: Jetpack Compose Material Design 3
- **Database**: Room Database untuk local storage
- **Navigation**: Android Navigation Compose
- **State Management**: StateFlow & MutableState
- **Dependency Injection**: Hilt
- **Async**: Kotlin Coroutines & Flow

## 🏗️ Arsitektur

Proyek ini mengimplementasikan **Clean Architecture** dengan pemisahan layer yang jelas:

```
📁 src/main/java/com/notesapp/
├── 📁 data/           # Data Layer
│   ├── 📁 database/   # Room Database, Entities, DAOs
│   └── 📁 repository/ # Repository implementation
├── 📁 domain/         # Business Logic Layer
│   ├── 📁 model/      # Domain models
│   └── 📁 repository/ # Repository interfaces
└── 📁 presentation/   # UI Layer
    ├── 📁 components/ # Reusable UI components
    ├── 📁 state/      # UI State management
    ├── 📁 notes_list/ # Notes list screen
    ├── 📁 add_edit_note/ # Add/edit note screen
    └── 📁 theme/      # Material You theming
```

### 📊 Database Schema

```kotlin
@Entity(tableName = "notes")
data class NoteEntity(
    @PrimaryKey(autoGenerate = true)
    val id: Long = 0,
    val title: String,
    val content: String,
    val timestamp: Long,
    val color: Int
)
```

## 🛠️ Persyaratan

### Development Environment
- **Android Studio**: Hedgehog (2023.1.1) atau lebih baru
- **JDK**: 17 (recommended: Temurin distribution)
- **Android SDK**: API 34 (Android 14)
- **Gradle**: 8.x compatible dengan Android Gradle Plugin 8.1.4

### Minimum Requirements
- **Min SDK**: 21 (Android 5.0 Lollipop)
- **Target SDK**: 34 (Android 14)
- **Compile SDK**: 34

## 🚀 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/moahaassy-design/smooth-notes.git
cd smooth-notes
```

### 2. Android Studio Setup
1. Buka Android Studio
2. Pilih "Open an existing Android Studio project"
3. Navigate ke folder cloned repository
4. Tunggu Gradle sync selesai

### 3. Configure SDK
- Buka `File > Project Structure > SDK Location`
- Set SDK path sesuai dengan instalasi Android SDK Anda
- Pastikan menggunakan JDK 17

## 🔨 Build Instructions

### Development Build
```bash
# Clean project
./gradlew clean

# Debug build
./gradlew assembleDebug

# Install debug APK ke device/emulator
./gradlew installDebug
```

### Release Build
```bash
# Release build (requires signing configuration)
./gradlew assembleRelease
```

### Testing
```bash
# Run unit tests
./gradlew test

# Run instrumentation tests
./gradlew connectedAndroidTest
```

## 📱 Features Guide

### 📝 Manage Notes
- **Tambah Catatan**: Tap tombol "+" untuk membuat catatan baru
- **Edit Catatan**: Tap catatan untuk mengedit konten
- **Hapus Catatan**: Long press catatan dan confirm deletion
- **Cari Catatan**: Gunakan search bar untuk mencari catatan

### 🎨 Theming
- **Material You**: App menggunakan dynamic colors dari system
- **Dark Mode**: Otomatis mengikuti system theme setting
- **Custom Colors**: Support untuk note colors berbeda

### 🔍 Advanced Features
- **Real-time Search**: Pencarian real-time saat mengetik
- **Date Sorting**: Sorting notes berdasarkan creation/update timestamp
- **Auto-save**: Notes otomatis tersimpan saat di-edit
- **State Management**: Proper UI state handling dengan loading/error states

## 📊 CI/CD Pipeline

### GitHub Actions Workflow
Automated pipeline yang melakukan:

- ✅ **Matrix Build**: Testing pada Android API 33 dan 34
- ✅ **JDK 17 Setup**: Menggunakan Temurin distribution
- ✅ **Gradle Cache**: Optimization untuk build speed
- ✅ **Unit & Integration Tests**: Testing lengkap
- ✅ **APK Artifacts**: Debug dan release APK upload
- ✅ **Test Reports**: Laporan testing tersedia

### Pipeline Triggers
Workflow berjalan otomatis pada:
- Setiap push ke branch `main` dan `develop`
- Pull request ke branch `main` dan `develop`
- Manual trigger via GitHub Actions

### Build Artifacts
Pipeline menggenerate artifact:
- `app-debug-{api-level}` - Debug APK untuk setiap API level
- `app-release-{api-level}` - Release APK untuk setiap API level  
- `test-reports-{api-level}` - Laporan testing dan coverage

## 🎨 Jetpack Compose Material Design 3 Implementation

### 🚀 Modern UI dengan Material You

Proyek ini mengimplementasikan **Jetpack Compose Material Design 3** yang lengkap dengan fitur-fitur modern:

#### ✨ Material You Theme
- **Dynamic Colors**: Menggunakan Material You dynamic colors pada Android 12+
- **Dark Mode Support**: Dukungan penuh untuk tema gelap dan terang
- **Responsive Design**: UI yang responsif dan accessible
- **Smooth Animations**: Transisi dan animasi yang halus

#### 📱 New Compose Screens

**NotesListScreen** (`app/src/main/java/com/notesapp/presentation/notes_list/`)
- ✅ Grid/List View Toggle dengan animasi smooth
- ✅ Search functionality dengan real-time filtering
- ✅ FloatingActionButton dengan ripple effects
- ✅ Note cards dengan color indicators
- ✅ Empty state yang informatif
- ✅ Animated list items dengan enter/exit transitions

**AddEditNoteScreen** (`app/src/main/java/com/notesapp/presentation/add_edit_note/`)
- ✅ Rich text editing dengan formatted text fields
- ✅ Color picker dengan 18 color options
- ✅ Save/Delete functionality dengan loading states
- ✅ Smooth slide transitions
- ✅ Auto-focus pada judul field
- ✅ FAB dengan save functionality

#### 🎯 Reusable Components

- **SearchBar**: Search bar dengan icon dan Material 3 styling
- **NoteCard**: Kartu catatan dengan color indicators dan actions
- **ColorPicker**: Grid picker dengan 18 Material colors
- **Typography**: Material 3 typography system
- **Theme**: Material You theme dengan dynamic color support

## 🤝 Contributing

Kami welcome kontribusi dari developer! Silakan ikuti guidelines berikut:

### Development Workflow
1. **Fork** repository
2. **Create feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open Pull Request**

### Code Standards
- ✅ **Kotlin Coding Conventions**: Ikuti official Kotlin style guide
- ✅ **Architecture**: Pertahankan Clean Architecture pattern
- ✅ **Testing**: Tulis unit tests untuk business logic
- ✅ **Documentation**: Update dokumentasi untuk new features

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👥 Authors

- **MiniMax Agent** - *Initial work* - [MiniMax](https://github.com/minimax)

## 🙏 Acknowledgments

- [Android Developers](https://developer.android.com/) - Official Android documentation
- [Material Design](https://material.io/design) - Design system guidelines
- [Kotlin](https://kotlinlang.org/) - Programming language
- [Room Database](https://developer.android.com/training/data-storage/room) - Local database

---

<div align="center">
  <strong>⭐ Jika project ini membantu, jangan lupa berikan star! ⭐</strong>
</div>