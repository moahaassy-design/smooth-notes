# Cara Menjalankan Script untuk Mendapatkan Family Codes

## Status Script
? Script sudah dibuat dan siap digunakan
? API key sudah terverifikasi: `245d2532-64c7-42ec-b4de-52f1e8cb4023`
? Nomor sudah dikonfigurasi: `6287864020187`
? File konfigurasi sudah siap

## ?? Catatan Penting

Environment remote ini **tidak bisa mengakses domain XL** (`ciam.xl.co.id`) karena masalah DNS/koneksi. 

**Script perlu dijalankan di komputer Anda sendiri** yang memiliki akses internet ke domain XL.

## Cara Menjalankan

### Opsi 1: Menggunakan Script yang Sudah Dibuat

```bash
cd /workspace
python3 -B login_and_get_codes.py
```

Script akan:
1. ? Memverifikasi API key
2. ?? Meminta OTP ke nomor 6287864020187
3. ? Menunggu Anda memasukkan OTP
4. ?? Mengambil semua family codes (PREPAID/POSTPAID, Enterprise/Non-Enterprise)
5. ?? Menyimpan hasil ke `xl_family_codes.json`

### Opsi 2: Menggunakan me-cli Langsung (Disarankan)

```bash
cd /workspace/me-cli-research
python main.py
```

Lalu:
1. API key sudah tersimpan (otomatis terdeteksi)
2. Login dengan nomor: `6287864020187`
3. Masukkan OTP yang diterima
4. Pilih menu **12** ? Store Family List
5. Family codes akan muncul

### Opsi 3: Menggunakan Script Standalone

```bash
cd /workspace
python3 standalone_family_codes.py
```

## File-file yang Sudah Disiapkan

1. ? `login_and_get_codes.py` - Script utama (menggunakan me-cli)
2. ? `standalone_family_codes.py` - Script standalone sederhana
3. ? `me-cli-research/.env` - Konfigurasi environment
4. ? `me-cli-research/api.key` - File API key
5. ? `me-cli-research/api-key.txt` - Backup API key

## Troubleshooting

### Jika ada error "Cannot resolve host"
- Pastikan komputer Anda bisa mengakses internet
- Coba: `ping ciam.xl.co.id` atau `curl https://ciam.xl.co.id`
- Jika tidak bisa, gunakan VPN atau koneksi internet yang berbeda

### Jika OTP tidak datang
- Pastikan nomor aktif dan bisa menerima SMS
- Cek apakah ada SMS dari XL
- Coba request OTP lagi setelah beberapa menit

### Jika API key invalid
- Pastikan API key masih valid
- Cek di bot Telegram @fykxt_bot dengan command `/viewkey`

## Hasil yang Diharapkan

Setelah berhasil login, script akan:
- Menampilkan semua family codes yang tersedia
- Menyimpan ke file JSON dengan format:
  ```json
  {
    "phone_number": "6287864020187",
    "family_codes": [
      {
        "id": "FAMILY_CODE_1",
        "label": "Nama Family",
        "_subs_type": "PREPAID",
        "_is_enterprise": false
      },
      ...
    ]
  }
  ```

## Langkah Selanjutnya

Setelah mendapatkan family codes:
1. Copy family code yang diinginkan
2. Gunakan di me-cli dengan menu 6 atau 7
3. Atau gunakan langsung untuk pembelian paket

---

**Script sudah siap! Silakan jalankan di komputer Anda yang memiliki akses internet ke XL.**
