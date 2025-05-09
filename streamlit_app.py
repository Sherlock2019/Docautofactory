
import streamlit as st, re, os, pathlib, base64
from docx import Document
from collections import defaultdict
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.sidebar.title("DocFactory – Upload inputs")
identity = {}
for key in ["CUSTOMER_NAME","PARTNER_NAME","CITY_NAME","COMPANY_NAME"]:
    identity[key] = st.sidebar.text_input(key.replace("_"," ").title())

st.header("1. Upload main Word template (.docx)")
tpl_file = st.file_uploader("Main template", type=["docx"])

def extract_placeholders(doc_path):
    doc = Document(doc_path)
    text = "\n".join(p.text for p in doc.paragraphs)
    return re.findall(r"{(.*?)}", text)

placeholder_files = defaultdict(lambda: None)

if tpl_file:
    tpl_path = os.path.join(UPLOAD_DIR, "template.docx")
    with open(tpl_path,"wb") as f: f.write(tpl_file.read())
    phs = extract_placeholders(tpl_path)
    st.success(f"Found {len(phs)} placeholders: {', '.join(phs)}")

    st.header("2. Provide content for each placeholder")
    for ph in phs:
        if ph in identity:
            st.info(f"{ph} will be filled from sidebar.")
            continue
        uploaded = st.file_uploader(f"{ph} file", key=ph)
        if uploaded:
            dest = os.path.join(UPLOAD_DIR, f"{ph}_{uploaded.name}")
            with open(dest,"wb") as f: f.write(uploaded.read())
            placeholder_files[ph]=dest

if st.button("Assemble Document") and tpl_file:
    st.write("🔧 Placeholder merge not yet implemented – stub.")
