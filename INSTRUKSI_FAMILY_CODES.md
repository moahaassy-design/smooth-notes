# Panduan Mendapatkan Family Codes dengan Nomor Anda

## Informasi:
- API Key: 245d2532-64c7-42ec-b4de-52f1e8cb4023  
- Nomor: 087864020187 ? format: 6287864020187

## Cara Termudah:

Karena Anda sudah tahu cara menggunakan me-cli, berikut langkah cepatnya:

### Langkah 1: Setup Environment Variables

Buat file `.env` di folder `me-cli-research/`:

```bash
cd /workspace/me-cli-research
cat > .env << 'EOF'
API_KEY=245d2532-64c7-42ec-b4de-52f1e8cb4023
BASE_API_URL=https://api.xl.co.id
BASE_CIAM_URL=https://ciam.xl.co.id
BASIC_AUTH=
AX_DEVICE_ID=
AX_FP=
UA=okhttp/4.9.0
AES_KEY_ASCII=
AX_FP_KEY=
EOF
```

### Langkah 2: Jalankan me-cli dan Login

```bash
cd /workspace/me-cli-research
python main.py
```

Ketika diminta:
1. Masukkan API key: `245d2532-64c7-42ec-b4de-52f1e8cb4023`
2. Login dengan nomor: `6287864020187`
3. Masukkan OTP yang Anda terima

### Langkah 3: Dapatkan Family Codes

Setelah login:
- Pilih menu: **12** (Store Family List)
- Pilih tipe subscriber (PREPAID/POSTPAID)
- Pilih enterprise (y/n)
- Family codes akan muncul

### Langkah 4: Gunakan Family Code

- Menu **6**: Lihat paket dalam family tertentu
- Menu **7**: Beli semua paket dalam family tertentu

## Catatan:

Jika ada error tentang environment variables yang kurang, Anda mungkin perlu mendapatkan nilai-nilai tersebut dari bot Telegram @fykxt_bot atau dari dokumentasi me-cli.

Apakah Anda ingin saya membantu setup file .env atau menjalankan me-cli sekarang?
