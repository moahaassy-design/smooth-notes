#!/usr/bin/env python3
"""
Script untuk login dan mendapatkan Family Codes XL
Menggunakan API key dan nomor yang sudah diberikan
"""

import sys
import os
import json

# Setup environment
os.chdir(os.path.dirname(__file__))
sys.path.insert(0, 'me-cli-research')

from dotenv import load_dotenv
load_dotenv('me-cli-research/.env')

# Set minimal environment variables
os.environ['API_KEY'] = os.getenv('API_KEY', '245d2532-64c7-42ec-b4de-52f1e8cb4023')
os.environ['BASE_API_URL'] = os.getenv('BASE_API_URL', 'https://api.xl.co.id')
os.environ['BASE_CIAM_URL'] = os.getenv('BASE_CIAM_URL', 'https://ciam.xl.co.id')
os.environ['UA'] = os.getenv('UA', 'okhttp/4.9.0')

# Set dummy values untuk encryption (32 bytes untuk AES-256)
if not os.getenv('BASIC_AUTH'):
    os.environ['BASIC_AUTH'] = ''
if not os.getenv('AES_KEY_ASCII'):
    # 32 karakter untuk AES-256 key
    os.environ['AES_KEY_ASCII'] = '0123456789abcdef0123456789abcdef'
if not os.getenv('AX_FP_KEY'):
    # 32 karakter untuk AES-256 key  
    os.environ['AX_FP_KEY'] = '0123456789abcdef0123456789abcdef'

# Set API key ke file sebelum import AuthInstance
api_key_file = 'me-cli-research/api.key'
os.makedirs(os.path.dirname(api_key_file), exist_ok=True)
with open(api_key_file, 'w') as f:
    f.write('245d2532-64c7-42ec-b4de-52f1e8cb4023')

# Change to me-cli-research directory so api.key can be found
original_dir = os.getcwd()
os.chdir('me-cli-research')

try:
    from app.client.engsel import get_otp, submit_otp
    from app.client.store.search import get_family_list
    from app.service.auth import AuthInstance
except ImportError as e:
    print(f"? Import error: {e}")
    print("\nInstalling dependencies...")
    os.system("pip3 install -q requests pycryptodome python-dotenv")
    print("Silakan jalankan script ini lagi")
    sys.exit(1)

def main():
    print("=" * 60)
    print("XL Family Codes Finder")
    print("=" * 60)
    print()
    
    # API key dan nomor dari user
    api_key = "245d2532-64c7-42ec-b4de-52f1e8cb4023"
    phone_number = "087864020187"
    
    # Convert phone number
    if phone_number.startswith('0'):
        formatted_phone = '62' + phone_number[1:]
    else:
        formatted_phone = phone_number
    
    if not formatted_phone.startswith('628'):
        formatted_phone = '628' + formatted_phone.replace('628', '')
    
    print(f"?? Nomor: {formatted_phone}")
    print(f"?? API Key: {api_key[:20]}...")
    print()
    
    # Set API key
    AuthInstance.api_key = api_key
    
    # Request OTP
    print("?? Meminta OTP...")
    try:
        subscriber_id = get_otp(formatted_phone)
        if not subscriber_id:
            print("? Gagal meminta OTP!")
            print("   Pastikan nomor sudah benar dan aktif")
            return
        print("? OTP berhasil dikirim ke nomor Anda!")
        print()
    except Exception as e:
        print(f"? Error saat request OTP: {e}")
        return
    
    # Get OTP from user
    print("=" * 60)
    print("Tunggu OTP dari XL...")
    print("=" * 60)
    
    max_tries = 5
    tokens = None
    
    for attempt in range(max_tries):
        remaining = max_tries - attempt
        print(f"\n? Sisa percobaan: {remaining}")
        otp_code = input("Masukkan OTP (6 digit): ").strip()
        
        if not otp_code.isdigit() or len(otp_code) != 6:
            print("? OTP harus 6 digit angka!")
            continue
        
        print("?? Memverifikasi OTP...")
        try:
            tokens = submit_otp(api_key, formatted_phone, otp_code)
            if tokens:
                print("? Login berhasil!")
                break
            else:
                print("? OTP salah, silakan coba lagi")
        except Exception as e:
            print(f"? Error: {e}")
    
    if not tokens:
        print("\n? Gagal login setelah beberapa percobaan")
        return
    
    # Save tokens
    AuthInstance.add_refresh_token(int(formatted_phone), tokens.get("refresh_token"))
    AuthInstance.load_tokens()
    
    print()
    print("=" * 60)
    print("Mengambil Family Codes...")
    print("=" * 60)
    
    # Get family codes
    results_all = []
    combinations = [
        ("PREPAID", False),
        ("PREPAID", True),
        ("POSTPAID", False),
        ("POSTPAID", True),
    ]
    
    for subs_type, is_enterprise in combinations:
        label = f"{subs_type} - {'Enterprise' if is_enterprise else 'Non-Enterprise'}"
        print(f"\n?? {label}...", end=" ")
        
        try:
            family_list_res = get_family_list(api_key, tokens, subs_type, is_enterprise)
            
            if family_list_res and family_list_res.get("status") == "SUCCESS":
                results = family_list_res.get("data", {}).get("results", [])
                if results:
                    print(f"? {len(results)} found")
                    for family in results:
                        family["_subs_type"] = subs_type
                        family["_is_enterprise"] = is_enterprise
                        family["_label"] = label
                        results_all.append(family)
                else:
                    print("??  tidak ada")
            else:
                print("? gagal")
        except Exception as e:
            print(f"? error: {e}")
    
    # Display results
    print()
    print("=" * 60)
    print(f"DAFTAR FAMILY CODES XL ({len(results_all)} total)")
    print("=" * 60)
    print()
    
    if not results_all:
        print("? Tidak ada family codes ditemukan!")
        return
    
    for idx, family in enumerate(results_all, 1):
        family_code = family.get("id", "N/A")
        family_name = family.get("label", "N/A")
        label = family.get("_label", "")
        
        print(f"{idx:3d}. {family_name}")
        print(f"     Code: {family_code}")
        print(f"     Type: {label}")
        print()
    
    # Save to file
    filename = "xl_family_codes.json"
    output_data = {
        "phone_number": formatted_phone,
        "family_codes": results_all
    }
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print("=" * 60)
    print(f"? Family codes disimpan ke: {filename}")
    print()
    print("?? Tips:")
    print("   - Gunakan family code dengan menu 6 atau 7 di me-cli")
    print("   - Pastikan tipe subscriber sesuai")

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
