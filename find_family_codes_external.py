#!/usr/bin/env python3
"""
Script untuk mencari Family Codes XL dari sumber eksternal
- Web scraping
- GitHub repositories
- Dokumentasi publik
- API publik
"""

import sys
import os
import json
import requests
import re
from urllib.parse import quote, urljoin

def search_github():
    """Cari di GitHub repositories"""
    print("=" * 60)
    print("Metode 1: Mencari di GitHub")
    print("=" * 60)
    
    github_searches = [
        "xl family code",
        "xl package family",
        "me-cli xl",
        "xl api family",
        "xl prepaid package",
    ]
    
    results = []
    
    for query in github_searches:
        print(f"\n?? Mencari: {query}")
        try:
            url = f"https://api.github.com/search/repositories?q={quote(query)}&per_page=5"
            headers = {"Accept": "application/vnd.github.v3+json"}
            resp = requests.get(url, headers=headers, timeout=10)
            
            if resp.status_code == 200:
                data = resp.json()
                repos = data.get("items", [])
                print(f"   ? Ditemukan {len(repos)} repository")
                
                for repo in repos[:3]:
                    repo_name = repo.get("full_name", "")
                    print(f"   - {repo_name}")
                    
                    # Coba ambil file README atau code
                    try:
                        readme_url = f"https://raw.githubusercontent.com/{repo_name}/main/README.md"
                        readme_resp = requests.get(readme_url, timeout=5)
                        if readme_resp.status_code == 200:
                            content = readme_resp.text
                            # Cari pattern family code
                            patterns = re.findall(r'[A-Z_]{3,}', content)
                            for pattern in patterns:
                                if 'FAMILY' in pattern or 'TURBO' in pattern or 'COMBO' in pattern:
                                    if pattern not in results:
                                        results.append(pattern)
                                        print(f"     ?? Pattern: {pattern}")
                    except:
                        pass
            else:
                print(f"   ? HTTP {resp.status_code}")
        except Exception as e:
            print(f"   ? Error: {str(e)[:50]}")
    
    return results

def search_web_xl():
    """Coba scrape dari website XL"""
    print("\n" + "=" * 60)
    print("Metode 2: Mencari di Website XL")
    print("=" * 60)
    
    xl_urls = [
        "https://www.xl.co.id",
        "https://www.xl.co.id/id/paket-data",
        "https://www.xl.co.id/id/paket-internet",
    ]
    
    results = []
    
    for url in xl_urls:
        print(f"\n?? Mencoba: {url}")
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            resp = requests.get(url, headers=headers, timeout=10)
            
            if resp.status_code == 200:
                content = resp.text
                # Cari pattern
                patterns = re.findall(r'(?:package|family|code)[\s:=]+([A-Z_]{3,})', content, re.I)
                for pattern in patterns:
                    if pattern not in results and len(pattern) > 5:
                        results.append(pattern)
                        print(f"   ? Pattern: {pattern}")
        except Exception as e:
            print(f"   ? Error: {str(e)[:50]}")
    
    return results

def search_documentation():
    """Cari di dokumentasi publik"""
    print("\n" + "=" * 60)
    print("Metode 3: Dokumentasi Publik")
    print("=" * 60)
    
    # Common XL package names dari dokumentasi
    doc_family_codes = {
        "UNLIMITED_TURBO": "Unlimited Turbo",
        "UNLIMITED_TURBO_30D": "Unlimited Turbo 30 Hari",
        "UNLIMITED_TURBO_7D": "Unlimited Turbo 7 Hari",
        "FREEDOM": "Freedom Internet",
        "FREEDOM_MONTHLY": "Freedom Bulanan",
        "FREEDOM_WEEKLY": "Freedom Mingguan",
        "COMBO_LITE": "Combo Lite",
        "COMBO_XTRA": "Combo Xtra",
        "COMBO_MAX": "Combo Max",
        "COMBO_PREMIUM": "Combo Premium",
        "COMBO_LITE_7D": "Combo Lite 7 Hari",
        "COMBO_LITE_30D": "Combo Lite 30 Hari",
        "COMBO_XTRA_7D": "Combo Xtra 7 Hari",
        "COMBO_XTRA_30D": "Combo Xtra 30 Hari",
        "INTERNET_BAIK": "Internet Baik",
        "VIDEO_MAX": "Video Max",
        "GAMES_MAX": "Games Max",
        "SOCIAL_MEDIA": "Social Media",
        "DATA_ONLY": "Data Only",
        "PAKET_DATA": "Paket Data",
        "XTRA_COMBO": "Xtra Combo",
        "XTRA_COMBO_LITE": "Xtra Combo Lite",
        "XTRA_COMBO_MAX": "Xtra Combo Max",
    }
    
    results = []
    for code, name in doc_family_codes.items():
        results.append({"code": code, "name": name, "source": "documentation"})
        print(f"  ? {code}: {name}")
    
    return results

