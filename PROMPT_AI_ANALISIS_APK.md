# PROMPT UNTUK AI: Bongkar APK MyXL dan Cari Family Codes

## Prompt Lengkap untuk Analisis APK MyXL

```
Saya ingin Anda membantu saya membongkar aplikasi MyXL (Android APK) untuk menemukan family codes yang digunakan untuk membeli paket internet XL melalui me-cli.

TUGAS:
1. Download atau analisis file APK MyXL (com.xl.app)
2. Extract dan analisis semua komponen APK
3. Cari family codes, API endpoints, dan konfigurasi terkait paket internet XL

LANGKAH-LANGKAH YANG HARUS DILAKUKAN:

1. DOWNLOAD APK:
   - Download MyXL APK dari https://apkpure.com/myxl/com.xl.app atau sumber resmi lainnya
   - File APK adalah file ZIP, extract isinya

2. ANALISIS STRUKTUR APK:
   - AndroidManifest.xml - cari permissions, API endpoints, metadata
   - res/values/strings.xml - cari string resources yang mungkin berisi family codes
   - res/values/arrays.xml - cari array data paket
   - assets/ - analisis semua file JSON, JS, atau config
   - classes.dex - decompile untuk melihat source code Java
   - smali/ - jika sudah decompile dengan apktool

3. CARI PATTERN BERIKUT:
   - Family codes: "FAMILY", "family_code", "package_family_code"
   - Paket populer: "UNLIMITED_TURBO", "FREEDOM", "COMBO_LITE", "COMBO_XTRA", "COMBO_MAX"
   - API endpoints: "api/v8/xl-stores", "xl-stores/options/search/family-list"
   - Base URLs: "api.xl.co.id", "ciam.xl.co.id"
   - Konstanta string yang mengandung pattern [A-Z_]{5,} dengan keyword FAMILY, TURBO, COMBO

4. TEMPAT YANG WAJIB DIPERIKSA:
   - Semua file .xml di folder res/
   - Semua file di folder assets/
   - Semua file .smali jika sudah decompile
   - Semua file .java jika sudah decompile dengan jadx
   - AndroidManifest.xml (perlu aapt atau axmlparser untuk binary)

5. OUTPUT YANG DIHARAPKAN:
   - Daftar semua family codes yang ditemukan
   - API endpoints lengkap dengan path
   - Base URLs yang digunakan
   - Konfigurasi API lainnya
   - Format output: JSON dengan struktur:
     {
       "family_codes": [
         {"code": "UNLIMITED_TURBO", "source": "strings.xml", "location": "res/values/strings.xml"},
         ...
       ],
       "api_endpoints": [
         {"url": "api/v8/xl-stores/options/search/family-list", "method": "POST"},
         ...
       ],
       "base_urls": ["https://api.xl.co.id", ...],
       "configurations": {...}
     }

6. METODE ANALISIS:
   - Gunakan grep, sed, atau tool text search untuk mencari pattern
   - Jika ada file binary, gunakan strings command atau hexdump
   - Untuk classes.dex, decompile dengan jadx atau jadx-gui
   - Untuk AndroidManifest.xml binary, gunakan aapt dump atau apktool

7. PRIORITAS PENCARIAN:
   - Priority 1: res/values/strings.xml (sering berisi konstanta)
   - Priority 2: assets/*.json (konfigurasi)
   - Priority 3: smali/*.smali atau java/*.java (source code)
   - Priority 4: AndroidManifest.xml
   - Priority 5: File lainnya

8. CATATAN PENTING:
   - APK mungkin di-obfuscate, jadi string bisa di-encode
   - Family codes mungkin tidak hardcoded tapi didapat dari API saat runtime
   - Fokus pada API endpoints karena itu yang paling berguna
   - Jika menemukan API endpoint, catat juga payload/request format

Lakukan analisis menyeluruh dan berikan hasil lengkap dengan semua family codes dan API endpoints yang ditemukan.
```

## Prompt Singkat (Quick Version)

```
Bongkar APK MyXL (com.xl.app) dan cari:
1. Family codes (UNLIMITED_TURBO, FREEDOM, COMBO_LITE, dll)
2. API endpoints (xl-stores/options/search/family-list)
3. Base URLs (api.xl.co.id)
4. Konfigurasi API lainnya

Cek di:
- res/values/strings.xml
- assets/*.json
- classes.dex (decompile dengan jadx)
- smali/ (jika sudah decompile)

Output: JSON dengan semua family codes dan endpoints yang ditemukan.
```

## Prompt untuk ChatGPT/Claude/Gemini

