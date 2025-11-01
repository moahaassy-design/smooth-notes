# Ringkasan Penelitian: XL Family Codes untuk me-cli

## Hasil Penelitian

Setelah menganalisis repository me-cli dan struktur API XL, berikut adalah temuan utama:

### 1. Apa itu Family Code?

Family code adalah identifier unik untuk grup paket internet XL. Setiap family code mewakili sekelompok paket dengan karakteristik serupa (misalnya: Unlimited Turbo, Freedom, Combo Lite, dll).

### 2. Cara Mendapatkan Family Codes

#### Metode 1: Menggunakan me-cli (Termudah)
```
Menu: 12 ? Store Family List
```
Ini akan memanggil API endpoint: `api/v8/xl-stores/options/search/family-list`

#### Metode 2: Menggunakan Script Python
Jalankan `get_family_codes.py` dengan API key dan ID token dari me-cli.

#### Metode 3: Analisis MyXL APK
Jalankan `analyze_myxl_apk.sh` untuk menganalisis MyXL APK dan mencari family codes di dalamnya.

### 3. API Endpoints yang Digunakan

**Get Family List:**
- Endpoint: `POST api/v8/xl-stores/options/search/family-list`
- Payload: `{"is_enterprise": false, "subs_type": "PREPAID", "lang": "en"}`
- Response berisi array `results` dengan `id` (family code) dan `label` (nama family)

**Get Packages by Family Code:**
- Endpoint: `POST api/v8/xl-stores/options/list`
- Payload: `{"package_family_code": "{FAMILY_CODE}", ...}`
- Response berisi detail semua paket dalam family tersebut

### 4. Cara Menggunakan Family Code untuk Beli Paket

1. **Lihat Paket:**
   ```
   Menu: 6 ? Masukkan family code ? Pilih paket
   ```

2. **Beli Semua Paket dalam Family:**
   ```
   Menu: 7 ? Masukkan family code ? Konfigurasi ? Beli
   ```

### 5. Struktur Kode me-cli

**File-file Penting:**
- `app/client/store/search.py` - Fungsi `get_family_list()`
- `app/client/engsel.py` - Fungsi `get_family()` untuk mengambil paket
- `app/menus/purchase.py` - Fungsi `purchase_by_family()` untuk pembelian
- `app/menus/store/search.py` - Menu untuk menampilkan family list

**Flow:**
1. User login ? dapat ID token
2. Panggil API dengan family code ? dapat daftar paket
3. Pilih paket ? dapat package option code
4. Purchase dengan package option code

### 6. Informasi Penting

- **Family codes berbeda untuk:**
  - PREPAID vs POSTPAID
  - Enterprise vs Non-Enterprise
  - Migration type (PRE_TO_PRIOH, PRIOH_TO_PRIO, dll)

- **Family codes dapat berubah** - Selalu ambil daftar terbaru dari API

- **Butuh API Key** - Dapat dari bot Telegram [@fykxt_bot](https://t.me/fykxt_bot) dengan command `/viewkey`

### 7. File-file yang Dibuat

1. **XL_FAMILY_CODES_RESEARCH.md** - Dokumentasi lengkap tentang family codes
2. **QUICK_START.md** - Panduan cepat untuk mulai menggunakan
3. **get_family_codes.py** - Script Python untuk mendapatkan family codes
4. **analyze_myxl_apk.sh** - Script bash untuk analisis MyXL APK

### 8. Rekomendasi

**Cara Terbaik:**
1. Gunakan menu "Store Family List" di me-cli (menu 12)
2. Ini adalah cara termudah dan terpercaya untuk mendapatkan family codes terbaru
3. Family codes langsung dari API selalu up-to-date

**Untuk Pengembangan:**
- Jika ingin mengintegrasikan ke aplikasi lain, gunakan script `get_family_codes.py` sebagai referensi
- API endpoints yang digunakan sudah teridentifikasi dengan jelas
- Struktur request/response sudah terdokumentasi

### 9. Catatan Teknis

- Base API URL di-set via environment variable (`BASE_API_URL`)
- API menggunakan encryption (`encryptsign_xdata`) untuk payload
- Memerlukan signature header (`x-signature`) untuk autentikasi
- Token perlu di-refresh secara berkala

### 10. Langkah Selanjutnya

Untuk menggunakan family codes:
1. Dapatkan API key dari @fykxt_bot
2. Login ke me-cli dengan nomor XL
3. Gunakan menu 12 untuk melihat family codes
4. Pilih family code yang diinginkan
5. Gunakan menu 6 atau 7 untuk membeli paket

## Kesimpulan

Family codes XL dapat diperoleh dengan mudah melalui:
- ? Menu "Store Family List" di me-cli (paling mudah)
- ? Script Python dengan API key (untuk otomatisasi)
- ? Analisis MyXL APK (untuk penelitian)

Semua metode sudah terdokumentasi dan siap digunakan.
