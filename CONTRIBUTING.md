# Contributing to Universitas Sebelas Maret (UNS) Study Programs Directory

Thank you for your interest in contributing to the **Universitas Sebelas Maret Study Programs & Accreditation Directory**. We welcome corrections, curriculum updates, and code enhancements from students, researchers, alumni, and academic counselors.

---

## 1. Development Standards & Hygiene

1. **Zero-Emoji Rule:** All source files, comments, markdown documentation, issue templates, and Git commit messages must contain zero emoji characters.
2. **Conventional Commits:** Follow standard conventional commit prefixes:
   - `docs:` for documentation, faculty profiles, admissions guides, or README updates.
   - `feat:` for new UI capabilities, filters, or dataset attributes.
   - `fix:` for data corrections, broken links, or UI bug fixes.
   - `test:` for test additions or validation assertions.
   - `chore:` for repository maintenance, dependencies, or configuration.
3. **Data Parity:** Any modifications to academic programs must be reflected consistently across all three data formats: `data/uns_prodi.json`, `data/uns_prodi.js`, and `data/uns_prodi.csv`.

---

## 2. Local Development & Testing

Run the automated test suite before opening any pull request:

```bash
# Execute unit tests across dataset integrity, DOM contracts, and zero-emoji compliance
python -m unittest discover tests
```

All 12 test cases must pass with `OK` status.

---

## 3. Academic Data Guidelines

When proposing revisions to study program data:
- Verify official accreditation status through the BAN-PT registry, LAM-PTKes, or official SPMB UNS documents (`https://spmb.uns.ac.id`).
- Cite the official SK Akreditasi number and publication date whenever modifying accreditation categories.
- Ensure international accreditation designations follow recognized bodies: ASIIN, AQAS, FIBAA, or IABEE.

---

## 4. Pull Request Guidelines

1. Fork the repository and create a descriptive feature branch:
   ```bash
   git checkout -b docs/add-faculty-profile
   ```
2. Verify all modifications locally using the test suite.
3. Submit a Pull Request targeting the `main` branch with clear references to official UNS publication sources.
