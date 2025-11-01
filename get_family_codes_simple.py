#!/usr/bin/env python3
"""
Script helper untuk mendapatkan Family Codes setelah login di me-cli
Cara penggunaan:
1. Login dulu di me-cli: python me-cli-research/main.py
2. Setelah login, jalankan script ini
"""

import sys
import os
import json

# Setup path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'me-cli-research'))

# Load environment variables
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), 'me-cli-research', '.env'))

try:
    from app.client.store.search import get_family_list
    from app.service.auth import AuthInstance
except ImportError as e:
    print(f"? Import error: {e}")
    print("\nPastikan:")
    print("1. Sudah install dependencies: pip install -r me-cli-research/requirements.txt")
    print("2. Sudah login di me-cli terlebih dahulu")
    sys.exit(1)

def get_family_codes():
    """Get family codes dari me-cli yang sudah login"""
    
    print("=" * 60)
    print("XL Family Codes Finder")
    print("=" * 60)
    print()
    
    # Load tokens
    AuthInstance.load_tokens()
    active_user = AuthInstance.get_active_user()
    
    if not active_user:
        print("? Belum login ke me-cli!")
        print()
        print("Silakan login dulu:")
        print("1. Jalankan: python me-cli-research/main.py")
        print("2. Login dengan nomor XL Anda")
        print("3. Kemudian jalankan script ini lagi")
        return None
    
    print("? User ditemukan:")
    print(f"   Nomor: {active_user.get('number', 'N/A')}")
    print(f"   Tipe: {active_user.get('subscription_type', 'N/A')}")
    print()
    
    api_key = AuthInstance.api_key
    tokens = active_user.get("tokens", {})
    
    if not api_key:
        print("? API Key tidak ditemukan!")
        print("   Pastikan sudah setup me-cli dengan benar")
        return None
    
    if not tokens.get("id_token"):
        print("? ID Token tidak ditemukan!")
        print("   Silakan login ulang di me-cli")
        return None
    
    # Get subscription type
    default_subs = active_user.get('subscription_type', 'PREPAID')
    
    print("Mengambil family codes untuk kombinasi:")
    print(f"  - PREPAID, Non-Enterprise")
    print(f"  - PREPAID, Enterprise")
    print(f"  - POSTPAID, Non-Enterprise")
    print(f"  - POSTPAID, Enterprise")
    print()
    
    results_all = []
    combinations = [
        ("PREPAID", False, "PREPAID - Non-Enterprise"),
        ("PREPAID", True, "PREPAID - Enterprise"),
        ("POSTPAID", False, "POSTPAID - Non-Enterprise"),
        ("POSTPAID", True, "POSTPAID - Enterprise"),
    ]
    
    for subs_type, is_enterprise, label in combinations:
        print(f"?? {label}...", end=" ")
        
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
    
    print()
    print("=" * 60)
    print(f"DAFTAR FAMILY CODES XL ({len(results_all)} total)")
    print("=" * 60)
    print()
    
    if not results_all:
        print("? Tidak ada family codes ditemukan!")
        return None
    
    # Display results
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
        "phone_number": str(active_user.get('number', '')),
        "subscription_type": active_user.get('subscription_type', ''),
        "family_codes": results_all
    }
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print("=" * 60)
    print(f"? Family codes disimpan ke: {filename}")
    print()
    print("?? Tips:")
    print("   - Gunakan family code dengan menu 6 atau 7 di me-cli")
    print("   - Pastikan tipe subscriber sesuai (PREPAID/POSTPAID)")
    print("   - Pastikan enterprise/non-enterprise sesuai")
    
    return results_all

if __name__ == "__main__":
    try:
        results = get_family_codes()
        if results:
            print("\n? Selesai!")
        else:
            print("\n? Gagal mengambil family codes")
    except KeyboardInterrupt:
        print("\n\n? Dibatalkan")
        sys.exit(0)
    except Exception as e:
        print(f"\n? Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
