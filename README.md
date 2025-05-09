# DocFactory – Modular RFP/Assessment Builder

This repository contains a Streamlit application that lets consultants generate complex RFP or assessment deliverables by:
1. Uploading a customer Word template (with `{placeholders}`).
2. Detecting every placeholder wrapped in curly‑braces.
3. Offering upload widgets (any file‑type) for each placeholder **except** core identity fields that are typed in the sidebar (`{CUSTOMER_NAME}`, `{PARTNER_NAME}`, `{CITY_NAME}`, `{COMPANY_NAME}`).
4. Merging the uploaded module content into the template and exporting a filled .docx or .pdf.

> **Why?** Stop copying & pasting decks. Treat documents like code: modular, versioned, automated.

## Quick start

```bash
git clone <your‑repo>
cd docfactory_full
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

The `modules/` folder contains default text files for each uploadable placeholder. Replace or extend as needed.

