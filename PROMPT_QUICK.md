# Quick Prompt untuk AI

```
Bongkar APK MyXL dan cari family codes XL untuk pembelian paket internet.

Tugas:
1. Analisis APK MyXL (com.xl.app)
2. Cari family codes seperti: UNLIMITED_TURBO, FREEDOM, COMBO_LITE, COMBO_XTRA
3. Cari API endpoint: api/v8/xl-stores/options/search/family-list
4. Cari base URL: api.xl.co.id

Lokasi cek:
- res/values/strings.xml
- assets/*.json
- classes.dex (decompile)

Pattern: FAMILY, TURBO, COMBO, FREEDOM, xl-stores

Output: JSON dengan family codes dan endpoints yang ditemukan.
```
