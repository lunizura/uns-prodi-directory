"""
Script to extract and normalize all study programs (prodi), faculties,
accreditation statuses, quotas, and links from official SPMB UNS portals.

Outputs:
  - data/uns_prodi.json
  - data/uns_prodi.js (for local file:// execution without CORS)
  - data/uns_prodi.csv
"""

import urllib.request
import re
import json
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

FACULTY_MAP = {
    'fatisda': ('Fakultas Teknologi Informasi dan Sains Data', 'FATISDA'),
    'ft': ('Fakultas Teknik', 'FT'),
    'fk': ('Fakultas Kedokteran', 'FK'),
    'feb': ('Fakultas Ekonomika dan Bisnis', 'FEB'),
    'fh': ('Fakultas Hukum', 'FH'),
    'hukum': ('Fakultas Hukum', 'FH'),
    'law': ('Fakultas Hukum', 'FH'),
    'fkip': ('Fakultas Keguruan dan Ilmu Pendidikan', 'FKIP'),
    'fisip': ('Fakultas Ilmu Sosial dan Politik', 'FISIP'),
    'isip': ('Fakultas Ilmu Sosial dan Politik', 'FISIP'),
    'fib': ('Fakultas Ilmu Budaya', 'FIB'),
    'fp': ('Fakultas Pertanian', 'FP'),
    'pertanian': ('Fakultas Pertanian', 'FP'),
    'fpet': ('Fakultas Peternakan', 'FPET'),
    'peternakan': ('Fakultas Peternakan', 'FPET'),
    'fsrd': ('Fakultas Seni Rupa dan Desain', 'FSRD'),
    'fkor': ('Fakultas Keolahragaan', 'FKOR'),
    'psikologi': ('Fakultas Psikologi', 'FPSI'),
    'vokasi': ('Sekolah Vokasi', 'SV'),
    'sv': ('Sekolah Vokasi', 'SV'),
    'pasca': ('Sekolah Pascasarjana', 'SPS'),
    'fmipa': ('Fakultas Matematika dan Ilmu Pengetahuan Alam', 'FMIPA'),
    'mipa': ('Fakultas Matematika dan Ilmu Pengetahuan Alam', 'FMIPA')
}

PRODI_OVERRIDE_FACULTY = {
    'Bahasa dan Kebudayaan Jepang': ('Fakultas Ilmu Budaya', 'FIB'),
    'Desain Mode': ('Fakultas Seni Rupa dan Desain', 'FSRD'),
    'Ekonomi dan Keuangan Islam': ('Fakultas Ekonomika dan Bisnis', 'FEB'),
    'Hubungan Internasional': ('Fakultas Ilmu Sosial dan Politik', 'FISIP'),
    'Ilmu Hukum': ('Fakultas Hukum', 'FH'),
    'Ilmu Komunikasi': ('Fakultas Ilmu Sosial dan Politik', 'FISIP'),
    'Informatika PSDKU (Kebumen)': ('Fakultas Teknologi Informasi dan Sains Data', 'FATISDA'),
    'Pendidikan Kepelatihan Olahraga': ('Fakultas Keolahragaan', 'FKOR'),
    'Proteksi Tanaman': ('Fakultas Pertanian', 'FP'),
    'Psikologi': ('Fakultas Psikologi', 'FPSI'),
    'Seni Rupa': ('Fakultas Seni Rupa dan Desain', 'FSRD'),
    'Agribisnis': ('Fakultas Pertanian', 'FP'),
    'Biomedis': ('Fakultas Kedokteran', 'FK'),
    'Ilmu Keolahragaan': ('Fakultas Keolahragaan', 'FKOR'),
    'Ilmu Teknik Sipil': ('Fakultas Teknik', 'FT'),
    'Kenotariatan': ('Fakultas Hukum', 'FH'),
    'Keselamatan dan Kesehatan Kerja': ('Fakultas Kedokteran', 'FK'),
    'Kimia': ('Fakultas Matematika dan Ilmu Pengetahuan Alam', 'FMIPA'),
    'Matematika': ('Fakultas Matematika dan Ilmu Pengetahuan Alam', 'FMIPA'),
    'Teknik Elektro': ('Fakultas Teknik', 'FT'),
    'Pendidikan Guru Sekolah Dasar (Kampus Kabupaten Kebumen)': ('Fakultas Keguruan dan Ilmu Pendidikan', 'FKIP'),
}

