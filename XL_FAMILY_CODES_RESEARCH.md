# Informasi Family Code XL untuk me-cli

## Ringkasan

Family code adalah kode identifikasi untuk grup paket internet XL. Setiap family code mewakili sekelompok paket dengan karakteristik serupa (misalnya: Unlimited Turbo, Freedom, dll).

## Cara Mendapatkan Family Code

### Metode 1: Menggunakan me-cli (Paling Mudah)

1. Jalankan me-cli:
   ```bash
   python main.py
   ```

2. Login dengan akun XL Anda

3. Pilih menu **"12. Store Family List"**
   - Pilih apakah enterprise atau tidak (y/n)
   - Tool akan menampilkan daftar family codes yang tersedia

4. Setelah mendapatkan family code, gunakan menu:
   - **"6. Beli Paket Berdasarkan Family Code"** - untuk melihat paket dalam family
   - **"7. Beli Semua Paket di Family Code (loop)"** - untuk membeli semua paket dalam family

### Metode 2: Menggunakan API Langsung

Family codes dapat diambil dari API endpoint:
```
POST api/v8/xl-stores/options/search/family-list
```

Payload:
```json
{
    "is_enterprise": false,
    "subs_type": "PREPAID",  // atau "POSTPAID"
    "lang": "en"
}
```

### Metode 3: Dari MyXL App

1. Download MyXL APK dari Play Store atau sumber resmi
2. Login ke aplikasi MyXL
3. Buka menu "Beli Paket" atau "Store"
4. Setiap paket memiliki family code yang dapat dilihat di:
   - Network request saat membuka detail paket
   - Package metadata dalam aplikasi
   - API response dari aplikasi

## Cara Menggunakan Family Code untuk Beli Paket

### Menggunakan me-cli:

1. **Lihat Paket dalam Family:**
   ```
   Menu: 6
   Masukkan family code: [FAMILY_CODE]
   ```

2. **Beli Semua Paket dalam Family:**
   ```
   Menu: 7
   Masukkan family code: [FAMILY_CODE]
   Start from option: [1]
   Use decoy: [y/n]
   Pause on success: [y/n]
   Delay seconds: [0]
   ```

### Contoh Family Code (perlu diverifikasi):
- Unlimited Turbo: `UNLIMITED_TURBO` (contoh)
- Freedom: `FREEDOM` (contoh)
- Combo Lite: `COMBO_LITE` (contoh)

**Catatan:** Family codes sebenarnya harus diambil dari API karena bisa berubah dan berbeda untuk setiap tipe subscriber (PREPAID/POSTPAID, Enterprise/Non-Enterprise).

## Struktur API Family Code

### Endpoint: Get Family List
```python
POST api/v8/xl-stores/options/search/family-list
{
    "is_enterprise": false,
    "subs_type": "PREPAID",
    "lang": "en"
}
```

Response:
```json
{
    "status": "SUCCESS",
    "data": {
        "results": [
            {
                "id": "FAMILY_CODE_1",
                "label": "Nama Family Paket"
            },
            ...
        ]
    }
}
```

### Endpoint: Get Packages by Family Code
```python
POST api/v8/xl-stores/options/list
{
    "package_family_code": "FAMILY_CODE",
    "is_enterprise": false,
    "is_show_tagging_tab": true,
    "is_dedicated_event": true,
    "is_transaction_routine": false,
    "migration_type": "NONE",
    "is_autobuy": false,
    "is_pdlp": true,
    "referral_code": "",
    "is_migration": false,
    "lang": "en"
}
```

## Ekstraksi dari MyXL APK

Untuk mendapatkan family codes dari MyXL APK:

1. **Download APK:**
   ```bash
   # Gunakan tools seperti:
   # - apkpure.com
   # - apkmirror.com
   # - atau langsung dari Play Store dengan tools seperti gplaycli
   ```

2. **Extract APK:**
   ```bash
   # Dekompresi APK (zip file)
   unzip myxl.apk -d myxl_extracted
   
   # Cari file yang mengandung family codes:
   grep -r "family" myxl_extracted/
   grep -r "package_family_code" myxl_extracted/
   ```

3. **Analisis Network Traffic:**
   - Gunakan proxy seperti Charles Proxy atau mitmproxy
   - Capture traffic saat membuka MyXL app
   - Cari request ke `api/v8/xl-stores/options/search/family-list`

## Referensi Kode me-cli

### File-file Penting:
- `app/client/store/search.py` - Fungsi `get_family_list()` untuk mengambil daftar family codes
- `app/client/engsel.py` - Fungsi `get_family()` untuk mengambil paket berdasarkan family code
- `app/menus/purchase.py` - Fungsi `purchase_by_family()` untuk membeli paket menggunakan family code
- `app/menus/store/search.py` - Menu untuk menampilkan family list

### Contoh Penggunaan dalam Code:
```python
from app.client.store.search import get_family_list
from app.client.engsel import get_family

# Ambil daftar family codes
family_list = get_family_list(api_key, tokens, "PREPAID", False)

# Ambil paket berdasarkan family code
family_data = get_family(api_key, tokens, "FAMILY_CODE")
```

## Tips

1. **Family codes berbeda untuk:**
   - PREPAID vs POSTPAID
   - Enterprise vs Non-Enterprise
   - Migration type (PRE_TO_PRIOH, PRIOH_TO_PRIO, dll)

2. **Cara terbaik mendapatkan family codes:**
   - Gunakan fitur "Store Family List" di me-cli (menu 12)
   - Atau call API langsung jika sudah punya API key

3. **Sebelum membeli:**
   - Pastikan balance cukup
   - Cek detail paket dengan menu 6 terlebih dahulu
   - Perhatikan harga dan validity

## Catatan Penting

?? **Family codes dapat berubah** - Selalu ambil daftar terbaru dari API sebelum menggunakan untuk pembelian.

?? **Butuh API Key** - Untuk menggunakan me-cli, Anda perlu API key dari bot Telegram [@fykxt_bot](https://t.me/fykxt_bot) dengan command `/viewkey`.
