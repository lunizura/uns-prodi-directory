# UNS Study Programs and Accreditation Directory

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Data Source](https://img.shields.io/badge/Data%20Source-SPMB%20UNS-0284c7.svg)](https://spmb.uns.ac.id)
[![Total Study Programs](https://img.shields.io/badge/Total%20Programs-177-emerald.svg)](#data-summary)
[![Accredited Unggul](https://img.shields.io/badge/Unggul%20(Superior)-126-gold.svg)](#data-summary)
[![International Accreditation](https://img.shields.io/badge/International-36%20Programs-teal.svg)](#data-summary)
[![GitHub Pages](https://img.shields.io/badge/Deployment-GitHub%20Pages%20Ready-brightgreen.svg)](#deployment-to-github-pages)

An open data repository and interactive web directory for all study programs, accreditation ratings (National & International), academic disciplines, campus locations, admission quotas, and faculties at **Universitas Sebelas Maret (UNS)**, Surakarta, Indonesia.

Designed for prospective university applicants (SNBP, SNBT, and Seleksi Mandiri), current students, academic researchers, and software developers seeking structured higher education open datasets.

---

## Key Features

- **Real-Time Search:** Search study programs instantly by program name, program code, or faculty.
- **Bilingual Interface:** Instant language switching between **Bahasa Indonesia** and **English**.
- **Comprehensive Multi-Level Filters:**
  - Degree levels: Undergraduate (S1), Vocational (D3/D4), Postgraduate (S2/S3).
  - Managing Faculties & Schools: FATISDA, FT, FK, FEB, FH, FKIP, FISIP, FIB, FP, FPET, FSRD, FKOR, FPSI, FMIPA, SV, SPS.
  - Academic Disciplines: Science & Technology (Saintek), Social Sciences & Humanities (Soshum), Sports, and Multidisciplinary.
  - Campus Locations: Surakarta Main Campus (Kentingan), PSDKU Kebumen, and PSDKU Madiun.
  - Accreditation Rankings: Superior (Unggul), Very Good (Baik Sekali), Good (Baik), Grade A, Grade B.
- **International Accreditation Badges:** Highlights programs certified by international accreditation bodies including **ASIIN**, **AQAS**, **FIBAA**, and **IABEE**.
- **Deep Linking:** Search queries and active filter states synchronize with the browser URL for easy sharing.
- **Permalinks:** Direct copy button to share specific study program cards.
- **Flexible Layouts:** Toggle seamlessly between an informative grid card view and a compact data table.
- **Automated Freshness Warning:** Alerts visitors automatically if data has not been updated within 90 days.
- **Zero-Dependency Deployment:** Ready to deploy immediately to **GitHub Pages** or **Vercel** with no compilation steps or npm packages required.

---

## Data Summary

Extracted directly from official SPMB Universitas Sebelas Maret portals:

| Metric | Total | Description |
| :--- | :--- | :--- |
| **Total Study Programs** | **177** | Spanning all academic levels |
| **Undergraduate (S1)** | 78 programs | Regular & PSDKU Kebumen |
| **Vocational School (D3/D4)** | 27 programs | Applied Bachelor & Diploma (Surakarta & Madiun) |
| **Postgraduate (S2/S3)** | 72 programs | Master & Doctoral programs |
| **Accredited Unggul (Superior)** | 126 programs | ~71% of all study programs |
| **International Accreditation** | 36 programs | ASIIN (16), AQAS (11), FIBAA (5), IABEE (4) |
| **Total Faculties & Schools** | 15 units | Including SV & Graduate School (SPS) |

---

## Running Locally

Clone the repository and open `index.html` in your web browser:

```bash
git clone https://github.com/lunizura/uns-prodi-directory.git
cd uns-prodi-directory
```

Open `index.html` directly by double-clicking it, or start a lightweight local server:

```bash
# Using Python built-in server (optional)
python -m http.server 8000
```
Then visit `http://localhost:8000` in your web browser.

---

## Deployment to GitHub Pages

To publish this website live for free:

1. Push this repository to your GitHub account.
2. In your repository on GitHub, navigate to **Settings** > **Pages** (in the left sidebar).
3. Under **Build and deployment** > **Branch**:
   - Select branch `main`.
   - Select folder `/ (root)`.
   - Click **Save**.
4. Within 1 to 2 minutes, your website will be live at:  
   `https://lunizura.github.io/uns-prodi-directory/`

---

## Using the Dataset as a Public API

You can consume the structured dataset directly in your applications (React, Vue, Flutter, Python, Go, etc.) using GitHub raw URLs or jsDelivr CDN:

```javascript
// Example: Fetch study program data in JavaScript
fetch('https://raw.githubusercontent.com/lunizura/uns-prodi-directory/main/data/uns_prodi.json')
  .then(response => response.json())
  .then(data => {
    console.log(`Loaded ${data.length} study programs!`);
    const unggulPrograms = data.filter(p => p.akreditasi === 'Unggul');
    console.log(`Unggul programs count: ${unggulPrograms.length}`);
  });
```

---

## Repository Structure

```text
uns-prodi-directory/
├── assets/
│   └── logo-uns.png       # Official Universitas Sebelas Maret crest logo
├── data/
│   ├── metadata.json      # Snapshot timestamp and data source metadata
│   ├── uns_prodi.json     # Complete structured dataset in JSON
│   ├── uns_prodi.js       # Offline-compatible script for local file:// execution
│   └── uns_prodi.csv      # Spreadsheet CSV format
├── scripts/
│   └── fetch_uns_data.py  # Python automated scraper to refresh all data
├── index.html             # Interactive web directory application
├── LICENSE                # MIT License
└── README.md              # Project documentation
```

---

## Updating the Dataset

If new accreditation decrees or admission quotas are published on SPMB UNS, re-run the extraction script:

```bash
python scripts/fetch_uns_data.py
```
The script will fetch the latest records, normalize rankings, regenerate the metadata timestamp, and update all files in the `data/` directory.

---

## License and Attribution

This project is licensed under the [MIT License](LICENSE). The raw institutional data is the property of **Universitas Sebelas Maret (UNS)** and is published openly via [spmb.uns.ac.id](https://spmb.uns.ac.id).
