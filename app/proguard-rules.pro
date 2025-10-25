# Add project specific ProGuard rules here.
# You can control the set of applied configuration files using the
# proguardFiles setting in build.gradle.
#
# For more details, see
#   http://developer.android.com/guide/developing/tools/proguard.html

# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}

# Uncomment this to preserve the line number information for
# debugging stack traces.
-keepattributes SourceFile,LineNumberTable

# If you keep the line number information, uncomment this to
# hide the original source file name.
-renamesourcefileattribute SourceFile

# Keep Room entities
-keep class com.notesapp.data.database.** { *; }

# Keep Hilt classes
-keep class dagger.hilt.** { *; }

# Keep annotation processor classes
-keep class * extends javax.inject.Named

# Generic keep rules for data classes
-keep class com.notesapp.domain.** { *; }
-keep class com.notesapp.presentation.** { *; }

# Keep enum classes
-keepclassmembers enum * {
    public static **[] values();
    public static ** valueOf(java.lang.String);
}

# Keep parcelable classes
-keepclassmembers class * implements android.os.Parcelable {
  public static final android.os.Parcelable$Creator CREATOR;
}

# Keep application class
-keep class com.notesapp.NotesApplication { *; }

# Room annotations
-keep class * extends androidx.room.RoomDatabase { *; }
-keep @androidx.room.Entity class * { *; }
-keep @androidx.room.Dao class * { *; }

# Material Design classes
-keep class androidx.compose.material3.** { *; }
-keep class androidx.compose.material.** { *; }