```
Saya perlu Anda membantu menganalisis APK aplikasi MyXL (Android) untuk menemukan family codes yang digunakan untuk membeli paket internet XL.

Tugas:
1. Analisis struktur APK MyXL
2. Cari family codes seperti UNLIMITED_TURBO, FREEDOM, COMBO_LITE, dll
3. Cari API endpoints khususnya "api/v8/xl-stores/options/search/family-list"
4. Cari base URLs dan konfigurasi API

Lokasi yang perlu dicek:
- res/values/strings.xml (string resources)
- assets/ folder (file JSON/JS/config)
- classes.dex (decompile ke Java untuk melihat source code)
- smali/ files (jika sudah decompile)

Pattern yang dicari:
- Family codes: "FAMILY", "family_code", "package_family_code"
- Paket: "UNLIMITED_TURBO", "FREEDOM", "COMBO_LITE", "COMBO_XTRA"
- API: "xl-stores", "api/v8", "family-list"

Output yang diinginkan:
Format JSON dengan:
- Daftar family codes beserta lokasi ditemukan
- API endpoints lengkap
- Base URLs
- Konfigurasi lainnya

Tolong analisis secara menyeluruh dan berikan hasil lengkap.
```

## Prompt untuk GitHub Copilot/Cursor

```
Saya punya APK MyXL yang perlu dianalisis untuk menemukan family codes XL.

Buat script Python yang:
1. Extract APK (file ZIP)
2. Cari family codes di:
   - res/values/strings.xml
   - assets/*.json, *.js
   - Semua file text lainnya
3. Cari API endpoints: "xl-stores", "api/v8", "family-list"
4. Decompile classes.dex jika perlu (gunakan jadx)
5. Output JSON dengan semua temuan

Pattern yang dicari:
- [A-Z_]{5,} dengan keyword FAMILY, TURBO, COMBO, FREEDOM
- URLs dengan "api.xl.co.id" atau "xl-stores"
- String constants yang mungkin family codes

Script harus bisa:
- Handle APK extraction
- Search recursively di semua file
- Parse XML dan JSON
- Output hasil dalam format terstruktur
```

## Prompt untuk Terminal/Command Line AI

```
Saya punya file myxl.apk. Bantu saya:

1. Extract APK: unzip myxl.apk -d myxl_extracted
2. Cari family codes dengan grep:
   grep -r "FAMILY\|TURBO\|COMBO\|FREEDOM" myxl_extracted/
   grep -r "xl-stores" myxl_extracted/
   grep -r "api/v8" myxl_extracted/
3. Cek strings.xml: cat myxl_extracted/res/values/strings.xml | grep -i family
4. Cek assets: find myxl_extracted/assets -name "*.json" -exec cat {} \;
5. Decompile classes.dex jika perlu: jadx -d myxl_java myxl.apk

Berikan command lengkap dan jelaskan hasilnya.
```

## Prompt untuk Analisis Manual

```
Saya ingin menganalisis APK MyXL secara manual. Berikan langkah-langkah:

1. Persiapan:
   - Tools yang diperlukan (apktool, jadx, aapt)
   - Cara install tools tersebut

2. Extract & Decompile:
   - Cara extract APK biasa
   - Cara decompile dengan apktool
   - Cara decompile ke Java dengan jadx

3. Analisis:
   - File apa saja yang perlu dicek
   - Command grep/sed untuk mencari pattern
   - Cara membaca AndroidManifest.xml binary
   - Cara analisis classes.dex

4. Pencarian:
   - Pattern regex untuk family codes
   - Pattern untuk API endpoints
   - Pattern untuk base URLs

5. Output:
   - Format output yang disarankan
   - Cara dokumentasi temuan

Berikan panduan lengkap step-by-step.
```

## Prompt untuk Code Generation

```
Generate Python script untuk analisis APK MyXL yang:

1. Extract APK menggunakan zipfile
2. Parse XML files (strings.xml, arrays.xml)
3. Parse JSON files di assets/
4. Search pattern menggunakan regex:
   - Family codes: r'["\']([A-Z_]{5,})["\']'
   - API endpoints: r'https?://[^"\s]+api[^"\s]+'
   - Base URLs: r'api\.xl\.co\.id|ciam\.xl\.co\.id'
5. Decompile classes.dex jika mungkin (gunakan jadx wrapper)
6. Output JSON dengan struktur:
   {
     "family_codes": [{"code": "...", "source": "...", "location": "..."}],
     "api_endpoints": [{"url": "...", "method": "..."}],
     "base_urls": ["..."],
     "configurations": {...}
   }

Script harus robust, handle errors, dan memberikan output yang jelas.
```

---

## Cara Menggunakan Prompt Ini

1. **Untuk ChatGPT/Claude/Gemini:**
   - Copy prompt lengkap atau prompt singkat
   - Paste ke chat AI
   - Upload file APK jika AI support file upload
   - Atau minta AI buatkan script analisis

2. **Untuk GitHub Copilot/Cursor:**
   - Gunakan prompt untuk code generation
   - AI akan generate script Python untuk analisis

3. **Untuk Terminal/Command Line:**
   - Gunakan prompt untuk Terminal
   - AI akan memberikan command yang tepat

4. **Untuk Analisis Manual:**
   - Gunakan prompt untuk analisis manual
   - Ikuti langkah-langkah yang diberikan

## Tips

- Gunakan prompt yang sesuai dengan AI tool yang digunakan
- Jika AI tidak bisa langsung analisis APK, minta buatkan script
- Kombinasikan beberapa prompt untuk hasil maksimal
- Pastikan AI memahami konteks "family codes" dan "XL internet packages"
