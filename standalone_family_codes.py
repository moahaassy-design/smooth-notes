#!/usr/bin/env python3
"""
Script Standalone untuk Login dan Mendapatkan Family Codes XL
Jalankan script ini di komputer Anda yang memiliki akses internet ke XL
"""

import sys
import os
import json
import requests

# Konfigurasi
API_KEY = "245d2532-64c7-42ec-b4de-52f1e8cb4023"
PHONE_NUMBER = "087864020187"  # Akan dikonversi ke 6287864020187
BASE_API_URL = "https://api.xl.co.id"
BASE_CIAM_URL = "https://ciam.xl.co.id"

def convert_phone(phone):
    """Convert phone to 628 format"""
    phone = phone.strip().replace('-', '').replace(' ', '')
    if phone.startswith('0'):
        phone = '62' + phone[1:]
    if not phone.startswith('628'):
        if phone.startswith('62'):
            phone = '62' + '8' + phone[2:]
        else:
            phone = '628' + phone
    return phone

def request_otp(phone):
    """Request OTP dari XL"""
    url = f"{BASE_CIAM_URL}/realms/xl-ciam/auth/otp"
    
    params = {
        "contact": phone,
        "contactType": "SMS",
        "alternateContact": "false"
    }
    
    headers = {
        "User-Agent": "okhttp/4.9.0",
        "Accept-Encoding": "gzip, deflate, br"
    }
    
    print(f"?? Meminta OTP ke {phone}...")
    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)
        print(f"Response status: {response.status_code}")
        print(f"Response: {response.text[:200]}")
        
        if response.status_code == 200:
            data = response.json()
            if "subscriber_id" in data:
                print("? OTP berhasil dikirim!")
                return data.get("subscriber_id")
            else:
                print(f"? Error: {data}")
        else:
            print(f"? HTTP {response.status_code}: {response.text[:200]}")
    except Exception as e:
        print(f"? Error: {e}")
    
    return None

def main():
    print("=" * 60)
    print("XL Family Codes Finder - Standalone")
    print("=" * 60)
    print()
    
    formatted_phone = convert_phone(PHONE_NUMBER)
    print(f"?? Nomor: {formatted_phone}")
    print(f"?? API Key: {API_KEY[:20]}...")
    print()
    
    # Test koneksi
    print("?? Testing koneksi...")
    try:
        test_resp = requests.get(f"{BASE_CIAM_URL}/realms/xl-ciam", timeout=5)
        print(f"? Koneksi OK (Status: {test_resp.status_code})")
    except Exception as e:
        print(f"? Koneksi gagal: {e}")
        print()
        print("??  Pastikan komputer Anda bisa mengakses ciam.xl.co.id")
        print("   Coba: ping ciam.xl.co.id atau curl https://ciam.xl.co.id")
        return
    
    print()
    
    # Request OTP
    subscriber_id = request_otp(formatted_phone)
    if not subscriber_id:
        print("\n? Gagal meminta OTP. Coba lagi nanti.")
        return
    
    print()
    print("=" * 60)
    print("Masukkan OTP yang diterima via SMS")
    print("=" * 60)
    
    # Get OTP from user
    max_tries = 5
    for attempt in range(max_tries):
        remaining = max_tries - attempt
        print(f"\n? Sisa percobaan: {remaining}")
        otp_code = input("Masukkan OTP (6 digit): ").strip()
        
        if not otp_code.isdigit() or len(otp_code) != 6:
            print("? OTP harus 6 digit angka!")
            continue
        
        print("?? Memverifikasi OTP...")
        # TODO: Implement submit_otp
        print("??  Submit OTP belum diimplementasikan di script standalone ini")
        print("   Gunakan me-cli untuk login lengkap:")
        print("   cd me-cli-research && python main.py")
        break
    
    print()
    print("=" * 60)
    print("Script selesai")
    print("=" * 60)
    print()
    print("?? Untuk mendapatkan family codes lengkap:")
    print("   1. Gunakan me-cli: cd me-cli-research && python main.py")
    print("   2. Login dengan nomor dan OTP")
    print("   3. Pilih menu 12 ? Store Family List")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n? Dibatalkan")
        sys.exit(0)
    except Exception as e:
        print(f"\n? Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
