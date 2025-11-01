#!/usr/bin/env python3
"""
Script untuk mendapatkan Family Codes XL
Menggunakan API yang sama dengan me-cli
"""

import sys
import os
import json

# Add me-cli to path if running from workspace
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'me-cli-research'))

try:
    from app.client.store.search import get_family_list
    from app.client.engsel import get_family
    from app.service.auth import AuthInstance
except ImportError:
    print("??  Import error. Pastikan me-cli sudah terinstall.")
    print("   Install dengan: cd me-cli-research && bash setup.sh")
    sys.exit(1)

def get_family_codes_interactive():
    """Fungsi interaktif untuk mendapatkan family codes"""
    
    print("=" * 60)
    print("XL Family Codes Finder")
    print("=" * 60)
    print()
    
    # Check if user is logged in to me-cli
    active_user = AuthInstance.get_active_user()
    
    if not active_user:
        print("? Belum login ke me-cli!")
        print()
        print("Silakan login dulu dengan me-cli:")
        print("1. Jalankan: python me-cli-research/main.py")
        print("2. Login dengan nomor XL Anda")
        print("3. Kemudian jalankan script ini lagi")
        print()
        print("ATAU gunakan metode langsung:")
        print("- Masukkan API key dan ID token manual di bawah")
        print()
        
        use_manual = input("Gunakan manual input? (y/n): ").strip().lower()
        if use_manual != 'y':
            return
        
        api_key = input("Masukkan API Key: ").strip()
        id_token = input("Masukkan ID Token: ").strip()
        
        if not api_key or not id_token:
            print("? API Key dan ID Token diperlukan!")
            return
        
        tokens = {"id_token": id_token}
    else:
        print("? Sudah login ke me-cli!")
        print(f"   Nomor: {active_user.get('number', 'N/A')}")
        print(f"   Tipe: {active_user.get('subscription_type', 'N/A')}")
        print()
        
        api_key = AuthInstance.api_key
        tokens = active_user.get("tokens", {})
        id_token = tokens.get("id_token")
        
        if not api_key or not id_token:
            print("? API Key atau ID Token tidak ditemukan!")
            print("   Silakan login ulang di me-cli")
            return
    
    # Get subscription type
    if active_user:
        default_subs = active_user.get('subscription_type', 'PREPAID')
    else:
        default_subs = 'PREPAID'
    
    print("\nPilih tipe subscriber:")
    print("1. PREPAID")
    print("2. POSTPAID")
    subs_choice = input(f"Pilihan (default: {default_subs}): ").strip()
    
    if subs_choice == '2':
        subs_type = 'POSTPAID'
    elif subs_choice == '1':
        subs_type = 'PREPAID'
    else:
        subs_type = default_subs
    
    # Get enterprise status
    print("\nApakah enterprise?")
    is_enterprise_input = input("(y/n, default: n): ").strip().lower()
    is_enterprise = is_enterprise_input == 'y'
    
    # Fetch family list
    print("\n" + "=" * 60)
    print(f"Mengambil daftar family codes...")
    print(f"Subs Type: {subs_type}")
    print(f"Enterprise: {is_enterprise}")
    print("=" * 60)
    print()
    
    family_list_res = get_family_list(api_key, tokens, subs_type, is_enterprise)
    
    if not family_list_res:
        print("? Gagal mengambil family list!")
        print("   Pastikan API key dan token masih valid")
        return
    
    if family_list_res.get("status") != "SUCCESS":
        print(f"? Error: {family_list_res.get('message', 'Unknown error')}")
        return
    
    results = family_list_res.get("data", {}).get("results", [])
    
    if not results:
        print("? Tidak ada family codes ditemukan!")
        print("   Coba dengan kombinasi berbeda (PREPAID/POSTPAID, Enterprise/Non-Enterprise)")
        return
    
    # Display family codes
    print("\n" + "=" * 60)
    print(f"DAFTAR FAMILY CODES XL ({len(results)} ditemukan)")
    print("=" * 60)
    print()
    
    for idx, family in enumerate(results, 1):
        family_code = family.get("id", "N/A")
        family_name = family.get("label", "N/A")
        
        print(f"{idx:3d}. {family_name}")
        print(f"     Family Code: {family_code}")
        print()
    
    print("=" * 60)
    
    # Ask to save
    save_choice = input("\nSimpan ke file? (y/n): ").strip().lower()
    if save_choice == 'y':
        filename = input("Nama file (default: xl_family_codes.json): ").strip()
        if not filename:
            filename = "xl_family_codes.json"
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(family_list_res, f, indent=2, ensure_ascii=False)
        
        print(f"? Disimpan ke {filename}")
    
    # Ask to view packages
    view_choice = input("\nLihat paket dalam family tertentu? (y/n): ").strip().lower()
    if view_choice == 'y':
        family_idx = input(f"Masukkan nomor family (1-{len(results)}): ").strip()
        try:
            idx = int(family_idx) - 1
            if 0 <= idx < len(results):
                selected_family = results[idx]
                family_code = selected_family.get("id")
                family_name = selected_family.get("label")
                
                print(f"\nMengambil paket untuk: {family_name} ({family_code})...")
                
                # Try different migration types
                migration_types = ["NONE", "PRE_TO_PRIOH", "PRIOH_TO_PRIO", "PRIO_TO_PRIOH"]
                
                for mt in migration_types:
                    print(f"  Mencoba migration_type: {mt}...")
                    family_data = get_family(api_key, tokens, family_code, is_enterprise, mt)
                    
                    if family_data:
                        family_name_found = family_data.get("package_family", {}).get("name", "")
                        if family_name_found:
                            print(f"  ? Berhasil dengan migration_type: {mt}")
                            print(f"  Family: {family_name_found}")
                            
                            variants = family_data.get("package_variants", [])
                            print(f"  Variants: {len(variants)}")
                            
                            total_options = sum(len(v.get("package_options", [])) for v in variants)
                            print(f"  Total Options: {total_options}")
                            
                            # Save package details
                            pkg_filename = f"family_{family_code}_packages.json"
                            with open(pkg_filename, "w", encoding="utf-8") as f:
                                json.dump(family_data, f, indent=2, ensure_ascii=False)
                            
                            print(f"  ? Detail paket disimpan ke {pkg_filename}")
                            break
                    else:
                        print(f"  ? Tidak berhasil")
            else:
                print("? Nomor tidak valid!")
        except ValueError:
            print("? Input tidak valid!")

if __name__ == "__main__":
    try:
        get_family_codes_interactive()
    except KeyboardInterrupt:
        print("\n\n? Dibatalkan oleh user")
        sys.exit(0)
    except Exception as e:
        print(f"\n? Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
