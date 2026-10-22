"""
Automated end-to-end validation test suite for Universitas Sebelas Maret (UNS) Study Programs Directory.
Verifies dataset consistency across JSON, JS, CSV, metadata, admission capacities, DOM contract elements,
and strict zero-emoji compliance.
"""

import os
import json
import csv
import re
import unittest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
INDEX_HTML = os.path.join(ROOT_DIR, "index.html")
README_MD = os.path.join(ROOT_DIR, "README.md")


class TestDatasetIntegrity(unittest.TestCase):
    """Verify integrity, counts, and parity across UNS data files."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(DATA_DIR, "metadata.json"), "r", encoding="utf-8") as f:
            cls.metadata = json.load(f)

        with open(os.path.join(DATA_DIR, "uns_prodi.json"), "r", encoding="utf-8") as f:
            cls.prodi_json = json.load(f)

        with open(os.path.join(DATA_DIR, "uns_prodi.js"), "r", encoding="utf-8") as f:
            content = f.read()
            match_data = re.search(r"window\.UNS_PRODI_DATA\s*=\s*(\[[\s\S]*?\]);", content)
            assert match_data is not None, "uns_prodi.js must define window.UNS_PRODI_DATA"
            cls.prodi_js = json.loads(match_data.group(1))

        with open(os.path.join(DATA_DIR, "uns_prodi.csv"), "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            cls.prodi_csv = list(reader)

    def test_total_counts(self):
        """Verify program counts across metadata, JSON, JS, and CSV."""
        self.assertEqual(self.metadata["total_prodi"], 176)
        self.assertEqual(len(self.prodi_json), 176)
        self.assertEqual(len(self.prodi_js), 176)
        self.assertEqual(len(self.prodi_csv), 176)

    def test_faculty_coverage(self):
        """Ensure all 15 faculties and academic units are represented."""
        expected_faculties = {
            "FATISDA", "FEB", "FH", "FIB", "FISIP", "FK", "FKIP",
            "FKOR", "FMIPA", "FP", "FPSI", "FSRD", "FT", "SPS", "SV"
        }
        found_faculties = {p["fakultas_singkatan"] for p in self.prodi_json}
        self.assertEqual(found_faculties, expected_faculties)

    def test_jenjang_distribution(self):
        """Verify academic degree level breakdown across all programs."""
        counts = {}
        for p in self.prodi_json:
            counts[p["jenjang"]] = counts.get(p["jenjang"], 0) + 1
        self.assertEqual(counts.get("S1"), 77)
        self.assertEqual(counts.get("D3"), 11)
        self.assertEqual(counts.get("D4"), 15)
        self.assertEqual(counts.get("S2"), 51)
        self.assertEqual(counts.get("S3"), 22)

    def test_campus_locations(self):
        """Ensure Surakarta, Kebumen, and Madiun campuses are present."""
        locations = {p["lokasi_kampus"] for p in self.prodi_json}
        self.assertIn("Kampus Utama (Surakarta)", locations)
        self.assertIn("Kampus PSDKU Kebumen", locations)
        self.assertIn("Kampus PSDKU Madiun", locations)

    def test_international_accreditations(self):
        """Verify international accreditation count matches documented statistics."""
        intl_programs = [p for p in self.prodi_json if p.get("akreditasi_internasional")]
        self.assertEqual(len(intl_programs), 36)
        recognized_agencies = {"ASIIN", "AQAS", "FIBAA", "IABEE"}
        for p in intl_programs:
            for agency in p["akreditasi_internasional"]:
                self.assertIn(agency, recognized_agencies, f"Unknown agency {agency} in {p['id']}")

    def test_required_record_fields(self):
        """Verify each program record has non-empty essential keys."""
        required_keys = ["id", "kode_prodi", "nama_prodi", "jenjang", "rumpun", "fakultas", "akreditasi"]
        for p in self.prodi_json:
            for k in required_keys:
                self.assertIn(k, p, f"Missing key {k} in {p.get('id', 'unknown')}")
                self.assertTrue(str(p[k]).strip() != "", f"Empty value for {k} in {p['id']}")

    def test_csv_parity(self):
        """Verify that CSV export contains exact matching records with JSON."""
        csv_ids = [row.get("id") or row.get("\ufeffid") for row in self.prodi_csv]
        json_ids = [p["id"] for p in self.prodi_json]
        self.assertEqual(csv_ids, json_ids)


class TestUIElements(unittest.TestCase):
    """Verify index.html DOM structure, controls, and interactive elements."""

    @classmethod
    def setUpClass(cls):
        with open(INDEX_HTML, "r", encoding="utf-8") as f:
            cls.html = f.read()

    def test_search_and_filter_elements(self):
        """Ensure search inputs, selects, pills, and toggles are present."""
        required_ids = [
            "search-input",
            "faculty-select",
            "rumpun-select",
            "accreditation-select",
            "level-pills",
            "location-select",
            "intl-checkbox",
            "view-grid-btn",
            "view-table-btn",
            "displayed-count",
            "total-count"
        ]
        for elem_id in required_ids:
            self.assertIn(f'id="{elem_id}"', self.html, f"Missing DOM id: {elem_id}")

    def test_metrics_elements(self):
        """Ensure hero metrics cards exist."""
        metric_ids = ["stat-total", "stat-unggul", "stat-intl", "stat-faculty"]
        for elem_id in metric_ids:
            self.assertIn(f'id="{elem_id}"', self.html, f"Missing metric DOM id: {elem_id}")

    def test_modal_elements(self):
        """Ensure detailed modal components exist for prodi inspection."""
        modal_ids = [
            "prodi-modal",
            "modal-close-btn",
            "modal-prodi-name",
            "modal-fakultas-name",
            "modal-desc",
            "modal-focus-list",
            "modal-career-tags",
            "modal-btn-copy",
            "toast",
            "toast-message"
        ]
        for elem_id in modal_ids:
            self.assertIn(f'id="{elem_id}"', self.html, f"Missing modal DOM id: {elem_id}")

    def test_seo_metadata(self):
        """Verify presence of OpenGraph, Twitter Card, and canonical metadata."""
        self.assertIn('<meta name="description"', self.html)
        self.assertIn('<meta property="og:title"', self.html)
        self.assertIn('<meta property="og:description"', self.html)
        self.assertIn('<meta name="twitter:card"', self.html)
        self.assertIn('<link rel="canonical"', self.html)


class TestZeroEmojiCompliance(unittest.TestCase):
    """Strictly assert zero emoji characters across repository files."""

    def test_no_emojis(self):
        files_to_check = [
            INDEX_HTML,
            README_MD,
            os.path.join(ROOT_DIR, "LICENSE"),
            os.path.join(DATA_DIR, "metadata.json"),
            os.path.join(DATA_DIR, "uns_prodi.json"),
            os.path.join(DATA_DIR, "uns_prodi.js"),
            os.path.join(DATA_DIR, "uns_prodi.csv"),
            os.path.join(ROOT_DIR, "scripts", "fetch_uns_data.py"),
            os.path.join(ROOT_DIR, "scripts", "prodi_knowledge.py")
        ]
        for file_path in files_to_check:
            if not os.path.exists(file_path):
                continue
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            emoji_chars = [
                c for c in content
                if ord(c) in range(0x1F300, 0x1FAFF)
                or ord(c) in range(0x2600, 0x27BF)
                or ord(c) in range(0x2300, 0x23FF)
            ]
            self.assertEqual(len(emoji_chars), 0, f"Found emojis in {file_path}: {emoji_chars}")


if __name__ == "__main__":
    unittest.main()
