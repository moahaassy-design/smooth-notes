#!/usr/bin/env python3
"""
Script untuk mendapatkan Family Codes XL dari API
Dapat digunakan untuk menemukan family codes yang tersedia untuk pembelian paket melalui me-cli
"""

import requests
import json
from typing import Optional, List, Dict

# Base URL API XL (dari analisis me-cli)
BASE_API_URL = "https://api.xl.co.id"

def get_family_list(
    api_key: str,
    id_token: str,
    subs_type: str = "PREPAID",
    is_enterprise: bool = False
) -> Optional[Dict]:
    """
    Mengambil daftar family codes dari API XL
    
    Args:
        api_key: API key dari @fykxt_bot
        id_token: ID token dari login MyXL
        subs_type: "PREPAID" atau "POSTPAID"
        is_enterprise: True untuk enterprise, False untuk consumer
    
    Returns:
        Dictionary dengan daftar family codes atau None jika error
    """
    url = f"{BASE_API_URL}/api/v8/xl-stores/options/search/family-list"
    
    headers = {
        "x-api-key": api_key,
        "Authorization": f"Bearer {id_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "is_enterprise": is_enterprise,
        "subs_type": subs_type,
        "lang": "en"
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching family list: {e}")
        return None

def get_packages_by_family_code(
    api_key: str,
    id_token: str,
    family_code: str,
    is_enterprise: bool = False
) -> Optional[Dict]:
    """
    Mengambil detail paket berdasarkan family code
    
    Args:
        api_key: API key dari @fykxt_bot
        id_token: ID token dari login MyXL
        family_code: Kode family yang ingin dicari
        is_enterprise: True untuk enterprise, False untuk consumer
    
    Returns:
        Dictionary dengan detail paket dalam family atau None jika error
    """
    url = f"{BASE_API_URL}/api/v8/xl-stores/options/list"
    
    headers = {
        "x-api-key": api_key,
        "Authorization": f"Bearer {id_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "is_show_tagging_tab": True,
        "is_dedicated_event": True,
        "is_transaction_routine": False,
        "migration_type": "NONE",
        "package_family_code": family_code,
        "is_autobuy": False,
        "is_enterprise": is_enterprise,
        "is_pdlp": True,
        "referral_code": "",
        "is_migration": False,
        "lang": "en"
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching packages for family {family_code}: {e}")
        return None

def display_family_codes(family_list_response: Dict):
    """
    Menampilkan daftar family codes dengan format yang mudah dibaca
    """
    if not family_list_response or family_list_response.get("status") != "SUCCESS":
        print("Failed to get family list")
        return
    
    results = family_list_response.get("data", {}).get("results", [])
    
    if not results:
        print("No family codes found")
        return
    
    print("\n" + "=" * 60)
    print("DAFTAR FAMILY CODES XL")
    print("=" * 60)
    
    for idx, family in enumerate(results, 1):
        family_code = family.get("id", "N/A")
        family_name = family.get("label", "N/A")
        print(f"\n{idx}. {family_name}")
        print(f"   Family Code: {family_code}")
        print("-" * 60)
    
    print(f"\nTotal: {len(results)} family codes")

def save_family_codes_to_file(family_list_response: Dict, filename: str = "xl_family_codes.json"):
    """
    Menyimpan daftar family codes ke file JSON
    """
    if not family_list_response or family_list_response.get("status") != "SUCCESS":
        print("Failed to get family list")
        return
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(family_list_response, f, indent=2, ensure_ascii=False)
    
    print(f"\nFamily codes saved to {filename}")

def main():
    """
    Main function untuk menjalankan script
    """
    print("=" * 60)
    print("XL Family Codes Extractor")
    print("=" * 60)
    print("\nScript ini memerlukan:")
    print("1. API Key dari @fykxt_bot (command: /viewkey)")
    print("2. ID Token dari login MyXL (dapat dari me-cli setelah login)")
    print("\n" + "=" * 60)
    
    # Input dari user
    api_key = input("\nMasukkan API Key: ").strip()
    if not api_key:
        print("API Key tidak boleh kosong!")
        return
    
    id_token = input("Masukkan ID Token: ").strip()
    if not id_token:
        print("ID Token tidak boleh kosong!")
        return
    
    print("\nPilih tipe subscriber:")
    print("1. PREPAID")
    print("2. POSTPAID")
    subs_choice = input("Pilihan (1/2): ").strip()
    subs_type = "POSTPAID" if subs_choice == "2" else "PREPAID"
    
    print("\nApakah enterprise?")
    is_enterprise_input = input("(y/n): ").strip().lower()
    is_enterprise = is_enterprise_input == "y"
    
    # Fetch family list
    print(f"\nMengambil daftar family codes...")
    print(f"Subs Type: {subs_type}, Enterprise: {is_enterprise}")
    
    family_list = get_family_list(api_key, id_token, subs_type, is_enterprise)
    
    if family_list:
        display_family_codes(family_list)
        
        # Tanya apakah ingin save ke file
        save_choice = input("\nSimpan ke file? (y/n): ").strip().lower()
        if save_choice == "y":
            filename = input("Nama file (default: xl_family_codes.json): ").strip()
            if not filename:
                filename = "xl_family_codes.json"
            save_family_codes_to_file(family_list, filename)
        
        # Tanya apakah ingin melihat detail paket dalam family tertentu
        detail_choice = input("\nLihat detail paket dalam family tertentu? (y/n): ").strip().lower()
        if detail_choice == "y":
            family_code = input("Masukkan Family Code: ").strip()
            if family_code:
                print(f"\nMengambil detail paket untuk family: {family_code}...")
                packages = get_packages_by_family_code(api_key, id_token, family_code, is_enterprise)
                if packages:
                    detail_filename = f"family_{family_code}_packages.json"
                    with open(detail_filename, "w", encoding="utf-8") as f:
                        json.dump(packages, f, indent=2, ensure_ascii=False)
                    print(f"Detail paket disimpan ke {detail_filename}")
                    print("\nStruktur paket:")
                    print(json.dumps(packages, indent=2)[:500] + "...")

if __name__ == "__main__":
    main()
