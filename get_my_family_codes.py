#!/usr/bin/env python3
"""
Script untuk login ke MyXL dan mendapatkan Family Codes
"""

import sys
import os
import json

# Setup path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'me-cli-research'))

# Set environment variables (diperlukan oleh me-cli)
os.environ['BASE_API_URL'] = os.getenv('BASE_API_URL', 'https://api.xl.co.id')
os.environ['BASE_CIAM_URL'] = os.getenv('BASE_CIAM_URL', 'https://ciam.xl.co.id')
os.environ['BASIC_AUTH'] = os.getenv('BASIC_AUTH', '')
os.environ['UA'] = os.getenv('UA', 'okhttp/4.9.0')

try:
    from app.client.engsel import get_otp, submit_otp
    from app.client.store.search import get_family_list
    from app.client.engsel import get_family
    from app.service.auth import AuthInstance
except ImportError as e:
    print(f"? Import error: {e}")
    print("   Pastikan me-cli sudah terinstall dengan benar")
    sys.exit(1)

def convert_phone_number(phone):
    """Convert phone number to 628 format"""
    phone = phone.strip().replace('-', '').replace(' ', '')
    
    # Jika mulai dengan 0, ganti dengan 62
    if phone.startswith('0'):
        phone = '62' + phone[1:]
    
    # Jika mulai dengan 62, pastikan tidak ada 0 setelahnya
    if phone.startswith('62') and len(phone) > 2:
        if phone[2] == '0':
            phone = '62' + phone[3:]
    
    # Pastikan mulai dengan 628
    if not phone.startswith('628'):
        if phone.startswith('62'):
            phone = '62' + '8' + phone[2:]
        else:
            phone = '628' + phone
    
    return phone

def login_and_get_family_codes(api_key, phone_number):
    """Login dan mendapatkan family codes"""
    
    print("=" * 60)
    print("XL Family Codes Finder")
    print("=" * 60)
    print()
    
    # Set API key
    AuthInstance.api_key = api_key
    
    # Convert phone number
    formatted_phone = convert_phone_number(phone_number)
    print(f"?? Nomor: {formatted_phone}")
    print()
    
    # Request OTP
    print("?? Meminta OTP...")
    subscriber_id = get_otp(formatted_phone)
    
    if not subscriber_id:
        print("? Gagal meminta OTP!")
        return None
    
    print("? OTP berhasil dikirim!")
    print()
    
    # Get OTP from user
    max_tries = 5
    tokens = None
    
    for attempt in range(max_tries):
        remaining = max_tries - attempt
        print(f"? Sisa percobaan: {remaining}")
        otp_code = input("Masukkan OTP (6 digit): ").strip()
        
        if not otp_code.isdigit() or len(otp_code) != 6:
            print("? OTP harus 6 digit angka!")
            continue
        
        print("?? Memverifikasi OTP...")
        tokens = submit_otp(api_key, formatted_phone, otp_code)
        
        if tokens:
            print("? Login berhasil!")
            break
        else:
            print("? OTP salah, silakan coba lagi")
    
    if not tokens:
        print("? Gagal login setelah beberapa percobaan")
        return None
    
    # Save tokens
    AuthInstance.add_refresh_token(int(formatted_phone), tokens.get("refresh_token"))
    AuthInstance.load_tokens()
    
    # Get user info
    active_user = AuthInstance.get_active_user()
    if active_user:
        print(f"? User: {active_user.get('number', 'N/A')}")
        print(f"   Tipe: {active_user.get('subscription_type', 'N/A')}")
    
    print()
    print("=" * 60)
    print("Mengambil Family Codes...")
    print("=" * 60)
    
    # Get family codes for different combinations
    results_all = []
    
    combinations = [
        ("PREPAID", False),
        ("PREPAID", True),
        ("POSTPAID", False),
        ("POSTPAID", True),
    ]
    
    for subs_type, is_enterprise in combinations:
        print(f"\n?? Mencari untuk: {subs_type}, Enterprise: {is_enterprise}")
        
        family_list_res = get_family_list(api_key, tokens, subs_type, is_enterprise)
        
        if family_list_res and family_list_res.get("status") == "SUCCESS":
            results = family_list_res.get("data", {}).get("results", [])
            if results:
                print(f"   ? Ditemukan {len(results)} family codes")
                for family in results:
                    family["_subs_type"] = subs_type
                    family["_is_enterprise"] = is_enterprise
                    results_all.append(family)
            else:
                print(f"   ??  Tidak ada family codes")
        else:
            print(f"   ? Gagal mengambil")
    
    # Display results
    print()
    print("=" * 60)
    print(f"DAFTAR FAMILY CODES XL ({len(results_all)} total)")
    print("=" * 60)
    print()
    
    if not results_all:
        print("? Tidak ada family codes ditemukan!")
        print("   Coba dengan kombinasi berbeda atau cek koneksi")
        return None
    
    # Group by name to avoid duplicates
    seen_codes = {}
    for idx, family in enumerate(results_all, 1):
        family_code = family.get("id", "N/A")
        family_name = family.get("label", "N/A")
        subs_type = family.get("_subs_type", "")
        is_enterprise = family.get("_is_enterprise", False)
        
        key = f"{family_code}_{subs_type}_{is_enterprise}"
        if key not in seen_codes:
            seen_codes[key] = True
            print(f"{idx:3d}. {family_name}")
            print(f"     Code: {family_code}")
            print(f"     Type: {subs_type}, Enterprise: {is_enterprise}")
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
    
    return results_all

if __name__ == "__main__":
    # API key dari user
    api_key = "245d2532-64c7-42ec-b4de-52f1e8cb4023"
    phone_number = "087864020187"
    
    try:
        results = login_and_get_family_codes(api_key, phone_number)
        if results:
            print("? Selesai! Family codes berhasil diambil.")
        else:
            print("? Gagal mengambil family codes")
    except KeyboardInterrupt:
        print("\n\n? Dibatalkan oleh user")
        sys.exit(0)
    except Exception as e:
        print(f"\n? Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
