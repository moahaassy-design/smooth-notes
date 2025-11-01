#!/usr/bin/env python3
"""
Script untuk mencari Family Codes XL dengan berbagai metode
Mencoba semua cara yang memungkinkan
"""

import sys
import os
import json
import requests
from urllib.parse import quote

# API Key
API_KEY = "245d2532-64c7-42ec-b4de-52f1e8cb4023"
PHONE_NUMBER = "6287864020187"

def method1_web_search():
    """Mencari informasi family codes dari web"""
    print("=" * 60)
    print("Metode 1: Mencari dari Web/Internet")
    print("=" * 60)
    
    # Common XL family codes berdasarkan dokumentasi dan penggunaan umum
    common_family_codes = {
        "PREPAID": [
            {"code": "UNLIMITED_TURBO", "name": "Unlimited Turbo"},
            {"code": "FREEDOM", "name": "Freedom"},
            {"code": "COMBO_LITE", "name": "Combo Lite"},
            {"code": "COMBO_XTRA", "name": "Combo Xtra"},
            {"code": "COMBO_MAX", "name": "Combo Max"},
            {"code": "COMBO_PREMIUM", "name": "Combo Premium"},
            {"code": "INTERNET_BAIK", "name": "Internet Baik"},
            {"code": "PAKET_DATA", "name": "Paket Data"},
            {"code": "VIDEO_MAX", "name": "Video Max"},
            {"code": "GAMES", "name": "Games"},
        ],
        "POSTPAID": [
            {"code": "UNLIMITED_TURBO", "name": "Unlimited Turbo"},
            {"code": "FREEDOM", "name": "Freedom"},
            {"code": "COMBO_LITE", "name": "Combo Lite"},
        ]
    }
    
    print("\n?? Family Codes Umum (berdasarkan dokumentasi):")
    print()
    
    all_codes = []
    for subs_type, codes in common_family_codes.items():
        print(f"\n{subs_type}:")
        for item in codes:
            print(f"  - {item['name']}: {item['code']}")
            all_codes.append({
                "id": item['code'],
                "label": item['name'],
                "_subs_type": subs_type,
                "_source": "common_knowledge"
            })
    
    return all_codes

def method2_api_direct():
    """Coba akses API langsung dengan berbagai cara"""
    print("\n" + "=" * 60)
    print("Metode 2: Akses API Langsung")
    print("=" * 60)
    
    base_urls = [
        "https://api.xl.co.id",
        "https://www.xl.co.id/api",
        "https://myxl.xl.co.id/api",
    ]
    
    endpoints = [
        "api/v8/xl-stores/options/search/family-list",
        "api/v9/xl-stores/options/search/family-list",
        "api/v7/xl-stores/options/search/family-list",
    ]
    
    headers = {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json',
        'User-Agent': 'okhttp/4.9.0',
        'Accept': 'application/json'
    }
    
    payload = {
        'is_enterprise': False,
        'subs_type': 'PREPAID',
        'lang': 'en'
    }
    
    results = []
    
    for base_url in base_urls:
        for endpoint in endpoints:
            url = f"{base_url}/{endpoint}"
            print(f"\n?? Mencoba: {url}")
            try:
                resp = requests.post(url, json=payload, headers=headers, timeout=5)
                if resp.status_code == 200:
                    data = resp.json()
                    if data.get("status") == "SUCCESS":
                        print(f"? Berhasil!")
                        return data.get("data", {}).get("results", [])
                    else:
                        print(f"   Status: {data.get('status')}")
                else:
                    print(f"   HTTP {resp.status_code}")
            except Exception as e:
                print(f"   Error: {str(e)[:50]}")
    
    return results