URLS = {
    'S1': 'https://spmb.uns.ac.id/portofolio-riwayat/jenjang?jenjang=s1',
    'Vokasi': 'https://spmb.uns.ac.id/portofolio-riwayat/jenjang?jenjang=d',
    'Pascasarjana': 'https://spmb.uns.ac.id/portofolio-riwayat/jenjang?jenjang=s2-s3'
}

def determine_location(nama):
    n = nama.lower()
    if 'kebumen' in n:
        return 'Kampus PSDKU Kebumen'
    if 'madiun' in n or 'caruban' in n:
        return 'Kampus PSDKU Madiun'
    return 'Kampus Utama (Surakarta)'

def determine_rumpun(nama, fac_short, category):
    n = nama.lower()
    if category == 'Pascasarjana' and fac_short == 'SPS':
        return 'Multidisiplin'
    if fac_short in ('FATISDA', 'FT', 'FK', 'FMIPA', 'FP', 'FPET'):
        return 'Saintek'
    if fac_short in ('FEB', 'FH', 'FISIP', 'FIB', 'FSRD', 'FPSI'):
        return 'Soshum'
    if fac_short == 'FKOR':
        return 'Saintek / Keolahragaan'
    if fac_short == 'FKIP':
        if any(k in n for k in ['matematika', 'fisika', 'kimia', 'biologi', 'komputer', 'ipa', 'mesin', 'bangunan', 'teknik']):
            return 'Saintek'
        return 'Soshum'
    if fac_short == 'SV':
        if any(k in n for k in ['informatika', 'sipil', 'mesin', 'kimia', 'agribisnis', 'ternak', 'kebidanan', 'farmasi', 'k3', 'kesehatan']):
            return 'Saintek'
        return 'Soshum'
    return 'Soshum'

