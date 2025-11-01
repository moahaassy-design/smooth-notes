#!/usr/bin/env python3
"""
Script untuk menganalisis MyXL APK dan mencari Family Codes
Mendukung berbagai metode analisis APK
"""

import sys
import os
import json
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def extract_apk(apk_path, output_dir):
    """Extract APK file"""
    print(f"?? Extracting APK: {apk_path}")
    try:
        with zipfile.ZipFile(apk_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        print(f"? APK extracted to: {output_dir}")
        return True
    except Exception as e:
        print(f"? Error extracting APK: {e}")
        return False

def search_in_strings_xml(extracted_dir):
    """Search for family codes in strings.xml"""
    print("\n" + "=" * 60)
    print("Metode 1: Mencari di strings.xml")
    print("=" * 60)
    
    results = []
    strings_files = list(Path(extracted_dir).rglob("strings.xml"))
    
    for strings_file in strings_files:
        print(f"\n?? Checking: {strings_file}")
        try:
            tree = ET.parse(strings_file)
            root = tree.getroot()
            
            for elem in root.iter():
                text = elem.text if elem.text else ""
                name = elem.get("name", "")
                
                # Cari pattern family code
                patterns = re.findall(r'([A-Z_]{5,})', text + " " + name)
                for pattern in patterns:
                    if any(keyword in pattern for keyword in ['FAMILY', 'TURBO', 'COMBO', 'FREEDOM']):
                        if pattern not in results:
                            results.append(pattern)
                            print(f"  ? Found: {pattern}")
        except Exception as e:
            print(f"  ? Error: {e}")
    
    return results

def search_in_assets(extracted_dir):
    """Search for family codes in assets folder"""
    print("\n" + "=" * 60)
    print("Metode 2: Mencari di Assets")
    print("=" * 60)
    
    results = []
    assets_dir = Path(extracted_dir) / "assets"
    
    if not assets_dir.exists():
        print("? Assets folder not found")
        return results
    
    print(f"?? Scanning assets folder...")
    
    # Cari file JSON, JS, atau config
    file_extensions = ['.json', '.js', '.txt', '.config', '.properties']
    
    for ext in file_extensions:
        for file_path in assets_dir.rglob(f"*{ext}"):
            print(f"\n?? Checking: {file_path.name}")
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                    # Cari pattern family code
                    patterns = re.findall(r'["\']([A-Z_]{5,})["\']', content)
                    patterns += re.findall(r'([A-Z_]{5,})', content)
                    
                    for pattern in patterns:
                        if any(keyword in pattern for keyword in ['FAMILY', 'TURBO', 'COMBO', 'FREEDOM', 'XL']):
                            if len(pattern) > 5 and pattern not in results:
                                results.append(pattern)
                                print(f"  ? Found: {pattern}")
            except Exception as e:
                pass
    
    return results

def search_in_smali(extracted_dir):
    """Search for family codes in Smali files (decompiled Java)"""
    print("\n" + "=" * 60)
    print("Metode 3: Mencari di Smali Files")
    print("=" * 60)
    
    results = []
    smali_dirs = list(Path(extracted_dir).rglob("smali*"))
    
    if not smali_dirs:
        print("??  Smali files not found. APK needs to be decompiled with apktool")
        print("   Run: apktool d myxl.apk")
        return results
    
    print(f"?? Found {len(smali_dirs)} smali directories")
    
    for smali_dir in smali_dirs[:3]:  # Limit untuk performa
        print(f"\n?? Scanning: {smali_dir.name}")
        for smali_file in list(smali_dir.rglob("*.smali"))[:50]:  # Limit files
            try:
                with open(smali_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                    # Cari string constants
                    patterns = re.findall(r'const-string.*?"([A-Z_]{5,})"', content)
                    for pattern in patterns:
                        if any(keyword in pattern for keyword in ['FAMILY', 'TURBO', 'COMBO', 'FREEDOM']):
                            if pattern not in results:
                                results.append(pattern)
                                print(f"  ? Found: {pattern}")
            except:
                pass
    
    return results

def search_in_resources(extracted_dir):
    """Search for family codes in resources"""
    print("\n" + "=" * 60)
    print("Metode 4: Mencari di Resources")
    print("=" * 60)
    
    results = []
    res_dir = Path(extracted_dir) / "res"
    
    if not res_dir.exists():
        print("? Resources folder not found")
        return results
    
    print(f"?? Scanning resources...")
    
    # Cari di berbagai file resources
    for resource_file in res_dir.rglob("*.xml"):
        try:
            with open(resource_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
                # Cari pattern
                patterns = re.findall(r'([A-Z_]{5,})', content)
                for pattern in patterns:
                    if any(keyword in pattern for keyword in ['FAMILY', 'TURBO', 'COMBO', 'FREEDOM']):
                        if pattern not in results:
                            results.append(pattern)
                            print(f"  ? Found: {pattern} in {resource_file.name}")
        except:
            pass
    
    return results

def search_api_endpoints(extracted_dir):
    """Search for API endpoints that might contain family codes"""
    print("\n" + "=" * 60)
    print("Metode 5: Mencari API Endpoints")
    print("=" * 60)
    
    endpoints = []
    
    # Cari di semua file
    for file_path in Path(extracted_dir).rglob("*"):
        if file_path.is_file():
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                    # Cari API URLs
                    url_patterns = re.findall(r'https?://[^"\s]+api[^"\s]+', content)
                    for url in url_patterns:
                        if 'xl' in url.lower() or 'family' in url.lower():
                            if url not in endpoints:
                                endpoints.append(url)
                                print(f"  ? Endpoint: {url}")
            except:
                pass
    
    return endpoints

def search_in_manifest(extracted_dir):
    """Search AndroidManifest.xml"""
    print("\n" + "=" * 60)
    print("Metode 6: Mencari di AndroidManifest.xml")
    print("=" * 60)
    
    results = []
    manifest_path = Path(extracted_dir) / "AndroidManifest.xml"
    
    if not manifest_path.exists():
        print("? AndroidManifest.xml not found")
        return results
    
    print(f"?? Reading AndroidManifest.xml...")
    try:
        # AndroidManifest.xml biasanya binary, perlu aapt atau axmlparser
        # Tapi kita coba baca sebagai text dulu
        with open(manifest_path, 'rb') as f:
            content = f.read()
            
        # Cari string patterns
        text_content = content.decode('utf-8', errors='ignore')
        patterns = re.findall(r'([A-Z_]{5,})', text_content)
        for pattern in patterns:
            if any(keyword in pattern for keyword in ['FAMILY', 'TURBO', 'COMBO', 'FREEDOM']):
                if pattern not in results:
                    results.append(pattern)
                    print(f"  ? Found: {pattern}")
    except Exception as e:
        print(f"  ??  Note: AndroidManifest.xml is binary, use 'apktool d' to decompile")
        print(f"     Error: {e}")
    
    return results

def main():
    print("=" * 60)
    print("MyXL APK Analyzer - Family Codes Finder")
    print("=" * 60)
    print()
    
    # Check if APK file exists
    apk_files = [
        "myxl.apk",
        "MyXL.apk",
        "MYXL.apk",
        "com.xl.app.apk",
    ]
    
    apk_path = None
    for apk_file in apk_files:
        if os.path.exists(apk_file):
            apk_path = apk_file
            break
    
    if not apk_path:
        print("? MyXL APK file not found!")
        print()
        print("?? Cara download MyXL APK:")
        print("   1. Kunjungi: https://apkpure.com/myxl/com.xl.app")
        print("   2. Download APK terbaru")
        print("   3. Simpan dengan nama: myxl.apk")
        print()
        print("   Atau dari Play Store menggunakan:")
        print("   - apkmirror.com")
        print("   - apkcombo.com")
        print()
        return
    
    print(f"? Found APK: {apk_path}")
    print(f"   Size: {os.path.getsize(apk_path) / 1024 / 1024:.2f} MB")
    print()
    
    # Extract APK
    extracted_dir = "myxl_extracted"
    if os.path.exists(extracted_dir):
        print(f"??  {extracted_dir} already exists. Using existing extraction.")
    else:
        if not extract_apk(apk_path, extracted_dir):
            return
    
    print()
    
    # Search in various locations
    all_results = []
    
    # Method 1: strings.xml
    results1 = search_in_strings_xml(extracted_dir)
    all_results.extend([{"code": r, "source": "strings.xml"} for r in results1])
    
    # Method 2: Assets
    results2 = search_in_assets(extracted_dir)
    all_results.extend([{"code": r, "source": "assets"} for r in results2])
    
    # Method 3: Smali
    results3 = search_in_smali(extracted_dir)
    all_results.extend([{"code": r, "source": "smali"} for r in results3])
    
    # Method 4: Resources
    results4 = search_in_resources(extracted_dir)
    all_results.extend([{"code": r, "source": "resources"} for r in results4])
    
    # Method 5: API Endpoints
    endpoints = search_api_endpoints(extracted_dir)
    
    # Method 6: Manifest
    results6 = search_in_manifest(extracted_dir)
    all_results.extend([{"code": r, "source": "manifest"} for r in results6])
    
    # Deduplicate
    seen = set()
    unique_results = []
    for item in all_results:
        code = item.get("code", "")
        if code and code not in seen:
            seen.add(code)
            unique_results.append(item)
    
    # Save results
    print("\n" + "=" * 60)
    print(f"TOTAL FAMILY CODES DITEMUKAN: {len(unique_results)}")
    print("=" * 60)
    
    output = {
        "apk_file": apk_path,
        "total_found": len(unique_results),
        "family_codes": unique_results,
        "api_endpoints": endpoints
    }
    
    filename = "xl_family_codes_from_apk.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n? Hasil disimpan ke: {filename}")
    
    if unique_results:
        print("\n?? Daftar Family Codes:")
        print()
        for idx, item in enumerate(unique_results, 1):
            code = item.get("code", "")
            source = item.get("source", "unknown")
            print(f"{idx:3d}. {code}")
            print(f"     Source: {source}")
            print()
    else:
        print("\n??  Tidak ada family codes ditemukan dalam APK")
        print("   Mungkin perlu:")
        print("   1. Decompile APK dengan apktool: apktool d myxl.apk")
        print("   2. Analisis lebih dalam dengan jadx atau jadx-gui")
        print("   3. Cek network traffic saat aplikasi berjalan")
    
    if endpoints:
        print("\n?? API Endpoints ditemukan:")
        for endpoint in endpoints[:10]:
            print(f"  - {endpoint}")
    
    print("\n" + "=" * 60)
    print("? Analisis selesai!")
    print("=" * 60)

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