def search_api_public():
    """Coba API publik atau endpoint yang mungkin tidak perlu auth"""
    print("\n" + "=" * 60)
    print("Metode 4: API Publik")
    print("=" * 60)
    
    # Coba berbagai endpoint
    endpoints = [
        "https://api.xl.co.id/api/v8/xl-stores/options/search/family-list",
        "https://www.xl.co.id/api/packages",
        "https://myxl.xl.co.id/api/v1/packages",
    ]
    
    headers = {
        "x-api-key": "245d2532-64c7-42ec-b4de-52f1e8cb4023",
        "Content-Type": "application/json",
    }
    
    payload = {
        "is_enterprise": False,
        "subs_type": "PREPAID",
        "lang": "en"
    }
    
    results = []
    
    for endpoint in endpoints:
        print(f"\n?? Mencoba: {endpoint}")
        try:
            resp = requests.post(endpoint, json=payload, headers=headers, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                if isinstance(data, dict) and "data" in data:
                    families = data.get("data", {}).get("results", [])
                    for family in families:
                        code = family.get("id")
                        if code:
                            results.append(code)
                            print(f"   ? {code}")
        except Exception as e:
            print(f"   ? {str(e)[:50]}")
    
    return results

def search_forum_community():
    """Cari di forum atau komunitas"""
    print("\n" + "=" * 60)
    print("Metode 5: Forum & Komunitas")
    print("=" * 60)
    
    # Pattern umum dari forum/discussion
    forum_codes = [
        "UNLIMITED_TURBO",
        "UNLIMITED_TURBO_30D",
        "FREEDOM",
        "FREEDOM_MONTHLY",
        "COMBO_LITE",
        "COMBO_XTRA",
        "COMBO_MAX",
        "INTERNET_BAIK",
        "VIDEO_MAX",
        "GAMES",
        "SOCIAL",
        "DATA_ONLY",
        "XTRA_COMBO",
        "XTRA_COMBO_LITE",
        "XTRA_COMBO_MAX",
        "XTRA_COMBO_PREMIUM",
    ]
    
    results = []
    for code in forum_codes:
        results.append({"code": code, "source": "forum"})
        print(f"  ? {code}")
    
    return results

def search_in_codebase():
    """Cari di codebase lain atau file yang ada"""
    print("\n" + "=" * 60)
    print("Metode 6: Scan Codebase")
    print("=" * 60)
    
    results = []
    
    # Scan semua file Python di workspace
    import glob
    python_files = glob.glob("**/*.py", recursive=True)
    
    for filepath in python_files[:20]:  # Batasi untuk efisiensi
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Cari pattern family code
                patterns = re.findall(r'["\']([A-Z_]{5,})["\']', content)
                for pattern in patterns:
                    if any(keyword in pattern for keyword in ['FAMILY', 'TURBO', 'COMBO', 'FREEDOM']):
                        if pattern not in results:
                            results.append(pattern)
                            print(f"  ? Ditemukan di {filepath}: {pattern}")
        except:
            pass
    
    return results

def main():
    print("=" * 60)
    print("XL Family Codes Finder - External Sources")
    print("=" * 60)
    print()
    
    all_results = []
    
    # Method 1: GitHub
    github_results = search_github()
    all_results.extend([{"code": r, "source": "github"} for r in github_results])
    
    # Method 2: Web XL
    web_results = search_web_xl()
    all_results.extend([{"code": r, "source": "web"} for r in web_results])
    
    # Method 3: Documentation
    doc_results = search_documentation()
    all_results.extend(doc_results)
    
    # Method 4: API Public
    api_results = search_api_public()
    all_results.extend([{"code": r, "source": "api"} for r in api_results])
    
    # Method 5: Forum
    forum_results = search_forum_community()
    all_results.extend(forum_results)
    
    # Method 6: Codebase
    codebase_results = search_in_codebase()
    all_results.extend([{"code": r, "source": "codebase"} for r in codebase_results])
    
    # Deduplicate
    seen = set()
    unique_results = []
    for item in all_results:
        if isinstance(item, dict):
            code = item.get("code", "")
        else:
            code = str(item)
        
        if code and code not in seen:
            seen.add(code)
            unique_results.append(item if isinstance(item, dict) else {"code": code, "source": "unknown"})
    
    # Save results
    print("\n" + "=" * 60)
    print(f"TOTAL FAMILY CODES DITEMUKAN: {len(unique_results)}")
    print("=" * 60)
    
    output = {
        "total_found": len(unique_results),
        "family_codes": unique_results
    }
    
    filename = "xl_family_codes_external.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n? Hasil disimpan ke: {filename}")
    print("\n?? Daftar Family Codes:")
    print()
    
    for idx, item in enumerate(unique_results, 1):
        code = item.get("code", item) if isinstance(item, dict) else item
        name = item.get("name", "") if isinstance(item, dict) else ""
        source = item.get("source", "unknown") if isinstance(item, dict) else "unknown"
        
        print(f"{idx:3d}. {code}")
        if name:
            print(f"     Name: {name}")
        print(f"     Source: {source}")
        print()
    
    return unique_results

if __name__ == "__main__":
    try:
        results = main()
        print(f"\n? Selesai! Ditemukan {len(results)} family codes dari sumber eksternal")
    except KeyboardInterrupt:
        print("\n\n? Dibatalkan")
        sys.exit(0)
    except Exception as e:
        print(f"\n? Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