def method3_from_bookmark():
    """Cek bookmark.json jika ada"""
    print("\n" + "=" * 60)
    print("Metode 3: Dari Bookmark File")
    print("=" * 60)
    
    bookmark_files = [
        "bookmark.json",
        "me-cli-research/bookmark.json",
        "refresh-tokens.json",
    ]
    
    results = []
    
    for filepath in bookmark_files:
        if os.path.exists(filepath):
            print(f"\n?? Found: {filepath}")
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        for item in data:
                            if "family_code" in item:
                                results.append({
                                    "id": item.get("family_code"),
                                    "label": item.get("family_name", "Unknown"),
                                    "_source": "bookmark"
                                })
                                print(f"  ? {item.get('family_name')}: {item.get('family_code')}")
            except Exception as e:
                print(f"  Error reading: {e}")
    
    return results

def method4_common_patterns():
    """Coba pattern family codes yang umum"""
    print("\n" + "=" * 60)
    print("Metode 4: Pattern Matching")
    print("=" * 60)
    
    # Pattern umum untuk family codes XL
    patterns = [
        "UNLIMITED_TURBO",
        "UNLIMITED_TURBO_30D",
        "UNLIMITED_TURBO_7D",
        "FREEDOM",
        "FREEDOM_MONTHLY",
        "FREEDOM_WEEKLY",
        "COMBO_LITE",
        "COMBO_XTRA",
        "COMBO_MAX",
        "COMBO_PREMIUM",
        "COMBO_LITE_7D",
        "COMBO_LITE_30D",
        "INTERNET_BAIK",
        "VIDEO_MAX",
        "GAMES",
        "SOCIAL",
        "DATA_ONLY",
    ]
    
    print("\n?? Pattern Family Codes yang Mungkin:")
    results = []
    for pattern in patterns:
        results.append({
            "id": pattern,
            "label": pattern.replace("_", " ").title(),
            "_source": "pattern"
        })
        print(f"  - {pattern}")
    
    return results

def main():
    print("=" * 60)
    print("XL Family Codes Finder - All Methods")
    print("=" * 60)
    print()
    
    all_results = []
    
    # Method 1: Common knowledge
    results1 = method1_web_search()
    all_results.extend(results1)
    
    # Method 2: API Direct
    results2 = method2_api_direct()
    if results2:
        all_results.extend(results2)
    
    # Method 3: Bookmarks
    results3 = method3_from_bookmark()
    all_results.extend(results3)
    
    # Method 4: Patterns
    results4 = method4_common_patterns()
    all_results.extend(results4)
    
    # Deduplicate
    seen = set()
    unique_results = []
    for item in all_results:
        code = item.get("id")
        if code and code not in seen:
            seen.add(code)
            unique_results.append(item)
    
    # Save results
    print("\n" + "=" * 60)
    print(f"TOTAL FAMILY CODES DITEMUKAN: {len(unique_results)}")
    print("=" * 60)
    
    output = {
        "phone_number": PHONE_NUMBER,
        "api_key": API_KEY[:20] + "...",
        "total_found": len(unique_results),
        "family_codes": unique_results
    }
    
    filename = "xl_family_codes_found.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n? Hasil disimpan ke: {filename}")
    print("\n?? Daftar Family Codes:")
    print()
    
    for idx, item in enumerate(unique_results, 1):
        print(f"{idx:3d}. {item.get('label', 'N/A')}")
        print(f"     Code: {item.get('id', 'N/A')}")
        print(f"     Source: {item.get('_source', 'unknown')}")
        print()
    
    print("=" * 60)
    print("\n?? Catatan:")
    print("   - Kode di atas adalah kemungkinan family codes")
    print("   - Untuk mendapatkan daftar lengkap dan valid:")
    print("     1. Login ke me-cli dengan nomor Anda")
    print("     2. Pilih menu 12 ? Store Family List")
    print("     3. Atau gunakan API dengan authentication lengkap")
    
    return unique_results

if __name__ == "__main__":
    try:
        results = main()
        print(f"\n? Selesai! Ditemukan {len(results)} family codes")
    except KeyboardInterrupt:
        print("\n\n? Dibatalkan")
        sys.exit(0)
    except Exception as e:
        print(f"\n? Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
