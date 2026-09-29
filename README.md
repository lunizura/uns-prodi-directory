# Direktori Program Studi dan Akreditasi UNS

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Data Source](https://img.shields.io/badge/Data%20Source-SPMB%20UNS-0284c7.svg)](https://spmb.uns.ac.id)
[![Total Study Programs](https://img.shields.io/badge/Total%20Prodi-177-emerald.svg)](#ringkasan-data)
[![Akreditasi Unggul](https://img.shields.io/badge/Unggul-126-gold.svg)](#ringkasan-data)
[![Akreditasi Internasional](https://img.shields.io/badge/Internasional-36%20Prodi-teal.svg)](#ringkasan-data)
[![GitHub Pages](https://img.shields.io/badge/Deployment-GitHub%20Pages%20Ready-brightgreen.svg)](#deploy-ke-github-pages)

Pusat basis data terbuka dan antarmuka pencarian interaktif untuk seluruh program studi, peringkat akreditasi (Nasional & Internasional), rumpun ilmu, lokasi kampus, daya tampung, serta fakultas di **Universitas Sebelas Maret (UNS)**.

Dibuat untuk memudahkan calon mahasiswa (SNBP, SNBT, Seleksi Mandiri), mahasiswa aktif, kebutuhan penelitian data pendidikan, serta open dataset bagi pengembang perangkat lunak.

---

## Fitur Utama

- **Pencarian Real-Time:** Cari prodi berdasarkan nama, kode prodi, maupun fakultas secara instan.
- **Filter Komprehensif:** 
  - Jenjang pendidikan (Sarjana S1, Vokasi D3/D4, Pascasarjana S2/S3).
  - Fakultas & Sekolah Pengelola (FATISDA, FT, FK, FEB, dll).
  - Rumpun Ilmu (Saintek, Soshum, Multidisiplin).
  - Lokasi Kampus (Kampus Utama Surakarta, Kampus PSDKU Kebumen, Kampus PSDKU Madiun).
  - Peringkat Akreditasi (Unggul, Baik Sekali, Baik, A, B).
- **Akreditasi Internasional:** Penanda khusus untuk program studi yang telah tersertifikasi internasional oleh **ASIIN**, **AQAS**, **FIBAA**, atau **IABEE**.
- **Deep Linking:** Filter dan kata kunci pencarian secara otomatis tersinkronisasi dengan URL peramban untuk memudahkan berbagi tautan langsung.
- **Salin Tautan:** Tombol cepat untuk menyalin tautan langsung ke kartu program studi tertentu.
- **Tampilan Fleksibel:** Pilihan tampilan visual kartu informatif atau tabel data ringkas.
- **Ekspor Data:** Dukungan unduh data format **JSON** dan **CSV** langsung dari antarmuka web.
- **Zero-Dependency Deployment:** Siap di-deploy langsung ke **GitHub Pages** atau **Vercel** tanpa langkah kompilasi atau dependensi rumit.

---

## Ringkasan Data

Berdasarkan ekstraksi data resmi portal SPMB UNS:

| Metrik | Jumlah | Keterangan |
| :--- | :--- | :--- |
| **Total Program Studi** | **177** | Mencakup seluruh jenjang pendidikan |
| **Sarjana (S1)** | 78 prodi | Termasuk kampus PSDKU Kebumen |
| **Sekolah Vokasi (D3/D4)** | 27 prodi | Sarjana Terapan & Diploma (Surakarta & Madiun) |
| **Pascasarjana (S2/S3)** | 72 prodi | Magister & Doktoral |
| **Terakreditasi Unggul** | 126 prodi | ~71% dari total program studi |
| **Akreditasi Internasional** | 36 prodi | ASIIN (16), AQAS (11), FIBAA (5), IABEE (4) |
| **Total Fakultas & Sekolah** | 15 unit | Termasuk SV & Sekolah Pascasarjana |

---

## Cara Menjalankan Secara Lokal

Unduh atau clone repositori ini, lalu buka file `index.html` pada peramban Anda:

```bash
git clone https://github.com/USERNAME/uns-prodi-directory.git
cd uns-prodi-directory
```

Buka file `index.html` langsung dengan mengklik ganda file tersebut, atau gunakan live server sederhana:

```bash
# Menggunakan server bawaan Python (opsional)
python -m http.server 8000
```
Lalu akses `http://localhost:8000` pada peramban Anda.

---

## Deploy ke GitHub Pages (Gratis & 1 Klik)

Untuk mempublikasikan situs web ini secara online:

1. Push folder repositori ini ke akun GitHub Anda.
2. Di halaman repositori GitHub, buka menu **Settings** > **Pages** (di sidebar kiri).
3. Pada bagian **Build and deployment** > **Branch**:
   - Pilih branch `main` (atau `master`).
   - Folder: pilih `/ (root)`.
   - Klik **Save**.
4. Dalam 1-2 menit, situs akan aktif dan dapat diakses di:  
   `https://<username>.github.io/uns-prodi-directory/`

---

## Menggunakan Dataset sebagai Public API

Data dapat diambil secara langsung di aplikasi Anda (React, Vue, Flutter, Python, Go, dll.) menggunakan URL raw GitHub atau CDN jsDelivr:

```javascript
// Contoh fetch data prodi dalam JavaScript
fetch('https://raw.githubusercontent.com/USERNAME/uns-prodi-directory/main/data/uns_prodi.json')
  .then(response => response.json())
  .then(data => {
    console.log(`Berhasil memuat ${data.length} program studi`);
    const prodiUnggul = data.filter(p => p.akreditasi === 'Unggul');
    console.log(`Prodi Unggul: ${prodiUnggul.length}`);
  });
```

---

## Struktur Repositori

```text
uns-prodi-directory/
├── assets/
│   └── logo-uns.png       # Logo resmi Universitas Sebelas Maret
├── data/
│   ├── uns_prodi.json     # Dataset lengkap format JSON
│   ├── uns_prodi.js       # Format JS untuk kompatibilitas offline (file://)
│   └── uns_prodi.csv      # Format spreadsheet CSV
├── scripts/
│   └── fetch_uns_data.py  # Script Python untuk scraping & update berkala
├── index.html             # Aplikasi web direktori interaktif
├── LICENSE                # Lisensi MIT
└── README.md              # Dokumentasi proyek
```

---

## Cara Memperbarui Data

Jika terdapat pembaruan akreditasi atau perubahan daya tampung di portal SPMB UNS, jalankan script ekstraksi data:

```bash
python scripts/fetch_uns_data.py
```
Script akan mengambil data terbaru, menormalisasi peringkat, dan memperbarui seluruh berkas di folder `data/`.

---

## Lisensi dan Atribusi

Proyek ini menggunakan lisensi [MIT License](LICENSE). Data mentah bersumber dari **Universitas Sebelas Maret (UNS)** yang dipublikasikan secara terbuka melalui portal [spmb.uns.ac.id](https://spmb.uns.ac.id).