def fetch_data():
    all_prodi = []
    
    for category, url in URLS.items():
        print(f"Fetching {category} from {url}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        try:
            html = urllib.request.urlopen(req, timeout=20).read().decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching {category}: {e}")
            continue
            
        table_match = re.search(r'<table[^>]*>(.*?)</table>', html, re.DOTALL)
        if not table_match:
            print(f"No table found for {category}")
            continue
            
        rows = [r for r in re.split(r'<tr[^>]*>', table_match.group(1)) if '<td' in r]
        
        # Skip header row
        for r in rows[1:]:
            tds = re.findall(r'<td[^>]*>(.*?)</td>', r, re.DOTALL)
            if len(tds) < 5:
                continue
                
            nama = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', tds[1])).strip()
            jenjang_raw = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', tds[2])).strip()
            jenjang_match = re.search(r'\b(S1|D3|D4|S2|S3|Profesi|Spesialis)\b', jenjang_raw, re.I)
            jenjang = jenjang_match.group(1).upper() if jenjang_match else jenjang_raw
            
            kode_match = re.search(r'kode_prodi=(\d+)', r)
            kode_prodi = kode_match.group(1) if kode_match else ""
            
            akr_raw = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', tds[3])).strip()
            akr_match = re.search(r'^([A-Za-z\s]+?)(?:\s*\((.*?)\))?$', akr_raw)
            if akr_match:
                akr_peringkat = akr_match.group(1).strip()
                akr_skor = akr_match.group(2).strip() if akr_match.group(2) else ""
            else:
                akr_peringkat = akr_raw
                akr_skor = ""
                
            # Normalize rank labels
            if akr_peringkat.lower() == 'terakreditasi unggul':
                akr_peringkat = 'Unggul'
                
            akr_internasional_raw = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', tds[4])).strip()
            if akr_internasional_raw in ('-', '', 'None'):
                akr_internasional = []
            else:
                clean_intl = akr_internasional_raw.replace('Full Accredited', '').replace('Conditions Accredited', '').strip(' ()')
                akr_internasional = [clean_intl if clean_intl else akr_internasional_raw]
                
            if category in ('S1', 'Vokasi'):
                daya_tampung = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', tds[5])).strip().replace('*', '')
                file_td = tds[6] if len(tds) > 6 else ""
            else:
                dt1 = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', tds[5])).strip()
                dt2 = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', tds[6])).strip() if len(tds) > 6 else ""
                daya_tampung = f"P1: {dt1}, P2: {dt2}" if dt2 and dt2 != '-' else dt1
                file_td = tds[7] if len(tds) > 7 else ""
                
            link_file_match = re.search(r'href=["\'](.*?)["\']', file_td)
            link_file = ("https://spmb.uns.ac.id" + link_file_match.group(1)) if link_file_match else ""
            
            all_links = re.findall(r'href=["\'](.*?)["\']', r)
            website = ""
            fakultas_name = ""
            fakultas_short = ""
            
            # 1. Override dictionary check
            if nama in PRODI_OVERRIDE_FACULTY and category != 'Vokasi':
                fakultas_name, fakultas_short = PRODI_OVERRIDE_FACULTY[nama]
                
            # 2. Subdomain check from links
            if not fakultas_short:
                for l in all_links:
                    for k, v in FACULTY_MAP.items():
                        if f'{k}.uns.ac.id' in l or f'fakultas/{k}' in l:
                            fakultas_name, fakultas_short = v
                            if not website and 'http' in l:
                                website = l
                            break
                    if fakultas_short: break

            # 3. Vokasi category always belongs to Sekolah Vokasi (SV)
            if category == 'Vokasi':
                fakultas_name, fakultas_short = ('Sekolah Vokasi', 'SV')

            # 4. Resolve website URL fallback
            if not website:
                for l in all_links:
                    if 'uns.ac.id' in l and 'spmb.uns.ac.id' not in l:
                        website = l
                        break

            # Create clean slug ID
            slug_name = re.sub(r'[^a-z0-9]+', '-', nama.lower()).strip('-')
            slug_id = f"{jenjang.lower()}-{slug_name}"

            lokasi = determine_location(nama)
            rumpun = determine_rumpun(nama, fakultas_short, category)

            all_prodi.append({
                'id': slug_id,
                'kode_prodi': kode_prodi,
                'nama_prodi': nama,
                'jenjang': jenjang,
                'kategori': category,
                'rumpun': rumpun,
                'lokasi_kampus': lokasi,
                'fakultas': fakultas_name,
                'fakultas_singkatan': fakultas_short,
                'akreditasi': akr_peringkat,
                'akreditasi_skor': akr_skor,
                'akreditasi_internasional': akr_internasional,
                'daya_tampung': daya_tampung,
                'website': website,
                'link_sk_akreditasi': link_file
            })
            
    print(f"Successfully processed {len(all_prodi)} study programs.")
    return all_prodi

from datetime import datetime

def save_outputs(prodi_list):
    now = datetime.now()
    months = ["", "Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    formatted_date = f"{now.day} {months[now.month]} {now.year}"
    metadata = {
        "last_updated_iso": now.isoformat(),
        "last_updated_date": formatted_date,
        "total_prodi": len(prodi_list),
        "source": "https://spmb.uns.ac.id"
    }

    # 1. Save Metadata JSON
    meta_path = os.path.join(DATA_DIR, "metadata.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print(f"Saved: {meta_path}")

    # 2. Save Prodi JSON
    json_path = os.path.join(DATA_DIR, "uns_prodi.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(prodi_list, f, indent=2, ensure_ascii=False)
    print(f"Saved: {json_path}")
    
    # 3. Save JS (for file:// protocol offline compatibility)
    js_path = os.path.join(DATA_DIR, "uns_prodi.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("window.UNS_METADATA = " + json.dumps(metadata, indent=2, ensure_ascii=False) + ";\n")
        f.write("window.UNS_PRODI_DATA = " + json.dumps(prodi_list, indent=2, ensure_ascii=False) + ";\n")
    print(f"Saved: {js_path}")
    
    # 4. Save CSV
    csv_path = os.path.join(DATA_DIR, "uns_prodi.csv")
    fieldnames = [
        'id', 'kode_prodi', 'nama_prodi', 'jenjang', 'kategori',
        'rumpun', 'lokasi_kampus', 'fakultas', 'fakultas_singkatan',
        'akreditasi', 'akreditasi_skor', 'akreditasi_internasional',
        'daya_tampung', 'website', 'link_sk_akreditasi'
    ]
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in prodi_list:
            row = dict(p)
            row['akreditasi_internasional'] = ", ".join(p['akreditasi_internasional'])
            writer.writerow(row)
    print(f"Saved: {csv_path}")

if __name__ == "__main__":
    prodi_data = fetch_data()
    save_outputs(prodi_data)
