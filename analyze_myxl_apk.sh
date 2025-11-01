#!/bin/bash
# Script untuk download dan analisis MyXL APK
# Dapat membantu menemukan family codes dari aplikasi MyXL

echo "=========================================="
echo "MyXL APK Analyzer for Family Codes"
echo "=========================================="
echo ""

# Check if required tools are installed
check_tool() {
    if ! command -v $1 &> /dev/null; then
        echo "? $1 tidak ditemukan. Install dengan:"
        case $1 in
            "apktool")
                echo "   sudo apt-get install apktool"
                ;;
            "jq")
                echo "   sudo apt-get install jq"
                ;;
        esac
        return 1
    else
        echo "? $1 sudah terinstall"
        return 0
    fi
}

echo "Checking tools..."
check_tool "unzip" || exit 1
check_tool "grep" || exit 1

# Function to download APK from apkpure
download_apk() {
    echo ""
    echo "Cara download MyXL APK:"
    echo "1. Kunjungi: https://apkpure.com/myxl/com.xl.app"
    echo "2. Download APK terbaru"
    echo "3. Simpan dengan nama: myxl.apk"
    echo ""
    read -p "Apakah sudah download? (y/n): " downloaded
    if [ "$downloaded" != "y" ]; then
        echo "Silakan download APK terlebih dahulu"
        exit 1
    fi
    
    if [ ! -f "myxl.apk" ]; then
        echo "? File myxl.apk tidak ditemukan!"
        exit 1
    fi
    echo "? File myxl.apk ditemukan"
}

# Function to extract APK
extract_apk() {
    echo ""
    echo "Extracting APK..."
    if [ -d "myxl_extracted" ]; then
        echo "Directory myxl_extracted sudah ada. Menghapus..."
        rm -rf myxl_extracted
    fi
    
    mkdir -p myxl_extracted
    unzip -q myxl.apk -d myxl_extracted
    echo "? APK berhasil diextract"
}

# Function to search for family codes
search_family_codes() {
    echo ""
    echo "Mencari family codes dalam APK..."
    echo ""
    
    # Search for common patterns
    echo "=== Pattern 1: 'family' ==="
    grep -r -i "family" myxl_extracted/ | grep -i "code\|id" | head -20
    
    echo ""
    echo "=== Pattern 2: 'package_family_code' ==="
    grep -r "package_family_code" myxl_extracted/ | head -20
    
    echo ""
    echo "=== Pattern 3: 'family_code' ==="
    grep -r "family_code" myxl_extracted/ | head -20
    
    echo ""
    echo "=== Pattern 4: API endpoints ==="
    grep -r "xl-stores/options" myxl_extracted/ | head -20
    
    echo ""
    echo "=== Pattern 5: Store atau package related ==="
    grep -r -i "store\|package" myxl_extracted/ | grep -i "family\|code" | head -20
}

# Function to analyze network traffic hints
analyze_network_hints() {
    echo ""
    echo "Menganalisis network endpoints..."
    echo ""
    
    # Look for API URLs
    echo "=== API Base URLs ==="
    grep -r -E "https?://.*api.*xl" myxl_extracted/ | head -10
    
    echo ""
    echo "=== API Endpoints ==="
    grep -r -E "api/v[0-9]/xl-stores" myxl_extracted/ | head -20
}

# Function to extract strings.xml or similar
extract_strings() {
    echo ""
    echo "Mencari string resources yang mungkin berisi family codes..."
    echo ""
    
    find myxl_extracted -name "*.xml" -type f | xargs grep -l "family\|package" | head -10 | while read file; do
        echo "=== $file ==="
        grep -i "family\|package" "$file" | head -5
        echo ""
    done
}

# Function to create summary
create_summary() {
    echo ""
    echo "=========================================="
    echo "Summary"
    echo "=========================================="
    echo ""
    echo "File-file yang mungkin berisi family codes:"
    echo "- res/values/strings.xml (Android resources)"
    echo "- assets/ (JavaScript/JSON files)"
    echo "- classes.dex (decompile dengan jadx untuk melihat Java code)"
    echo ""
    echo "Cara terbaik untuk mendapatkan family codes:"
    echo "1. Gunakan me-cli dengan menu 'Store Family List'"
    echo "2. Capture network traffic MyXL app dengan proxy"
    echo "3. Gunakan script get_family_codes.py dengan API key"
    echo ""
}

# Main execution
main() {
    if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
        echo "Usage: $0 [options]"
        echo ""
        echo "Options:"
        echo "  --help, -h     Show this help message"
        echo "  --no-download  Skip APK download step"
        echo ""
        echo "This script will:"
        echo "1. Download MyXL APK (if needed)"
        echo "2. Extract APK contents"
        echo "3. Search for family codes in extracted files"
        echo ""
        exit 0
    fi
    
    if [ "$1" != "--no-download" ]; then
        download_apk
    fi
    
    extract_apk
    search_family_codes
    analyze_network_hints
    extract_strings
    create_summary
    
    echo ""
    echo "? Analisis selesai!"
    echo "Hasil disimpan di directory: myxl_extracted/"
    echo ""
    echo "Tips:"
    echo "- Gunakan jadx untuk decompile classes.dex untuk melihat kode Java"
    echo "- Capture network traffic untuk melihat API calls yang sebenarnya"
    echo "- Gunakan script get_family_codes.py untuk mendapatkan family codes langsung dari API"
}

main "$@"
