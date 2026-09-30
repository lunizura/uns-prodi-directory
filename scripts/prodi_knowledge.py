"""
Knowledge base and generator for UNS Study Program profiles.
Provides detailed bilingual (Indonesian & English) information on:
- Program Overview (Deskripsi)
- What it Teaches / Core Study Focus (Fokus Studi / Kurikulum Inti)
- What Graduates Do / Career Prospects (Prospek Karir & Lapangan Kerja)
"""

import re

def get_prodi_profile(nama, jenjang, fakultas_singkatan, rumpun, lokasi):
    n = nama.lower()
    j = jenjang.upper()
    fac = fakultas_singkatan.upper() if fakultas_singkatan else ""

    # Defaults
    desc_id = ""
    desc_en = ""
    fokus_id = []
    fokus_en = []
    karir_id = []
    karir_en = []

    # 1. Computer Science & IT (FATISDA / PTIK / D3 TI)
    if 'informatika' in n or 'komputer' in n or 'sains data' in n:
        if 'sains data' in n:
            desc_id = f"Program studi {nama} ({j}) membekali mahasiswa dengan keahlian analitika data skala besar, pembelajaran mesin (machine learning), pemodelan statistika, dan visualisasi data untuk pengambilan keputusan strategis berbasis data."
            desc_en = f"The {nama} ({j}) program equips students with expertise in large-scale data analytics, machine learning, statistical modeling, and data visualization to drive strategic data-driven decisions."
            fokus_id = ["Machine Learning & Deep Learning", "Analitika Big Data & Basis Data Terdistribusi", "Statistika Terapan & Pemodelan Prediktif", "Visualisasi Data & Business Intelligence"]
            fokus_en = ["Machine Learning & Deep Learning", "Big Data Analytics & Distributed Databases", "Applied Statistics & Predictive Modeling", "Data Visualization & Business Intelligence"]
            karir_id = ["Data Scientist", "Data Engineer", "Machine Learning Engineer", "Business Intelligence Analyst", "Peneliti AI"]
            karir_en = ["Data Scientist", "Data Engineer", "Machine Learning Engineer", "Business Intelligence Analyst", "AI Researcher"]
        elif 'pendidikan' in n:
            desc_id = f"Program studi {nama} ({j}) memadukan ilmu komputasi modern dengan pedagogi pendidikan untuk mencetak tenaga pendidik profesional di bidang informatika, rekayasa perangkat lunak, dan teknologi pembelajaran digital."
            desc_en = f"The {nama} ({j}) program integrates computer science with pedagogical methodologies to produce professional educators in informatics, software engineering, and educational technologies."
            fokus_id = ["Rekayasa Perangkat Lunak & Pemrograman", "Jaringan Komputer & Sistem Operasi", "Pedagogi & Desain Pembelajaran Digital", "Pengembangan Media Interaktif & E-Learning"]
            fokus_en = ["Software Engineering & Programming", "Computer Networks & Operating Systems", "Pedagogy & Digital Learning Design", "Interactive Media Development & E-Learning"]
            karir_id = ["Guru / Dosen Informatika & Komputer", "Instruktur Pelatihan IT", "Instructional Designer", "Pengembang Perangkat Pembelajaran", "Software Developer"]
            karir_en = ["Informatics & Computer Science Teacher/Lecturer", "IT Corporate Trainer", "Instructional Designer", "EdTech Developer", "Software Developer"]
        elif j in ('D3', 'D4'):
            desc_id = f"Program studi vokasi {nama} ({j}) berfokus pada penguasaan keterampilan praktis terapan dalam rekayasa aplikasi web, mobile, komputasi awan, administrasi basis data, dan dukungan teknis industri."
            desc_en = f"The vocational {nama} ({j}) program focuses on hands-on practical skills in web and mobile application engineering, cloud computing, database administration, and industrial IT support."
            fokus_id = ["Pemrograman Web & Mobile Terapan", "Administrasi Basis Data & Cloud Computing", "Pengujian Perangkat Lunak & QA", "Keamanan Siber Praktis & Jaringan"]
            fokus_en = ["Applied Web & Mobile Programming", "Database Administration & Cloud Computing", "Software Quality Assurance (QA)", "Practical Cybersecurity & Networking"]
            karir_id = ["Web & Mobile Application Developer", "Junior Software Engineer", "Database Administrator", "QA Tester", "Network & IT Support Specialist"]
            karir_en = ["Web & Mobile Application Developer", "Junior Software Engineer", "Database Administrator", "QA Tester", "Network & IT Support Specialist"]
        elif j in ('S2', 'S3'):
            desc_id = f"Program pascasarjana {nama} ({j}) berfokus pada riset tingkat lanjut dalam kecerdasan buatan, sistem otonom, optimasi algoritma, komputasi berkinerja tinggi, dan inovasi arsitektur perangkat lunak."
            desc_en = f"The postgraduate {nama} ({j}) program focuses on advanced research in artificial intelligence, autonomous systems, algorithmic optimization, high-performance computing, and software architecture innovation."
            fokus_id = ["Riset Kecerdasan Artifisial Tingkat Lanjut", "Arsitektur Sistem Terdistribusi & Cloud", "Optimasi Algoritma & Teori Komputasi", "Sains Data & Bioinformatika"]
            fokus_en = ["Advanced AI Research", "Distributed & Cloud Systems Architecture", "Algorithmic Optimization & Computational Theory", "Data Science & Bioinformatics"]
            karir_id = ["Peneliti Komputasi / Ilmuwan AI", "Dosen / Akademisi", "Chief Technology Officer (CTO)", "Konsultan Arsitektur IT", "Lead Data Scientist"]
            karir_en = ["Computing Researcher / AI Scientist", "University Professor / Academic", "Chief Technology Officer (CTO)", "Enterprise IT Architecture Consultant", "Lead Data Scientist"]
        else:
            kebumen_note = " di Kampus PSDKU Kebumen" if "kebumen" in n else ""
            desc_id = f"Program studi {nama} ({j}){kebumen_note} mengkaji teori komputasi, rekayasa perangkat lunak modern, kecerdasan buatan, keamanan siber, dan sistem jaringan terdistribusi untuk memecahkan tantangan teknologi terkini."
            desc_en = f"The {nama} ({j}) program{kebumen_note} explores computational theory, modern software engineering, artificial intelligence, cybersecurity, and distributed systems to solve cutting-edge technological challenges."
            fokus_id = ["Rekayasa Perangkat Lunak (Software Engineering)", "Kecerdasan Buatan (Artificial Intelligence) & Machine Learning", "Keamanan Siber & Jaringan Komputer", "Sistem Terdistribusi & Arsitektur Cloud"]
            fokus_en = ["Software Engineering & Architecture", "Artificial Intelligence & Machine Learning", "Cybersecurity & Computer Networks", "Distributed Systems & Cloud Architecture"]
            karir_id = ["Software Engineer / Fullstack Developer", "AI / Machine Learning Engineer", "Cybersecurity Specialist", "Cloud & DevOps Architect", "Sistem Analis IT"]
            karir_en = ["Software Engineer / Fullstack Developer", "AI / Machine Learning Engineer", "Cybersecurity Specialist", "Cloud & DevOps Architect", "IT Systems Analyst"]

    # 2. Medicine, Nursing & Health (FK / SV Medis)
    elif 'kedokteran' in n or 'profesi dokter' in n or 'kebidanan' in n or 'farmasi' in n or 'biomedis' in n or 'kesehatan kerja' in n or 'k3' in n:
        if 'farmasi' in n:
            desc_id = f"Program studi {nama} ({j}) mempelajari formulasi obat, farmakologi, kimia medisinal, farmasi klinis, serta pengembangan obat herbal dan fitofarmaka berbasis riset berkelanjutan."
            desc_en = f"The {nama} ({j}) program investigates pharmaceutical formulation, pharmacology, medicinal chemistry, clinical pharmacy, and evidence-based phytopharmaceutical drug discovery."
            fokus_id = ["Farmakologi & Toksikologi", "Teknologi Formulasi Sediaan Farmasi", "Farmasi Klinis & Komunitas", "Kimia Medisinal & Bahan Alam"]
            fokus_en = ["Pharmacology & Toxicology", "Pharmaceutical Formulation Technology", "Clinical & Community Pharmacy", "Medicinal Chemistry & Natural Products"]
            karir_id = ["Apoteker / Tenaga Teknis Kefarmasian", "Formulator Riset & Pengembangan Obat (R&D)", "Penjamin Mutu Farmasi (QA/QC)", "Regulatory Affairs Specialist", "Farmasi Klinis Rumah Sakit"]
            karir_en = ["Pharmacist / Pharmaceutical Technical Staff", "Pharmaceutical R&D Formulator", "Quality Assurance / Quality Control (QA/QC)", "Regulatory Affairs Specialist", "Hospital Clinical Pharmacist"]
        elif 'kebidanan' in n:
            desc_id = f"Program studi {nama} ({j}) mendidik tenaga profesional kebidanan dengan keunggulan asuhan holistik pada masa prakonsepsi, kehamilan, persalinan, nifas, bayi baru lahir, dan kesehatan reproduksi wanita."
            desc_en = f"The {nama} ({j}) program trains professional midwifery practitioners specializing in holistic care across pre-conception, pregnancy, childbirth, postpartum, neonatal, and women's reproductive health."
            fokus_id = ["Asuhan Kebidanan Fisiologis & Patologis", "Kesehatan Reproduksi & Keluarga Berencana", "Kebidanan Komunitas & Promosi Kesehatan", "Keterampilan Kegawatdaruratan Maternal & Neonatal"]
            fokus_en = ["Physiological & Pathological Midwifery Care", "Reproductive Health & Family Planning", "Community Midwifery & Health Promotion", "Maternal & Neonatal Emergency Skills"]
            karir_id = ["Bidan Praktik Mandiri & Rumah Sakit", "Konselor Kesehatan Reproduksi", "Fasilitator Kesehatan Komunitas", "Pendidik & Peneliti Kebidanan", "Tenaga Ahli KIA di Lembaga Kesehatan"]
            karir_en = ["Clinical & Private Practice Midwife", "Reproductive Health Counselor", "Community Health Facilitator", "Midwifery Educator & Researcher", "Maternal-Child Health Specialist"]
        elif 'k3' in n or 'keselamatan dan kesehatan kerja' in n:
            desc_id = f"Program studi {nama} ({j}) mendalami identifikasi bahaya kerja, analisis risiko ergonomi dan higiene industri, investigasi kecelakaan, serta implementasi sistem manajemen K3 di berbagai sektor industri."
            desc_en = f"The {nama} ({j}) program explores occupational hazard identification, ergonomic and industrial hygiene risk analysis, incident investigation, and HSE management systems across industrial sectors."
            fokus_id = ["Sistem Manajemen K3 (SMK3 & ISO 45001)", "Higiene Industri & Toksikologi Lingkungan Kerja", "Ergonomi & Faktor Manusia", "Investigasi & Manajemen Risiko Kecelakaan Kerja"]
            fokus_en = ["Occupational Health & Safety Systems (ISO 45001)", "Industrial Hygiene & Occupational Toxicology", "Ergonomics & Human Factors", "Accident Investigation & Risk Management"]
            karir_id = ["HSE (Health, Safety, and Environment) Officer", "Industrial Hygiene Specialist", "Auditor Sistem Manajemen K3", "Konsultan Keselamatan Kerja", "HSE Coordinator di Sektor Manufaktur/Migas"]
            karir_en = ["HSE Officer / Specialist", "Industrial Hygiene Specialist", "Occupational Health & Safety Auditor", "Safety Management Consultant", "HSE Coordinator (Manufacturing/Energy)"]
        elif 'biomedis' in n:
            desc_id = f"Program studi {nama} ({j}) memadukan biologi molekuler, genetika manusia, imunologi, dan patologi modern untuk meneliti mekanisme penyakit dan terapi inovatif tingkat seluler."
            desc_en = f"The {nama} ({j}) program integrates molecular biology, human genetics, immunology, and advanced pathology to investigate disease mechanisms and cellular-level therapeutic innovations."
            fokus_id = ["Biologi Molekuler & Genetika Medis", "Imunologi & Onkologi Terapan", "Patobiologi Penyakit Infeksi & Degeneratif", "Teknik Laboratorium Diagnostik Lanjutan"]
            fokus_en = ["Molecular Biology & Medical Genetics", "Applied Immunology & Oncology", "Pathobiology of Infectious & Degenerative Diseases", "Advanced Diagnostic Laboratory Techniques"]
            karir_id = ["Peneliti Biomedis", "Ilmuwan Laboratorium Klinis / Molekuler", "Dosen / Akademisi Kedokteran", "Spesialis Riset Pengembangan Terapi", "Konsultan Bioteknologi Medis"]
            karir_en = ["Biomedical Researcher", "Clinical / Molecular Laboratory Scientist", "Medical Academic / Lecturer", "Therapeutics R&D Specialist", "Medical Biotechnology Consultant"]
        else:
            desc_id = f"Program studi {nama} ({j}) melatih dokter berstandar global dengan penguasaan komprehensif sains dasar kedokteran, keterampilan diagnostik klinis, etika bioetika, dan kedokteran keluarga/komunitas."
            desc_en = f"The {nama} ({j}) program trains globally qualified medical physicians with comprehensive mastery of basic medical sciences, clinical diagnostic acumen, bioethics, and community medicine."
            fokus_id = ["Sains Biomedik Dasar & Organ Sistem Tubuh", "Keterampilan Klinis & Komunikasi Medis", "Penalaran Klinis & Diagnosis Penyakit", "Kedokteran Keluarga, Komunitas & Bioetika"]
            fokus_en = ["Basic Biomedical Sciences & Body Systems", "Clinical Skills & Medical Communication", "Clinical Reasoning & Differential Diagnosis", "Family Medicine, Community Health & Bioethics"]
            karir_id = ["Dokter Umum / Praktisi Klinis", "Dokter Rumah Sakit / Puskesmas", "Peneliti Medis & Klinis", "Manajer Fasilitas Pelayanan Kesehatan", "Akademisi Kedokteran"]
            karir_en = ["General Practitioner / Medical Doctor", "Hospital / Community Health Physician", "Medical & Clinical Researcher", "Healthcare Facility Administrator", "Medical Academician"]

    # 3. Engineering (FT / Vokasi Teknik)
    elif fac == 'FT' or any(k in n for k in ['teknik sipil', 'arsitektur', 'teknik mesin', 'teknik industri', 'teknik kimia', 'teknik elektro', 'perencanaan wilayah']):
        if 'sipil' in n:
            desc_id = f"Program studi {nama} ({j}) mengkaji perencanaan, perancangan, konstruksi, dan pemeliharaan infrastruktur seperti gedung, jembatan, jalan raya, pelabuhan, serta sistem pengelolaan sumber daya air."
            desc_en = f"The {nama} ({j}) program investigates the planning, structural design, construction, and maintenance of civil infrastructure including buildings, bridges, highways, harbors, and water resource systems."
            fokus_id = ["Rekayasa Struktur & Material Konstruksi", "Geoteknik & Mekanika Tanah", "Rekayasa Transportasi & Jalan Raya", "Manajemen Proyek Konstruksi & Sumber Daya Air"]
            fokus_en = ["Structural Engineering & Construction Materials", "Geotechnical Engineering & Soil Mechanics", "Transportation & Highway Engineering", "Construction Project Management & Water Resources"]
            karir_id = ["Structural Engineer / Perancang Bangunan", "Project Manager Konstruksi", "Konsultan Rekayasa Sipil", "Quantity Surveyor", "Ahli Geoteknik / Infrastruktur"]
            karir_en = ["Structural Design Engineer", "Construction Project Manager", "Civil Engineering Consultant", "Quantity Surveyor", "Geotechnical / Infrastructure Specialist"]
        elif 'arsitektur' in n:
            desc_id = f"Program studi {nama} ({j}) memadukan seni desain spasial, sains bangunan, teknologi konstruksi, dan keberlanjutan lingkungan untuk merancang ruang hunian dan perkotaan yang estetik serta fungsional."
            desc_en = f"The {nama} ({j}) program blends spatial design art, building science, construction technology, and environmental sustainability to create aesthetic, resilient, and functional built environments."
            fokus_id = ["Studio Perancangan Arsitektur", "Sains Bangunan & Arsitektur Berkelanjutan", "Struktur & Konstruksi Bangunan Tinggi", "Sejarah, Teori, dan Kritik Arsitektur"]
            fokus_en = ["Architectural Design Studio", "Building Science & Sustainable Architecture", "High-Rise Structures & Construction Systems", "Architectural History, Theory & Criticism"]
            karir_id = ["Arsitek Perancang (Architectural Designer)", "Urban Designer / Perancang Kota", "Konsultan Green Building", "Interior Architect", "Visualizer Arsitektur 3D / BIM Coordinator"]
            karir_en = ["Architectural Designer", "Urban Designer", "Green Building Consultant", "Interior Architect", "BIM Coordinator / 3D Architectural Visualizer"]
        elif 'mesin' in n:
            desc_id = f"Program studi {nama} ({j}) mendalami konversi energi, perancangan sistem mekanikal, manufaktur modern, robotika, dan pemilihan material teknik untuk aplikasi industri otomotif dan energi terbarukan."
            desc_en = f"The {nama} ({j}) program explores energy conversion, mechanical system design, precision manufacturing, robotics, and engineering materials for automotive, manufacturing, and renewable energy industries."
            fokus_id = ["Konversi Energi & Termodinamika Terapan", "Perancangan Mekanikal & CAD/CAM/CAE", "Manufaktur Presisi & Otomasi Industri", "Material Teknik & Metalurgi"]
            fokus_en = ["Energy Conversion & Applied Thermodynamics", "Mechanical Design & CAD/CAM/CAE", "Precision Manufacturing & Industrial Automation", "Engineering Materials & Metallurgy"]
            karir_id = ["Mechanical Design Engineer", "Maintenance & Reliability Engineer", "Manufacturing & Plant Engineer", "Spesialis Otomasi & Robotika", "Konsultan Konversi Energi"]
            karir_en = ["Mechanical Design Engineer", "Maintenance & Reliability Engineer", "Manufacturing & Plant Engineer", "Automation & Robotics Specialist", "Energy Conversion Consultant"]
        elif 'industri' in n:
            desc_id = f"Program studi {nama} ({j}) memfokuskan integrasi sistem manusia, mesin, material, informasi, dan energi untuk mengoptimalkan efisiensi produksi, logistik, rantai pasok, dan manajemen kualitas."
            desc_en = f"The {nama} ({j}) program optimizes integrated systems of people, equipment, materials, information, and energy to enhance manufacturing efficiency, logistics, supply chains, and quality systems."
            fokus_id = ["Optimasi Sistem Produksi & Operasi", "Manajemen Rantai Pasok (Supply Chain) & Logistik", "Ergonomi & Perancangan Sistem Kerja", "Rekayasa Kualitas (Quality Engineering & Six Sigma)"]
            fokus_en = ["Production & Operations Systems Optimization", "Supply Chain Management & Logistics", "Work Design & Human Factors Ergonomics", "Quality Engineering & Six Sigma"]
            karir_id = ["Supply Chain / Logistics Planner", "Production Planning & Inventory Control (PPIC)", "Quality Assurance / Continuous Improvement Engineer", "Operations Analyst", "Konsultan Manajemen Operasional"]
            karir_en = ["Supply Chain / Logistics Planner", "PPIC Engineer", "Quality Assurance & Continuous Improvement Engineer", "Operations Analyst", "Operations Management Consultant"]
        elif 'kimia' in n:
            desc_id = f"Program studi {nama} ({j}) mempelajari perancangan pabrik kimia, proses pemisahan, termodinamika reaksi, perancangan reaktor, dan teknologi bioproses yang ramah lingkungan."
            desc_en = f"The {nama} ({j}) program studies chemical plant design, separation processes, reaction thermodynamics, reactor modeling, and eco-friendly bioprocess technologies."
            fokus_id = ["Termodinamika Teknik Kimia & Perancangan Reaktor", "Operasi Teknik Kimia & Proses Pemisahan", "Perancangan Pabrik Kimia Terpadu", "Teknologi Polimer & Pengolahan Limbah Industri"]
            fokus_en = ["Chemical Reaction Engineering & Reactor Design", "Transport Phenomena & Unit Operations", "Integrated Chemical Plant Design", "Polymer Technology & Environmental Treatment"]
            karir_id = ["Process Engineer di Industri Petrokimia/Migas", "Chemical Plant Operations Engineer", "R&D Chemist / Formulator", "HSE & Waste Treatment Specialist", "Project Engineering Consultant"]
            karir_en = ["Petrochemical / Process Engineer", "Chemical Plant Operations Engineer", "R&D Industrial Chemist", "HSE & Environmental Treatment Specialist", "Project Engineering Consultant"]
        elif 'elektro' in n:
            desc_id = f"Program studi {nama} ({j}) memfokuskan kajian pada sistem tenaga listrik, elektronika industri, sistem kendali cerdas, telekomunikasi, dan pemrosesan sinyal digital."
            desc_en = f"The {nama} ({j}) program investigates electrical power systems, industrial electronics, intelligent control systems, telecommunications, and digital signal processing."
            fokus_id = ["Sistem Tenaga Listrik & Energi Baru Terbarukan", "Elektronika Daya & Sistem Tertanam (Embedded Systems)", "Sistem Kendali, Otomasi & IoT Industri", "Telekomunikasi & Pengolahan Sinyal"]
            fokus_en = ["Electrical Power Systems & Renewable Energy", "Power Electronics & Embedded Systems", "Control Systems, Automation & Industrial IoT", "Telecommunications & Signal Processing"]
            karir_id = ["Electrical Power Engineer", "Embedded Systems Developer", "Automation & Control Engineer", "Telecommunications Engineer", "Konsultan Energi Terbarukan"]
            karir_en = ["Electrical Power Engineer", "Embedded Systems Developer", "Automation & Control Engineer", "Telecommunications Engineer", "Renewable Energy Consultant"]
        elif 'wilayah' in n or 'pwk' in n:
            desc_id = f"Program studi {nama} ({j}) mengkaji perencanaan tata ruang kota dan wilayah, analisis spasial GIS, pengelolaan permukiman, transportasi perkotaan, dan kebijakan mitigasi bencana lingkungan."
            desc_en = f"The {nama} ({j}) program examines urban and regional spatial planning, GIS spatial modeling, housing and infrastructure policy, sustainable transport, and disaster mitigation planning."
            fokus_id = ["Studio Perencanaan Kota & Wilayah Terpadu", "Sistem Informasi Geografis (SIG / GIS) & Analisis Spasial", "Manajemen Infrastruktur & Transportasi Perkotaan", "Kebijakan Tata Ruang & Pembangunan Berkelanjutan"]
            fokus_en = ["Integrated Urban & Regional Planning Studio", "Geographic Information Systems (GIS) & Spatial Analysis", "Urban Infrastructure & Transportation Management", "Spatial Policy & Sustainable Development"]
            karir_id = ["Urban & Regional Planner", "GIS Analyst / Spesialis Pemetaan Spasial", "Konsultan Tata Ruang & AMDAL", "Perencana Pembangunan di Bappeda / Kementerian ATR", "Community Development Specialist"]
            karir_en = ["Urban & Regional Planner", "GIS Analyst & Spatial Modeler", "Spatial & Environmental Planning Consultant", "Public Planning Officer (National/Regional)", "Community Development Specialist"]
        else:
            desc_id = f"Program studi {nama} ({j}) membina kemampuan rekayasa teknis, inovasi teknologi terapan, riset eksperimental, dan analisis kuantitatif untuk menjawab tantangan industri kontemporer."
            desc_en = f"The {nama} ({j}) program fosters engineering acumen, applied technological innovation, experimental research, and quantitative analysis to address modern industrial challenges."
            fokus_id = ["Perancangan Sistem Rekayasa & Keteknikan", "Matematika Teknik & Komputasi Numerik", "Manajemen Proyek Rekayasa", "Inovasi & Keberlanjutan Teknologi"]
            fokus_en = ["Engineering Systems Design", "Engineering Mathematics & Numerical Methods", "Engineering Project Management", "Technological Innovation & Sustainability"]
            karir_id = ["Engineering Specialist", "Project Engineer", "Konsultan Keteknikan", "Analis Operasional Industri", "Peneliti Rekayasa"]
            karir_en = ["Engineering Specialist", "Project Engineer", "Engineering Consultant", "Industrial Operations Analyst", "Engineering Researcher"]

    # 4. Economics, Business & Management (FEB / Vokasi Bisnis)
    elif fac == 'FEB' or any(k in n for k in ['akuntansi', 'manajemen', 'ekonomi pembangunan', 'bisnis digital', 'keuangan islam', 'perpajakan', 'pemasaran']):
        if 'akuntansi' in n or 'perpajakan' in n:
            desc_id = f"Program studi {nama} ({j}) mendalami akuntansi keuangan, audit dan asurans, sistem informasi akuntansi, pelaporan keberlanjutan (ESG), analisis perpajakan, dan tata kelola korporat modern."
            desc_en = f"The {nama} ({j}) program examines financial accounting, audit assurance, accounting information systems, ESG sustainability reporting, tax planning, and corporate governance."
            fokus_id = ["Akuntansi Keuangan Menengah & Lanjutan", "Pengauditan & Layanan Asurans (Auditing)", "Perpajakan Korporat & Perencanaan Pajak", "Sistem Informasi Akuntansi & Analitika Data Finansial"]
            fokus_en = ["Intermediate & Advanced Financial Accounting", "Auditing & Assurance Services", "Corporate Taxation & Tax Planning", "Accounting Information Systems & Financial Analytics"]
            karir_id = ["Akuntan Publik (CPA / Auditor)", "Analis Keuangan & Pajak Korporat", "Akuntan Manajemen / Controller", "Auditor Forensik & Internal", "Konsultan Keuangan Perusahaan"]
            karir_en = ["Certified Public Accountant (CPA / Auditor)", "Corporate Financial & Tax Analyst", "Management Accountant / Controller", "Forensic & Internal Auditor", "Corporate Finance Consultant"]
        elif 'bisnis digital' in n:
            desc_id = f"Program studi {nama} ({j}) memadukan ilmu manajemen modern, strategi e-commerce, pemasaran digital, fintech, analitika data konsumen, dan perancangan startup teknologi inovatif."
            desc_en = f"The {nama} ({j}) program merges modern management, e-commerce strategy, digital marketing, fintech, consumer data analytics, and tech startup entrepreneurship."
            fokus_id = ["Model Bisnis Digital & Strategi E-Commerce", "Digital Marketing & Growth Hacking", "Analitika Data Bisnis & Big Data", "Teknologi Finansial (Fintech) & Startup Inovatif"]
            fokus_en = ["Digital Business Models & E-Commerce Strategy", "Digital Marketing & Growth Hacking", "Business Analytics & Big Data", "Financial Technology (Fintech) & Startup Venturing"]
            karir_id = ["Digital Business Strategist / Product Manager", "Digital Marketing Specialist", "Growth & E-Commerce Manager", "Business Analyst", "Tech Startup Founder"]
            karir_en = ["Digital Business Strategist / Product Manager", "Digital Marketing Specialist", "Growth & E-Commerce Manager", "Business Analyst", "Tech Startup Founder"]
        elif 'manajemen' in n or 'pemasaran' in n:
            desc_id = f"Program studi {nama} ({j}) mengembangkan kepemimpinan strategis, manajemen pemasaran global, manajemen operasi rantai nilai, tata kelola sumber daya manusia, dan manajemen keuangan korporasi."
            desc_en = f"The {nama} ({j}) program develops strategic leadership, global marketing management, value-chain operations, human capital governance, and corporate financial management."
            fokus_id = ["Manajemen Strategik & Kepemimpinan Bisnis", "Pemasaran Strategis & Perilaku Konsumen", "Manajemen Operasi & Rantai Nilai", "Manajemen Keuangan Korporasi & Investasi"]
            fokus_en = ["Strategic Management & Business Leadership", "Strategic Marketing & Consumer Behavior", "Operations & Value Chain Management", "Corporate Finance & Investment Analysis"]
            karir_id = ["Brand / Marketing Manager", "Human Resource (HR) Manager", "Operations & Logistics Manager", "Business Development Executive", "Konsultan Manajemen Bisnis"]
            karir_en = ["Brand / Marketing Manager", "Human Capital / HR Manager", "Operations & Logistics Manager", "Business Development Executive", "Management Consultant"]
        elif 'keuangan islam' in n:
            desc_id = f"Program studi {nama} ({j}) mengkaji prinsip-prinsip fiqih muamalah, perbankan syariah, manajemen investasi dan sukuk, asuransi syariah (takaful), serta tata kelola filantropi Islam (zakat dan wakaf)."
            desc_en = f"The {nama} ({j}) program studies Islamic jurisprudence (fiqh muamalah), Islamic banking, sukuk and investment funds, takaful insurance, and Islamic social finance governance (zakat and waqf)."
            fokus_id = ["Fiqih Muamalah & Hukum Ekonomi Syariah", "Manajemen Perbankan & Lembaga Keuangan Syariah", "Pasar Modal Syariah, Sukuk & Investasi", "Tata Kelola Zakat, Infak, Sedekah & Wakaf (ZISWAF)"]
            fokus_en = ["Islamic Commercial Jurisprudence (Fiqh Muamalah)", "Islamic Banking & Financial Institutions Management", "Islamic Capital Markets, Sukuk & Investment", "Zakat, Waqf & Social Finance Governance"]
            karir_id = ["Sharia Banking Officer / Analis Pembiayaan", "Analis Pasar Modal Syariah", "Dewan Pengawas Syariah / Konsultan Fiqih Bisnis", "Manajer Lembaga Amil Zakat & Wakaf", "Risk Management Officer Syariah"]
            karir_en = ["Sharia Banking Officer / Credit Analyst", "Islamic Capital Market Analyst", "Sharia Compliance & Advisory Officer", "Islamic Philanthropy (Zakat/Waqf) Manager", "Sharia Risk Management Officer"]
        else: # Ekonomi Pembangunan
            desc_id = f"Program studi {nama} ({j}) menganalisis teori ekonomi makro-mikro, ekonomi moneter dan fiskal, ekonometrika terapan, kebijakan publik, dan strategi pembangunan berkelanjutan."
            desc_en = f"The {nama} ({j}) program analyzes macroeconomic-microeconomic theory, monetary and fiscal policies, applied econometrics, public policy analysis, and sustainable regional development strategies."
            fokus_id = ["Teori Ekonomi Makro & Mikro Lanjutan", "Ekonometrika Terapan & Analisis Data Ekonomi", "Ekonomi Moneter, Fiskal & Kebijakan Publik", "Ekonomi Pembangunan Daerah & Perdagangan Internasional"]
            fokus_en = ["Advanced Macroeconomic & Microeconomic Theory", "Applied Econometrics & Economic Data Analysis", "Monetary, Fiscal & Public Policy Economics", "Regional Development & International Trade Economics"]
            karir_id = ["Analis Kebijakan Ekonomi (Kemenkeu, Bappenas, BI, OJK)", "Peneliti Ekonomi & Sosial", "Economic & Market Research Analyst", "Konsultan Kebijakan Pembangunan", "Perencana Pembangunan Daerah"]
            karir_en = ["Economic Policy Analyst (Govt / Central Bank / IMF)", "Economic & Social Researcher", "Market Research Analyst", "Development Policy Consultant", "Regional Development Planner"]

    # 5. Law & Governance (FH / Kenotariatan / Demografi)
    elif fac == 'FH' or any(k in n for k in ['hukum', 'kenotariatan', 'pencatatan sipil']):
        if 'kenotariatan' in n:
            desc_id = f"Program studi {nama} ({j}) menyiapkan calon notaris dan Pejabat Pembuat Akta Tanah (PPAT) profesional dengan penguasaan mendalam atas hukum perdata, pembuatan akta otentik, hukum pertanahan, dan kode etik kenotariatan."
            desc_en = f"The {nama} ({j}) program prepares future Notaries and Land Deed Officials (PPAT) with specialized mastery in civil law, authentic deed drafting, agrarian law, and notarial ethics."
            fokus_id = ["Teknik Pembuatan Akta Notaris & Perjanjian", "Hukum Pertanahan & Pembuatan Akta Tanah (PPAT)", "Hukum Perusahaan, Perbankan & Jaminan", "Kode Etik Profesi & Jabatan Notaris"]
            fokus_en = ["Notarial Deed & Contract Drafting Techniques", "Agrarian Law & Land Deed Drafting (PPAT)", "Corporate Law, Banking & Collateral Law", "Professional Code of Ethics & Notarial Office"]
            karir_id = ["Notaris & PPAT (setelah uji kompetensi)", "Konsultan Hukum Pertanahan & Korporasi", "Legal Specialist di Lembaga Keuangan/Perbankan", "Akademisi Hukum Kenotariatan"]
            karir_en = ["Notary Public & Land Deed Official", "Corporate & Agrarian Legal Consultant", "Banking / Real Estate Legal Specialist", "Legal Academic / Lecturer"]
        elif 'pencatatan sipil' in n or 'demografi' in n:
            desc_id = f"Program studi vokasi {nama} ({j}) mendidik profesional terapan di bidang administrasi kependudukan, registrasi sipil, analisis statistik demografi, dan tata kelola data kependudukan digital."
            desc_en = f"The vocational {nama} ({j}) program trains applied professionals in civil registration, vital statistics, demographic analytics, and digital identity data governance."
            fokus_id = ["Hukum & Administrasi Kependudukan", "Sistem Pendaftaran Penduduk & Pencatatan Sipil", "Analisis Data Demografi & Kependudukan", "Digitalisasi Layanan Publik & Tata Kelola Data"]
            fokus_en = ["Population Law & Civil Administration", "Vital Registration & Civil Status Systems", "Demographic Analytics & Population Trends", "Public Service Digitalization & Data Governance"]
            karir_id = ["Aparatur / Administrator Dukcapil", "Analis Data Demografi & Kependudukan", "Petugas Registrasi Sipil Profesional", "Konsultan Kebijakan Sosial & Kependudukan", "Staff HR / Verifikasi Identitas Korporat"]
            karir_en = ["Civil Registration & Vital Statistics Administrator", "Demographic Data Analyst", "Identity Verification & Vital Records Specialist", "Social Policy Researcher", "Corporate Identity Compliance Officer"]
        else:
            desc_id = f"Program studi {nama} ({j}) membekali mahasiswa dengan penguasaan komprehensif sistem hukum Indonesia dan internasional, penalaran hukum (legal reasoning), penyusunan kontrak, advokasi, dan penegakan keadilan yang berintegritas."
            desc_en = f"The {nama} ({j}) program provides comprehensive mastery of domestic and international legal systems, rigorous legal reasoning, contract negotiation, litigation advocacy, and judicial integrity."
            fokus_id = ["Hukum Perdata, Dagang & Bisnis Modern", "Hukum Pidana & Sistem Peradilan Pidana", "Hukum Tata Negara & Hukum Administrasi Negara", "Hukum Internasional, Hak Asasi Manusia & Kemahiran Litigasi"]
            fokus_en = ["Civil, Commercial & Modern Business Law", "Criminal Law & Criminal Justice Systems", "Constitutional & Administrative Law", "International Law, Human Rights & Litigation Advocacy"]
            karir_id = ["Advokat / Pengacara", "Hakim & Jaksa Penegak Hukum", "Corporate Legal Counsel", "Diplomat / Analis Hukum Internasional", "Legal Drafter / Analis Peraturan Perundang-Undangan"]
            karir_en = ["Advocate / Attorney at Law", "Judge / Public Prosecutor", "Corporate Legal Counsel", "Diplomat / International Legal Specialist", "Legislative & Regulatory Drafter"]

    # 6. Languages, Humanities & Culture (FIB / D4 Bahasa)
    elif fac == 'FIB' or any(k in n for k in ['sastra', 'bahasa inggris', 'bahasa mandarin', 'bahasa jepang', 'bahasa daerah', 'bahasa jawa', 'sastra arab', 'sejarah', 'linguistik', 'budaya']):
        if 'bisnis dan profesional' in n:
            lang_label = "Bahasa Inggris" if "inggris" in n else ("Bahasa Mandarin" if "mandarin" in n else "Bahasa Asing")
            lang_label_en = "English" if "inggris" in n else ("Mandarin Chinese" if "mandarin" in n else "Foreign Language")
            desc_id = f"Program studi terapan {nama} ({j}) melatih kemahiran komunikasi korporat tingkat lanjut berbahasa {lang_label}, penerjemahan dan penjurubahasaan profesional, diplomasi bisnis, serta hubungan masyarakat internasional."
            desc_en = f"The applied {nama} ({j}) program develops advanced {lang_label_en} corporate communication competence, professional translation and interpretation, cross-border business diplomacy, and global public relations."
            fokus_id = [f"Komunikasi Bisnis & Korespondensi Korporat Berbahasa {lang_label}", f"Penerjemahan Teks Bisnis & Penjurubahasaan Simultan (Interpretation)", "Public Relations & Negosiasi Antarbudaya", "Pemasaran Konten & Komunikasi Media Digital"]
            fokus_en = [f"Advanced {lang_label_en} Business Communication & Corporate Correspondence", f"Commercial Translation & Simultaneous Interpretation", "Public Relations & Cross-Cultural Negotiation", "Content Marketing & Digital Media Strategy"]
            karir_id = ["Professional Translator & Interpreter", "International Public Relations Specialist", "Corporate Communications Officer", "Bilingual Content Strategist", "Diplomatic / Trade Liaison Officer"]
            karir_en = ["Professional Translator & Interpreter", "International Public Relations Specialist", "Corporate Communications Officer", "Bilingual Content Strategist", "Trade & Diplomatic Liaison Officer"]
        elif 'sejarah' in n:
            desc_id = f"Program studi {nama} ({j}) mempelajari metodologi penelitian historis, historiografi, arsip dan museum, sejarah sosial-politik Indonesia, dan analisis peristiwa masa lalu untuk memahami dinamika peradaban."
            desc_en = f"The {nama} ({j}) program studies historical research methodologies, historiography, archival and museum curation, Indonesian socio-political history, and critical analysis of civilizational change."
            fokus_id = ["Metodologi Penelitian Sejarah & Kritik Sumber", "Historiografi Indonesia & Sejarah Asia", "Kearsipan, Kurasi Museum & Sejarah Publik", "Sejarah Kebudayaan & Pemikiran Kritis"]
            fokus_en = ["Historical Research Methodology & Source Criticism", "Indonesian & Asian Historiography", "Archival Sciences, Museum Curation & Public History", "Cultural History & Critical Intellectual Inquiry"]
            karir_id = ["Sejarawan & Peneliti Sejarah", "Kurator Museum & Arsiparis", "Penulis & Jurnalis Sejarah", "Analis Cagar Budaya", "Akademisi / Dosen Sejarah"]
            karir_en = ["Historian & Archival Researcher", "Museum Curator & Archivist", "Historical Writer & Investigative Journalist", "Cultural Heritage Specialist", "History Academic / University Lecturer"]
        else:
            lang_name = "Sastra & Bahasa"
            if 'inggris' in n: lang_name = "Sastra Inggris"
            elif 'jepang' in n: lang_name = "Bahasa & Kebudayaan Jepang"
            elif 'mandarin' in n: lang_name = "Bahasa Mandarin & Kebudayaan Tiongkok"
            elif 'jawa' in n or 'daerah' in n: lang_name = "Sastra Daerah (Jawa)"
            elif 'arab' in n: lang_name = "Sastra Arab"
            elif 'indonesia' in n: lang_name = "Sastra Indonesia"

            desc_id = f"Program studi {nama} ({j}) mendalami kemahiran linguistik, telaah sastra kritis, penerjemahan, kajian kebudayaan, dan filologi untuk menghasilkan lulusan yang berwawasan humanis serta komunikator lintas budaya."
            desc_en = f"The {nama} ({j}) program explores linguistic theory, critical literary analysis, translation studies, cultural history, and philology to produce culturally adept communicators and humanities scholars."
            fokus_id = ["Kajian Linguistik & Fonologi-Sintaksis-Semantik", "Apresiasi & Kritik Sastra Teoretis", "Kajian Budaya & Komunikasi Antarbudaya", "Teori & Praktik Penerjemahan Lintas Bahasa"]
            fokus_en = ["Linguistic Studies (Phonology, Syntax, Semantics)", "Theoretical Literary Criticism & Comparative Literature", "Cultural Studies & Cross-Cultural Communication", "Translation Theory & Bilingual Practice"]
            karir_id = ["Penerjemah & Penyunting Naskah (Editor)", "Spesialis Komunikasi Lintas Budaya", "Penulis Kreatif & Kritikus Sastra", "Diplomat Budaya / Atase Kebudayaan", "Akademisi & Peneliti Humaniora"]
            karir_en = ["Professional Translator & Literary Editor", "Cross-Cultural Communication Specialist", "Creative Author & Cultural Critic", "Cultural Diplomat / Cultural Liaison Officer", "Humanities Researcher & Educator"]

    # 7. Social & Political Sciences (FISIP)
    elif fac == 'FISIP' or any(k in n for k in ['komunikasi', 'hubungan internasional', 'administrasi negara', 'administrasi publik', 'sosiologi']):
        if 'komunikasi' in n:
            desc_id = f"Program studi {nama} ({j}) mengkaji teori komunikasi massa, jurnalisme investigatif, periklanan kreatif, public relations strategis, penyiaran media, dan produksi konten digital."
            desc_en = f"The {nama} ({j}) program investigates mass communication theories, investigative journalism, creative advertising, strategic public relations, broadcasting, and digital content production."
            fokus_id = ["Teori Komunikasi Strategis & Riset Media", "Manajemen Hubungan Masyarakat (Public Relations)", "Jurnalisme Multimedia & Penyiaran", "Komunikasi Pemasaran Terpadu (IMC) & Periklanan"]
            fokus_en = ["Strategic Communication Theory & Media Research", "Corporate Public Relations Management", "Multimedia Journalism & Digital Broadcasting", "Integrated Marketing Communications (IMC) & Advertising"]
            karir_id = ["Public Relations / Corporate PR Specialist", "Jurnalis / Produser Media Digital", "Media Planner & Advertising Specialist", "Social Media & Brand Strategist", "Konsultan Komunikasi Publik"]
            karir_en = ["Corporate Public Relations Specialist", "Digital Journalist / Media Producer", "Media Planner & Advertising Executive", "Social Media & Brand Strategist", "Public Communication Consultant"]
        elif 'hubungan internasional' in n:
            desc_id = f"Program studi {nama} ({j}) menganalisis dinamika geopolitik global, diplomasi antarnegara, ekonomi politik internasional, resolusi konflik, dan tata kelola organisasi multilateral."
            desc_en = f"The {nama} ({j}) program analyzes global geopolitical dynamics, bilateral and multilateral diplomacy, international political economy, conflict resolution, and international organizations."
            fokus_id = ["Teori Hubungan Internasional & Geopolitik Global", "Diplomasi & Negosiasi Internasional", "Ekonomi Politik Global & Perdagangan Internasional", "Keamanan Internasional & Studi Perdamaian"]
            fokus_en = ["International Relations Theory & Geopolitics", "Diplomacy & International Negotiations", "Global Political Economy & Trade Governance", "International Security & Peace Studies"]
            karir_id = ["Diplomat / Pejabat Dinas Luar Negeri", "Analis Geopolitik & Hubungan Internasional", "Officer di Lembaga Internasional (PBB, ASEAN, NGO Global)", "International Business Development Consultant", "Peneliti Kebijakan Luar Negeri"]
            karir_en = ["Diplomat / Foreign Service Officer", "Geopolitical & Intelligence Analyst", "International NGO / UN Program Officer", "International Business Development Consultant", "Foreign Policy Researcher"]
        elif 'administrasi' in n:
            desc_id = f"Program studi {nama} ({j}) mendalami formulasi dan evaluasi kebijakan publik, reformasi birokrasi, tata kelola pemerintahan digital (e-government), serta manajemen organisasi sektor publik."
            desc_en = f"The {nama} ({j}) program analyzes public policy formulation and evaluation, bureaucratic reform, digital government (e-governance), and public-sector organizational management."
            fokus_id = ["Analisis Kebijakan Publik & Manajemen Pelayanan Publik", "Tata Kelola Pemerintahan Digital (E-Government)", "Manajemen Keuangan Sektor Publik & Anggaran", "Reformasi Birokrasi & Kepemimpinan Publik"]
            fokus_en = ["Public Policy Analysis & Public Service Management", "Digital Governance & E-Government Systems", "Public Sector Financial Management & Budgeting", "Bureaucratic Reform & Public Leadership"]
            karir_id = ["Analis Kebijakan Publik (Kementerian/Bappeda)", "Administrator Instansi Pemerintah", "Konsultan Tata Kelola Pemerintahan & Sektor Publik", "Manajer Organisasi Nirlaba (NGO)", "Peneliti Kebijakan Publik"]
            karir_en = ["Public Policy Analyst", "Government Agency Administrator", "Public Sector Governance Consultant", "Non-Profit Organization Director", "Public Governance Researcher"]
        else: # Sosiologi
            desc_id = f"Program studi {nama} ({j}) mempelajari struktur masyarakat, perubahan sosial, dinamika konflik dan integrasi, sosiologi perkotaan-pedesaan, serta metodologi penelitian sosial kualitatif dan kuantitatif."
            desc_en = f"The {nama} ({j}) program examines social structures, societal transformation, social conflict and cohesion, urban-rural sociology, and qualitative and quantitative sociological methodologies."
            fokus_id = ["Teori Sosiologi Klasik & Kontemporer", "Metodologi Riset Sosial Kualitatif & Kuantitatif", "Sosiologi Pembangunan, Kemiskinan & Perubahan Sosial", "Sosiologi Lingkungan & Pemberdayaan Komunitas"]
            fokus_en = ["Classical & Contemporary Sociological Theories", "Qualitative & Quantitative Social Research Methodologies", "Sociology of Development & Social Transformation", "Environmental Sociology & Community Empowerment"]
            karir_id = ["Peneliti Sosial & Kebijakan Kemasyarakatan", "Spesialis Pemberdayaan Masyarakat (CSR/Community Development)", "Analis Masalah Sosial & Opini Publik", "Perencana Pembangunan Sosial", "Akademisi Sosiologi"]
            karir_en = ["Social Researcher & Demographer", "Community Development / CSR Specialist", "Social Impact & Public Opinion Analyst", "Social Planning Consultant", "Sociology Academician"]

    # 8. Art & Design (FSRD / Vokasi Desain)
    elif fac == 'FSRD' or any(k in n for k in ['desain komunikasi visual', 'dkv', 'desain interior', 'kriya', 'seni rupa', 'desain mode', 'media digital']):
        if 'komunikasi visual' in n or 'dkv' in n or 'media digital' in n:
            desc_id = f"Program studi {nama} ({j}) mengembangkan keahlian perancangan identitas visual, ilustrasi digital, tipografi, desain UI/UX, animasi gerak, dan strategi komunikasi kreatif lintas platform."
            desc_en = f"The {nama} ({j}) program develops expertise in visual identity branding, digital illustration, typography, UI/UX design, motion graphics, and multi-platform creative communications."
            fokus_id = ["Desain Identitas Merek (Branding) & Tipografi", "Desain Antarmuka & Pengalaman Pengguna (UI/UX)", "Ilustrasi Digital, Konsep Seni & Animasi", "Komunikasi Visual Periklanan & Kampanye Sosial"]
            fokus_en = ["Brand Identity Design & Advanced Typography", "User Interface & User Experience Design (UI/UX)", "Digital Illustration, Concept Art & Motion Graphics", "Advertising Visual Communication & Campaigns"]
            karir_id = ["UI/UX Designer & Product Designer", "Art Director / Creative Director", "Brand Identity Designer", "Digital Illustrator & Motion Graphic Designer", "Visual Communication Consultant"]
            karir_en = ["UI/UX Designer & Product Designer", "Art Director / Creative Director", "Brand Identity Designer", "Digital Illustrator & Motion Graphic Artist", "Creative Communications Consultant"]
        elif 'interior' in n:
            desc_id = f"Program studi {nama} ({j}) melatih perancangan ruang dalam (interior) komersial, residensial, dan publik dengan integrasi ergonomi, pencahayaan, materialitas estetika, serta efisiensi energi."
            desc_en = f"The {nama} ({j}) program trains interior design for commercial, residential, and public spaces integrating human ergonomics, architectural lighting, materiality, and sustainable energy efficiency."
            fokus_id = ["Studio Perancangan Desain Interior Ruang Publik & Residensial", "Ergonomi Spasial & Sains Pencahayaan / Akustik", "Material Interior, Konstruksi & Furnitur Kustom", "Rendering Visualisasi 3D & Manajemen Proyek Interior"]
            fokus_en = ["Residential & Public Interior Design Studio", "Spatial Ergonomics, Lighting Science & Acoustics", "Interior Materials, Construction & Custom Furniture", "3D Architectural Visualization & Interior Project Management"]
            karir_id = ["Desainer Interior Profesional", "Konsultan Tata Ruang Komersial", "Perancang Furnitur / Lighting Specialist", "Interior Project Manager", "Set Designer untuk Film / Pameran"]
            karir_en = ["Professional Interior Designer", "Commercial Space Planning Consultant", "Custom Furniture / Lighting Designer", "Interior Project Manager", "Exhibition & Stage Set Designer"]
        elif 'mode' in n:
            desc_id = f"Program studi {nama} ({j}) mendalami pembuatan pola busana, tren fesyen, eksplorasi tekstil tradisional seperti batik nusantara, desain busana kontemporer, dan manajemen bisnis industri kreatif fesyen."
            desc_en = f"The {nama} ({j}) program explores apparel pattern drafting, fashion forecasting, textile innovation including traditional Indonesian batik, contemporary garment design, and fashion business management."
            fokus_id = ["Perancangan Busana Kontemporer & Konseptual", "Pembuatan Pola (Pattern Making) & Draping", "Eksplorasi Tekstil Nusantara & Batik", "Manajemen Bisnis, Branding & Pemasaran Fesyen"]
            fokus_en = ["Contemporary & Conceptual Fashion Design", "Advanced Pattern Making & Draping", "Traditional Indonesian Textiles & Batik Innovation", "Fashion Brand Management & Merchandising"]
            karir_id = ["Fashion Designer / Perancang Busana", "Fashion Stylist / Konsultan Gaya", "Pattern Maker / Garment Production Specialist", "Textile Designer", "Wirausahawan Label Fesyen"]
            karir_en = ["Fashion Designer", "Fashion Stylist & Creative Director", "Garment Production & Pattern Specialist", "Textile Designer", "Fashion Label Entrepreneur"]
        else: # Kriya / Seni Rupa
            desc_id = f"Program studi {nama} ({j}) mengasah eksplorasi artistik murni dan terapan, penguasaan medium dua dimensi dan tiga dimensi, kurasi seni, kritik seni, dan pelestarian warisan budaya visual."
            desc_en = f"The {nama} ({j}) program hones artistic exploration across fine arts and applied crafts, mastery of 2D and 3D media, art curation, aesthetic criticism, and cultural visual preservation."
            fokus_id = ["Studio Seni Lukis, Patung & Seni Grafis", "Eksplorasi Kriya Keramik, Logam, Kayu & Tekstil", "Sejarah Seni Rupa Nusantara & Dunia", "Kurasi Galeri Seni & Kritik Seni Kontemporer"]
            fokus_en = ["Painting, Sculpture & Printmaking Studios", "Craft Exploration in Ceramics, Metal, Wood & Textile", "Indonesian & World Art History", "Gallery Curation & Contemporary Art Criticism"]
            karir_id = ["Seniman Rupa / Kriya Mandiri", "Kurator Seni & Pengelola Galeri", "Konservator Karya Seni / Restorator", "Kritikus Seni & Penulis Budaya", "Pendidik Seni Rupa"]
            karir_en = ["Fine Artist / Master Craftsman", "Art Curator & Gallery Manager", "Art Conservator / Heritage Restorer", "Art Critic & Cultural Essayist", "Fine Arts Educator"]

    # 9. Sports & Physical Education (FKOR)
    elif fac == 'FKOR' or any(k in n for k in ['keolahragaan', 'olahraga', 'penjas']):
        desc_id = f"Program studi {nama} ({j}) mempelajari fisiologi olahraga, biomekanika gerak, psikologi atlet, metodologi kepelatihan fisik terukur, pencegahan cedera, dan manajemen industri keolahragaan modern."
        desc_en = f"The {nama} ({j}) program investigates exercise physiology, sports biomechanics, athletic psychology, scientific training methodology, injury rehabilitation, and sports industry management."
        fokus_id = ["Fisiologi Latihan & Biomekanika Olahraga", "Metodologi Kepelatihan & Periodisasi Fisik Atlet", "Psikologi Olahraga & Manajemen Pertandingan", "Pencegahan, Penanganan Cedera & Terapi Fisik Olahraga"]
        fokus_en = ["Exercise Physiology & Sports Biomechanics", "Athletic Training Periodization & Coaching Methodology", "Sports Psychology & Event Management", "Sports Injury Prevention, Rehabilitation & Physical Therapy"]
        karir_id = ["Pelatih Fisik / Pelatih Cabang Olahraga Prestasi", "Strength & Conditioning Coach", "Instruktur Kebugaran & Wellness Specialist", "Guru / Dosen Pendidikan Jasmani", "Manajer Klub / Event Organizer Keolahragaan"]
        karir_en = ["Performance Sports Coach", "Strength & Conditioning Coach", "Fitness Instructor & Wellness Specialist", "Physical Education Teacher / Lecturer", "Sports Club & Event Manager"]

    # 10. Psychology (FPSI)
    elif fac == 'FPSI' or 'psikologi' in n:
        desc_id = f"Program studi {nama} ({j}) mempelajari perilaku manusia, proses mental, asesmen psikodiagnostika, psikologi perkembangan, intervensi psikososial, dan dinamika psikologi organisasi/industri."
        desc_en = f"The {nama} ({j}) program explores human behavior, cognitive processes, psychodiagnostic assessment, developmental psychology, psychosocial interventions, and organizational-industrial dynamics."
        fokus_id = ["Psikodiagnostika & Konstruksi Alat Ukur Psikologi", "Psikologi Perkembangan Anak, Remaja & Dewasa", "Psikologi Industri & Organisasi (PIO)", "Psikologi Klinis Dasar & Intervensi Psikososial"]
        fokus_en = ["Psychodiagnostics & Psychological Test Construction", "Child, Adolescent & Adult Developmental Psychology", "Industrial & Organizational Psychology (I/O)", "Foundations of Clinical Psychology & Psychosocial Interventions"]
        karir_id = ["Asisten Psikolog & Asesor Psikotes", "Talent Acquisition / HR Generalist", "Konselor Pendidikan & Pengasuhan", "Analis Perilaku Konsumen / Riset Psikologi", "Pelatih Pengembangan Sumber Daya Manusia (Trainer)"]
        karir_en = ["Psychological Assessor & Assistant Psychologist", "Talent Acquisition / HR Generalist", "Educational & Family Counselor", "Consumer Behavior / Behavioral Researcher", "Corporate Human Capital Trainer"]

    # 11. Agriculture, Forestry & Animal Science (FP / FPET)
    elif fac in ('FP', 'FPET') or any(k in n for k in ['agroteknologi', 'agribisnis', 'peternakan', 'ternak', 'tanah', 'proteksi tanaman', 'kehutanan', 'agronomi']):
        if 'peternakan' in n or 'ternak' in n:
            desc_id = f"Program studi {nama} ({j}) mendalami nutrisi dan pakan ternak, pemuliaan genetik hewan, teknologi reproduksi, manajemen peternakan komersial, serta pengolahan produk hewani yang higienis."
            desc_en = f"The {nama} ({j}) program studies animal nutrition, livestock genetics, reproductive technologies, sustainable farm management, and hygienic processing of animal-derived products."
            fokus_id = ["Ilmu Nutrisi & Teknologi Pakan Ternak", "Pemuliaan & Genetika Ternak Tropis", "Teknologi Hasil Ternak (Daging, Susu, Telur)", "Manajemen Agribisnis & Peternakan Modern"]
            fokus_en = ["Animal Nutrition & Feed Technology", "Tropical Livestock Breeding & Genetics", "Dairy, Meat & Egg Processing Technology", "Commercial Farm & Livestock Business Management"]
            karir_id = ["Manajer Operasional Peternakan / Feedmill", "Formulator Pakan Ternak (Feed Formulator)", "Breeding Specialist di Perusahaan Peternakan", "Wirausahawan Peternakan Modern", "Penyuluh & Peneliti Peternakan"]
            karir_en = ["Livestock Farm / Feedmill Operations Manager", "Animal Nutrition & Feed Formulator", "Livestock Breeding Specialist", "Modern Agribusiness Entrepreneur", "Livestock Extension Officer / Researcher"]
        elif 'agribisnis' in n:
            desc_id = f"Program studi {nama} ({j}) mengintegrasikan ilmu pertanian dengan ekonomi bisnis, manajemen rantai pasok komoditas pangan, pemasaran pertanian digital, dan evaluasi kelayakan usaha tani."
            desc_en = f"The {nama} ({j}) program integrates agricultural science with agribusiness economics, food supply chain logistics, digital agricultural marketing, and farm venture feasibility appraisal."
            fokus_id = ["Ekonomi Pertanian & Analisis Usahatani", "Manajemen Rantai Pasok Pangan (Food Supply Chain)", "Pemasaran Produk Pertanian & Agribisnis Digital", "Kebijakan Pertanian & Pembangunan Pedesaan"]
            fokus_en = ["Agricultural Economics & Farm Financial Analysis", "Food Supply Chain & Commodity Logistics", "Agricultural Marketing & Digital Agribusiness", "Agricultural Policy & Rural Development"]
            karir_id = ["Manajer Agribisnis & Perusahaan Pertanian", "Supply Chain Analyst Komoditas Pertanian", "Konsultan Usahatani & Perbankan Pertanian", "Wirausahawan Produk Pangan Inovatif", "Perencana Pembangunan Pertanian"]
            karir_en = ["Agribusiness & Estate Farm Manager", "Agricultural Supply Chain Analyst", "Agricultural Banking & Credit Consultant", "Agri-Food Entrepreneur", "Rural Agriculture Development Planner"]
        else: # Agroteknologi / Tanah / Proteksi Tanaman
            desc_id = f"Program studi {nama} ({j}) memfokuskan inovasi budidaya tanaman presisi, kesuburan tanah dan nutrisi tanaman, bioteknologi pertanian, pengendalian hama terpadu, dan adaptasi perubahan iklim."
            desc_en = f"The {nama} ({j}) program focuses on precision crop cultivation, soil health and fertility, plant biotechnology, integrated pest management (IPM), and climate-resilient farming."
            fokus_id = ["Agronomi & Rekayasa Budidaya Tanaman Tropis", "Ilmu Kesuburan Tanah, Nutrisi & Konservasi Lahan", "Proteksi Tanaman & Pengendalian Hayati Hama/Penyakit", "Bioteknologi Pertanian & Smart Farming Berkelanjutan"]
            fokus_en = ["Agronomy & Tropical Crop Production", "Soil Fertility, Plant Nutrition & Conservation", "Plant Protection & Biological Pest Management", "Agricultural Biotechnology & Sustainable Smart Farming"]
            karir_id = ["Agronomis / Field Crop Specialist", "Manajer Perkebunan Kelapa Sawit / Hortikultura", "Peneliti Pemuliaan Tanaman & Benih", "Konsultan Pengendalian Hama & Kesuburan Tanah", "Spesialis Pertanian Presisi (Smart Farming)"]
            karir_en = ["Agronomist / Field Crop Specialist", "Plantation / Horticultural Estate Manager", "Plant Breeding & Seed Researcher", "Soil Fertility & Pest Management Consultant", "Precision Agriculture Specialist"]

    # 12. Natural Sciences & Mathematics (FMIPA)
    elif fac == 'FMIPA' or any(k in n for k in ['matematika', 'fisika', 'kimia', 'biologi', 'statistika']):
        if 'statistika' in n:
            desc_id = f"Program studi {nama} ({j}) mempelajari inferensi statistika, pemodelan data, analisis regresi multivariat, riset operasional, data mining, dan statistika aktuaria untuk pemecahan masalah empiris."
            desc_en = f"The {nama} ({j}) program covers statistical inference, mathematical modeling, multivariate regression, operations research, data mining, and actuarial statistics for empirical problem-solving."
            fokus_id = ["Statistika Matematika & Teori Peluang", "Analisis Data Multivariat & Time Series", "Metode Survei & Riset Operasi", "Statistika Komputasi & Data Mining"]
            fokus_en = ["Mathematical Statistics & Probability Theory", "Multivariate & Time Series Analysis", "Survey Sampling & Operations Research", "Computational Statistics & Data Mining"]
            karir_id = ["Statistisi / Data Analyst", "Aktuaris (Actuarial Analyst)", "Market Researcher & Polling Analyst", "Risk Analyst di Industri Finansial", "Peneliti Kuantitatif"]
            karir_en = ["Statistician / Data Analyst", "Actuarial Analyst", "Market Research & Polling Methodologist", "Risk Analyst (Financial / Insurance)", "Quantitative Researcher"]
        elif 'biologi' in n:
            desc_id = f"Program studi {nama} ({j}) mengkaji biosains dari tingkat molekuler, genetika, mikrobiologi, hingga ekologi lingkungan dan konservasi keanekaragaman hayati tropis."
            desc_en = f"The {nama} ({j}) program investigates biosciences from molecular biology, genetics, and microbiology to environmental ecology and tropical biodiversity conservation."
            fokus_id = ["Biologi Molekuler & Genetika Organisme", "Mikrobiologi Terapan & Bioteknologi", "Ekologi & Konservasi Keanekaragaman Hayati", "Fisiologi Tumbuhan & Hewan"]
            fokus_en = ["Molecular Biology & Genetics", "Applied Microbiology & Biotechnology", "Ecology & Biodiversity Conservation", "Plant & Animal Physiology"]
            karir_id = ["Biosains Researcher / Peneliti Biologi", "Quality Control / Mikrobiolog di Industri Pangan/Farmasi", "Spesialis Konservasi Lingkungan", "Kurator Spesimen Hayati", "Akademisi Biologi"]
            karir_en = ["Bioscience Researcher", "Industrial Microbiologist / QA Microbiologist", "Environmental Conservation Specialist", "Biological Specimen Curator", "Biology Academician"]
        elif 'kimia' in n:
            desc_id = f"Program studi {nama} ({j}) mendalami kimia organik, anorganik, analitik, biokimia, dan kimia material nano untuk sintesis senyawa baru dan analisis instrumen modern."
            desc_en = f"The {nama} ({j}) program examines organic, inorganic, analytical, biochemical, and nanomaterial chemistry for novel compound synthesis and advanced instrumental analysis."
            fokus_id = ["Kimia Analitik & Spektroskopi Instrumen", "Sintesis Kimia Organik & Anorganik", "Biokimia & Kimia Bahan Alam", "Kimia Material, Katalis & Nanoteknologi"]
            fokus_en = ["Analytical Chemistry & Instrumental Spectroscopy", "Organic & Inorganic Chemical Synthesis", "Biochemistry & Natural Product Chemistry", "Material Chemistry, Catalysis & Nanotechnology"]
            karir_id = ["Chemist / Analis Kimia Laboratorium", "R&D Chemist di Industri Kosmetik/Farmasi/Polimer", "Quality Assurance / Quality Control (QA/QC) Specialist", "Peneliti Sains Material", "Konsultan Pengujian Lingkungan"]
            karir_en = ["Laboratory Analytical Chemist", "R&D Industrial Chemist (Cosmetics/Polymer/Pharma)", "QA/QC Chemical Specialist", "Materials Science Researcher", "Environmental Testing Consultant"]
        elif 'fisika' in n:
            desc_id = f"Program studi {nama} ({j}) mempelajari mekanika kuantum, elektrodinamika, fisika material maju, instrumentasi elektronika, geofisika, dan fisika komputasi."
            desc_en = f"The {nama} ({j}) program covers quantum mechanics, electrodynamics, advanced materials physics, electronic instrumentation, geophysics, and computational physics."
            fokus_id = ["Fisika Teoretik & Komputasi", "Fisika Material Maju & Semikonduktor", "Elektronika & Instrumentasi Sensor", "Geofisika & Fisika Lingkungan"]
            fokus_en = ["Theoretical & Computational Physics", "Advanced Materials Physics & Semiconductors", "Electronics & Sensor Instrumentation", "Geophysics & Environmental Physics"]
            karir_id = ["Fisikawan Riset / R&D Scientist", "Instrumentasi & Metrology Engineer", "Geofisikawan di Sektor Eksplorasi Energi", "Data Scientist / Computational Modeler", "Akademisi Fisika"]
            karir_en = ["Research Physicist / R&D Scientist", "Instrumentation & Metrology Engineer", "Exploration Geophysicist", "Data Scientist / Computational Modeler", "Physics Academician"]
        else: # Matematika
            desc_id = f"Program studi {nama} ({j}) membina kemampuan berpikir logis dan analitis abstrak melalui aljabar murni, analisis matematika, matematika diskrit, kriptografi, dan pemodelan matematika terapan."
            desc_en = f"The {nama} ({j}) program develops rigorous logical and abstract reasoning through pure algebra, mathematical analysis, discrete mathematics, cryptography, and applied mathematical modeling."
            fokus_id = ["Aljabar Abstrak & Analisis Riil / Kompleks", "Pemodelan Matematika & Sistem Dinamik", "Matematika Diskrit, Optimasi & Kriptografi", "Komputasi Matematika & Algoritma Numerik"]
            fokus_en = ["Abstract Algebra & Real / Complex Analysis", "Mathematical Modeling & Dynamical Systems", "Discrete Mathematics, Optimization & Cryptography", "Scientific Computing & Numerical Algorithms"]
            karir_id = ["Kuantitatif Analyst (Finansial / Perbankan)", "Cryptographer / Analis Keamanan Data", "Operations Research Analyst", "Pendidik & Peneliti Matematika", "Algorithm Engineer"]
            karir_en = ["Quantitative Analyst (Finance / Tech)", "Cryptographer / Data Security Analyst", "Operations Research Analyst", "Mathematics Educator / Researcher", "Algorithm Engineer"]

    # 13. Teacher Training & Education (FKIP)
    elif fac == 'FKIP' or 'pendidikan' in n or 'pgsd' in n or 'pgpaud' in n:
        subj = nama.replace('Pendidikan', '').replace('S1', '').replace('S2', '').replace('S3', '').strip()
        if 'pgsd' in n or 'guru sekolah dasar' in n:
            kebumen_tag = " di Kampus PSDKU Kebumen" if "kebumen" in n else ""
            desc_id = f"Program studi {nama} ({j}){kebumen_tag} mencetak pendidik profesional sekolah dasar yang menguasai pembelajaran tematik integratif, psikologi perkembangan anak, manajemen kelas, dan inovasi kurikulum SD."
            desc_en = f"The {nama} ({j}) program{kebumen_tag} trains professional primary school educators skilled in integrative thematic pedagogy, child developmental psychology, classroom management, and elementary curriculum innovation."
            fokus_id = ["Pembelajaran Tematik Terpadu SD", "Psikologi Perkembangan & Bimbingan Anak SD", "Pengembangan Kurikulum & Bahan Ajar Inovatif", "Evaluasi Pembelajaran & Manajemen Kelas"]
            fokus_en = ["Integrated Thematic Elementary Pedagogy", "Child Developmental Psychology & Guidance", "Elementary Curriculum & Learning Media Design", "Classroom Management & Educational Assessment"]
            karir_id = ["Guru Kelas Sekolah Dasar (SD/MI)", "Pengembang Media & Kurikulum Pembelajaran SD", "Kepala Sekolah / Pengawas Pendidikan Dasar", "Konsultan Pendidikan Anak Usia Dasar", "Peneliti Pendidikan Dasar"]
            karir_en = ["Elementary / Primary School Teacher", "Elementary Curriculum & EdTech Developer", "Primary School Principal / Inspector", "Child Education Consultant", "Primary Education Researcher"]
        elif 'paud' in n:
            desc_id = f"Program studi {nama} ({j}) mendidik guru dan konsultan anak usia dini yang ahli dalam stimulasi tumbuh kembang anak, neurosains pembelajaran usia dini, permainan edukatif, dan parenting."
            desc_en = f"The {nama} ({j}) program trains early childhood educators and specialists in holistic child development stimulation, early learning neuroscience, educational play, and parenting partnerships."
            fokus_id = ["Stimulasi Tumbuh Kembang & Neurosains Anak Usia Dini", "Desain Alat Permainan Edukatif (APE)", "Manajemen PAUD & Kemitraan Keluarga", "Asesmen Tumbuh Kembang Anak"]
            fokus_en = ["Early Childhood Developmental Neuroscience", "Educational Play & Toy Design", "Early Childhood Center Management & Parenting", "Early Development Assessment Methods"]
            karir_id = ["Pendidik PAUD / TK Profesional", "Konsultan Pengasuhan & Tumbuh Kembang Anak", "Pengelola / Pengusaha Lembaga PAUD", "Perancang Media & Permainan Edukasi", "Peneliti Pendidikan Usia Dini"]
            karir_en = ["Early Childhood / Kindergarten Educator", "Child Development & Parenting Consultant", "Early Learning Center Director / Owner", "Educational Media & Toy Designer", "Early Childhood Education Researcher"]
        elif 'luar biasa' in n or 'khusus' in n:
            desc_id = f"Program studi {nama} ({j}) membekali pendidik inklusif dengan keahlian asesmen anak berkebutuhan khusus, adaptasi kurikulum individual (PPI), braille, bahasa isyarat, dan intervensi rehabilitasi."
            desc_en = f"The {nama} ({j}) program equips inclusive educators with expertise in special needs assessment, individualized educational programs (IEP), braille, sign language, and rehabilitative interventions."
            fokus_id = ["Asesmen Anak Berkebutuhan Khusus (ABK)", "Program Pembelajaran Individual (PPI) & Kurikulum Inklusif", "Bahasa Isyarat, Orientasi Mobilitas & Braille", "Teknologi Asistif & Intervensi Perilaku"]
            fokus_en = ["Special Needs Assessment & Diagnostics", "Individualized Education Programs (IEP) & Inclusive Curricula", "Sign Language, Orientation & Mobility, and Braille", "Assistive Technologies & Behavioral Interventions"]
            karir_id = ["Guru Sekolah Luar Biasa (SLB)", "Guru Pembimbing Khusus (GPK) di Sekolah Inklusi", "Konsultan Terapi & Pendidikan ABK", "Pengembang Teknologi Aksesibilitas Pembelajaran", "Peneliti Pendidikan Khusus"]
            karir_en = ["Special Education School Teacher", "Special Needs Coordinator in Inclusive Schools", "Special Needs Educational Therapist / Consultant", "Educational Accessibility Developer", "Special Education Researcher"]
        elif 'bimbingan' in n:
            desc_id = f"Program studi {nama} ({j}) mendidik konselor profesional dan guru BK yang menguasai teknik konseling individual dan kelompok, asesmen psikopedagogis, serta bimbingan karir dan sosial-pribadi."
            desc_en = f"The {nama} ({j}) program prepares professional school counselors with expertise in individual and group counseling, psychopedagogical assessment, and career/social-personal guidance."
            fokus_id = ["Teori & Teknik Konseling Individual / Kelompok", "Asesmen Psikologis & Pemetaan Potensi Siswa", "Bimbingan Karir & Perencanaan Masa Depan", "Manajemen Pelayanan Bimbingan Konseling Sekolah"]
            fokus_en = ["Individual & Group Counseling Techniques", "Psychological Assessment & Student Profiling", "Career Guidance & Life Planning", "School Guidance & Counseling Program Management"]
            karir_id = ["Guru Bimbingan dan Konseling (BK) di Sekolah", "Konselor Pendidikan & Remaja", "Konsultan Pengembangan Diri & Karir", "Human Resource Development / Counselor Korporat", "Fasilitator Kesehatan Mental Komunitas"]
            karir_en = ["School Guidance Counselor", "Educational & Youth Counselor", "Life Skills & Career Development Consultant", "Corporate HR Counselor", "Community Mental Health Facilitator"]
        else:
            desc_id = f"Program studi {nama} ({j}) mendidik calon guru dan praktisi pendidikan yang menguasai substansi keilmuan {subj}, metodologi pengajaran modern, evaluasi belajar, dan pemanfaatan media digital."
            desc_en = f"The {nama} ({j}) program trains educators and pedagogy specialists with deep mastery of {subj}, modern teaching methodologies, educational evaluation, and digital learning media."
            fokus_id = [f"Substansi Bidang Keilmuan {subj}", "Perencanaan Pembelajaran & Desain Kurikulum", "Pengembangan Media Interaktif & Pembelajaran Digital", "Asesmen & Evaluasi Hasil Belajar"]
            fokus_en = [f"Core Academic Disciplines of {subj}", "Lesson Planning & Instructional Design", "Interactive Media & Digital Learning Technologies", "Educational Assessment & Learning Analytics"]
            karir_id = [f"Guru Mata Pelajaran {subj} di SMP/SMA/SMK", "Pengembang Kurikulum & Modul Pembelajaran", "Instruktur Pelatihan Akademik", "Penulis Buku Pendidikan & Konten Edukasi", "Peneliti Pendidikan"]
            karir_en = [f"Secondary School Teacher in {subj}", "Curriculum & Educational Module Developer", "Academic Training Instructor", "Educational Book Author & Content Creator", "Educational Researcher"]

    # 14. Postgraduate School (SPS) & Multidisciplinary
    elif fac == 'SPS' or any(k in n for k in ['lingkungan', 'penyuluhan pembangunan', 'kependudukan']):
        desc_id = f"Program pascasarjana multidisiplin {nama} ({j}) mengintegrasikan kajian ekologi, kebijakan tata kelola sumber daya alam, pembangunan berkelanjutan (SDGs), dan resolusi konflik sosial-lingkungan."
        desc_en = f"The multidisciplinary postgraduate {nama} ({j}) program integrates ecological science, natural resource governance, sustainable development goals (SDGs), and socio-environmental conflict resolution."
        fokus_id = ["Ekologi Terapan & Valuasi Ekonomi Sumber Daya", "Hukum, Kebijakan Lingkungan & AMDAL", "Manajemen Pembangunan Berkelanjutan (SDGs)", "Pemberdayaan Masyarakat & Ketahanan Iklim"]
        fokus_en = ["Applied Ecology & Environmental Resource Valuation", "Environmental Law, Policy & Impact Assessment (EIA)", "Sustainable Development Management (SDGs)", "Community Empowerment & Climate Resilience"]
        karir_id = ["Pakar Kebijakan Lingkungan & Keberlanjutan (ESG Specialist)", "Konsultan AMDAL & Audit Lingkungan", "Peneliti Lembaga Riset Nasional / Internasional", "Pimpinan Lembaga Swadaya Masyarakat (NGO)", "Akademisi Pascasarjana"]
        karir_en = ["Environmental Policy & ESG Specialist", "EIA & Environmental Audit Consultant", "National / International Research Scientist", "NGO / Sustainability Program Director", "Postgraduate Academician"]

    # 15. General Fallback
    else:
        rumpun_label = "Sains & Teknologi" if "Saintek" in rumpun else ("Sosial & Humaniora" if "Soshum" in rumpun else "Keilmuan Terpadu")
        rumpun_label_en = "Science & Technology" if "Saintek" in rumpun else ("Social Sciences & Humanities" if "Soshum" in rumpun else "Integrated Studies")
        desc_id = f"Program studi {nama} ({j}) di {fakultas_singkatan} UNS memberikan pendidikan berkualitas tinggi dalam rumpun {rumpun_label}, memadukan teori ilmiah mutakhir dengan aplikasi praktis untuk kemaslahatan masyarakat."
        desc_en = f"The {nama} ({j}) program at {fakultas_singkatan} UNS provides high-caliber education in {rumpun_label_en}, integrating cutting-edge academic theory with practical applications for societal benefit."
        fokus_id = ["Fondasi Keilmuan & Metodologi Riset", "Aplikasi Praktis & Pemecahan Masalah Industri", "Etika Profesi & Kepemimpinan Berkelanjutan", "Inovasi & Publikasi Ilmiah"]
        fokus_en = ["Scientific Foundations & Research Methodology", "Practical Application & Problem-Solving", "Professional Ethics & Sustainable Leadership", "Innovation & Scholarly Publication"]
        karir_id = ["Praktisi Profesional di Bidangnya", "Peneliti & Akademisi", "Konsultan Spesialis", "Wirausahawan Inovatif", "Aparatur Sektor Publik & Korporasi"]
        karir_en = ["Professional Practitioner in the Field", "Researcher & Academician", "Specialist Consultant", "Innovative Entrepreneur", "Public Sector & Corporate Leader"]

    return {
        "deskripsi": {
            "id": desc_id,
            "en": desc_en
        },
        "fokus_studi": {
            "id": fokus_id,
            "en": fokus_en
        },
        "prospek_karir": {
            "id": karir_id,
            "en": karir_en
        }
    }
