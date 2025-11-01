# Quick Start Guide: XL Family Codes untuk me-cli

## Ringkasan Singkat

Family code adalah identifier untuk grup paket internet XL. Setiap family code mewakili sekelompok paket dengan karakteristik serupa.

## Cara Cepat Mendapatkan Family Codes

### ? Metode Tercepat: Menggunakan me-cli

1. **Setup me-cli:**
   ```bash
   git clone https://github.com/purplemashu/me-cli
   cd me-cli
   bash setup.sh
   python main.py
   ```

2. **Dapatkan API Key:**
   - Chat bot Telegram: [@fykxt_bot](https://t.me/fykxt_bot)
   - Kirim command: `/viewkey`
   - Copy API key yang diberikan

3. **Login ke me-cli:**
   - Jalankan: `python main.py`
   - Masukkan API key
   - Login dengan nomor XL Anda (format: 6281234567890)

4. **Dapatkan Family Codes:**
   - Pilih menu: **12** (Store Family List)
   - Pilih enterprise atau tidak
   - **Selesai!** Anda akan melihat daftar semua family codes yang tersedia

5. **Gunakan Family Code untuk Beli Paket:**
   - Menu **6**: Lihat paket dalam family tertentu
   - Menu **7**: Beli semua paket dalam family tertentu

## Menggunakan Script Python

Script `get_family_codes.py` dapat digunakan untuk mendapatkan family codes secara langsung:

```bash
python get_family_codes.py
```

Script akan meminta:
- API Key (dari @fykxt_bot)
- ID Token (dapat dari me-cli setelah login)
- Tipe subscriber (PREPAID/POSTPAID)
- Enterprise atau tidak

## Analisis MyXL APK (Opsional)

Jika ingin menganalisis MyXL APK untuk menemukan family codes:

```bash
# 1. Download MyXL APK dari apkpure.com atau Play Store
# 2. Jalankan script analisis
bash analyze_myxl_apk.sh
```

Script akan:
- Extract APK
- Mencari pattern family codes
- Menampilkan API endpoints yang digunakan
- Memberikan hints untuk pencarian lebih lanjut

## API Endpoints yang Digunakan

### 1. Get Family List
```
POST {BASE_API_URL}/api/v8/xl-stores/options/search/family-list

Headers:
- x-api-key: {API_KEY}
- Authorization: Bearer {ID_TOKEN}
- Content-Type: application/json

Body:
{
    "is_enterprise": false,
    "subs_type": "PREPAID",
    "lang": "en"
}
```

### 2. Get Packages by Family Code
```
POST {BASE_API_URL}/api/v8/xl-stores/options/list

Headers:
- x-api-key: {API_KEY}
- Authorization: Bearer {ID_TOKEN}
- Content-Type: application/json

Body:
{
    "package_family_code": "{FAMILY_CODE}",
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

**Catatan:** `BASE_API_URL` biasanya di-set via environment variable saat menjalankan me-cli. Untuk mengetahui URL yang tepat, cek file `.env` atau environment variables di me-cli.

## Contoh Flow Pembelian Paket

1. **Dapatkan Family Code:**
   ```
   Menu: 12 ? Store Family List
   Copy family code dari daftar yang muncul
   ```

2. **Lihat Paket dalam Family:**
   ```
   Menu: 6 ? Beli Paket Berdasarkan Family Code
   Masukkan family code
   Pilih paket yang ingin dibeli
   ```

3. **Beli Paket:**
   ```
   Menu: 7 ? Beli Semua Paket di Family Code
   Masukkan family code
   Konfigurasi pembelian (decoy, delay, dll)
   ```

## Troubleshooting

### Family Code tidak ditemukan
- Pastikan tipe subscriber benar (PREPAID/POSTPAID)
- Cek apakah enterprise atau tidak
- Pastikan API key dan ID token masih valid

### Gagal mengambil family list
- Pastikan sudah login dengan benar
- Cek koneksi internet
- Refresh token jika perlu (logout dan login lagi)

### Paket tidak muncul untuk family code tertentu
- Family code mungkin spesifik untuk tipe subscriber tertentu
- Coba dengan kombinasi berbeda (enterprise/non-enterprise)
- Cek migration_type jika perlu

## File-file Penting

- `XL_FAMILY_CODES_RESEARCH.md` - Dokumentasi lengkap tentang family codes
- `get_family_codes.py` - Script Python untuk mendapatkan family codes
- `analyze_myxl_apk.sh` - Script bash untuk analisis MyXL APK
- `me-cli-research/` - Repository me-cli yang sudah di-clone untuk referensi

## Referensi

- Repository me-cli: https://github.com/purplemashu/me-cli
- Bot Telegram untuk API Key: [@fykxt_bot](https://t.me/fykxt_bot)
- MyXL App: Tersedia di Play Store

## Catatan Penting

?? **Family codes dapat berubah** - Selalu ambil daftar terbaru dari API sebelum menggunakan untuk pembelian.

?? **Butuh API Key** - Untuk menggunakan me-cli atau script, Anda perlu API key dari bot Telegram.

?? **Gunakan dengan bijak** - Pastikan Anda memahami risiko dan syarat penggunaan sebelum membeli paket secara otomatis.
