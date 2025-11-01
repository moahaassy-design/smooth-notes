# Panduan Menganalisis MyXL APK untuk Mencari Family Codes

## ? Ya, Bisa!

Membongkar aplikasi MyXL **sangat mungkin** bisa menemukan family codes karena:
- Aplikasi mobile biasanya menyimpan konfigurasi di dalamnya
- API endpoints sering hardcoded di aplikasi
- Family codes mungkin ada di resources atau assets
- Konstanta string bisa ditemukan di source code

## ?? Metode Analisis APK

### Metode 1: Analisis Dasar (Tanpa Decompile)
Script `analyze_myxl_apk_python.py` akan:
1. Extract APK (file ZIP)
2. Mencari di `strings.xml`
3. Mencari di folder `assets/`
4. Mencari di resources
5. Mencari API endpoints

### Metode 2: Analisis Lengkap (Dengan Decompile)

#### Menggunakan apktool (Recommended):
```bash
# Install apktool
sudo apt-get install apktool

# Decompile APK
apktool d myxl.apk

# Hasil akan di folder myxl/
```

#### Menggunakan jadx (Untuk Java source):
```bash
# Download jadx dari: https://github.com/skylot/jadx
# Decompile ke Java source
jadx -d myxl_java myxl.apk

# Atau gunakan GUI:
jadx-gui myxl.apk
```

## ?? Tempat yang Perlu Dicek

### 1. Resources (`res/`)
- `res/values/strings.xml` - String resources
- `res/values/arrays.xml` - Array data
- `res/xml/` - XML configurations

### 2. Assets (`assets/`)
- File JSON dengan konfigurasi
- File JavaScript
- File config lainnya

### 3. Smali Files (setelah decompile)
- `smali/` - Decompiled Java code
- Cari string constants
- Cari API URLs

### 4. Classes.dex (setelah decompile)
- Java source code
- Konstanta yang hardcoded
- API endpoints

### 5. AndroidManifest.xml
- Permissions dan config
- Intent filters
- Metadata

## ?? Cara Menggunakan Script

### 1. Download MyXL APK
```bash
# Dari APKPure
wget https://d.apkpure.com/b/APK/com.xl.app?version=latest -O myxl.apk

# Atau download manual dari:
# - https://apkpure.com/myxl/com.xl.app
# - https://apkmirror.com/apk/xl-axiata/myxl/
```

### 2. Jalankan Script Analisis
```bash
python3 analyze_myxl_apk_python.py
```

Script akan:
- ? Extract APK otomatis
- ? Mencari di berbagai lokasi
- ? Menemukan family codes dan API endpoints
- ? Menyimpan hasil ke JSON

### 3. Analisis Lanjutan (Opsional)

Jika script dasar tidak menemukan cukup, coba:

```bash
# Decompile dengan apktool
apktool d myxl.apk

# Analisis manual
grep -r "FAMILY\|TURBO\|COMBO" myxl/
grep -r "xl-stores" myxl/
grep -r "api/v8" myxl/
```

## ?? Yang Bisa Ditemukan

### Dari APK biasanya bisa ditemukan:
1. ? **API Endpoints** - URL lengkap ke API XL
2. ? **Family Codes** - Jika ada di resources/constants
3. ? **Package Codes** - Kode paket spesifik
4. ? **API Keys** - Jika tidak di-obfuscate
5. ? **Konfigurasi** - Base URLs, endpoints, dll

### Contoh yang mungkin ditemukan:
- `api/v8/xl-stores/options/search/family-list`
- `UNLIMITED_TURBO`, `FREEDOM`, `COMBO_LITE`
- Base URL: `https://api.xl.co.id`
- API keys atau tokens

## ?? Catatan Penting

### Jika APK Di-obfuscate:
- Kode mungkin sudah di-obfuscate
- String bisa di-encode
- Perlu analisis lebih dalam

### Jika Tidak Ditemukan Langsung:
- Family codes mungkin didapat dari API saat runtime
- Cek network traffic saat aplikasi berjalan
- Gunakan proxy seperti Charles Proxy atau mitmproxy

## ?? Tools yang Berguna

1. **apktool** - Decompile APK ke Smali
2. **jadx** - Decompile ke Java source
3. **aapt** - Analisis resources
4. **strings** - Extract strings dari binary
5. **grep** - Search pattern dalam file

## ?? Langkah-langkah Lengkap

```bash
# 1. Download APK
wget https://d.apkpure.com/b/APK/com.xl.app?version=latest -O myxl.apk

# 2. Analisis dengan script Python
python3 analyze_myxl_apk_python.py

# 3. Atau decompile manual
apktool d myxl.apk

# 4. Cari family codes
grep -r "FAMILY\|TURBO\|COMBO" myxl/
grep -r "xl-stores" myxl/

# 5. Atau gunakan jadx untuk Java source
jadx -d myxl_java myxl.apk
grep -r "family" myxl_java/
```

## ? Kesimpulan

**Ya, membongkar MyXL APK sangat mungkin menemukan family codes!**

Script `analyze_myxl_apk_python.py` sudah siap digunakan. Tinggal download APK dan jalankan script.

**Untuk hasil maksimal, kombinasikan dengan:**
- Analisis APK (script ini)
- Network traffic capture
- API langsung setelah login
