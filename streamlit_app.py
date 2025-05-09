import streamlit as st
import os
import re
from docx import Document
from bundle import replace_placeholders_and_generate

st.set_page_config(layout="wide")
st.title("📄 DocAutoFactory – Modular RFP Builder")

# Upload main template
st.sidebar.header("📥 Upload RFP Template")
template_file = st.sidebar.file_uploader("Upload a .docx Template", type=["docx"], key="template")

# Placeholders that should be entered as text only (not files)
TEXT_ONLY_FIELDS = {"CUSTOMER_NAME", "PARTNER_NAME", "COMPANY_NAME", "CITY_NAME"}

# Folder to store uploaded content
UPLOADS_DIR = "uploaded_modules"
os.makedirs(UPLOADS_DIR, exist_ok=True)

# Step 1 – Detect placeholders
def extract_placeholders(docx_file):
    doc = Document(docx_file)
    full_text = "\n".join([p.text for p in doc.paragraphs])
    matches = re.findall(r"\{(.*?)\}", full_text)
    return sorted(set(matches))

if template_file:
    st.success("✅ Template uploaded")
    placeholders = extract_placeholders(template_file)
    st.sidebar.subheader("🔍 Found Placeholders")
    for ph in placeholders:
        st.sidebar.markdown(f"- `{ph}`")

    st.divider()
    st.subheader("📤 Upload or Enter Module Content")

    uploaded_data = {}
    for ph in placeholders:
        st.markdown(f"**{ph}**")
        if ph in TEXT_ONLY_FIELDS:
            uploaded_data[ph] = st.text_input(f"Enter value for {ph}", key=ph)
        else:
            uploaded_file = st.file_uploader(f"Upload file for {ph}", type=None, key=ph)
            if uploaded_file:
                file_path = os.path.join(UPLOADS_DIR, f"{ph}_{uploaded_file.name}")
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.read())
                uploaded_data[ph] = file_path
        st.divider()

    # Step 2 – Submit button
    if st.button("🧩 Generate Final Document"):
        output_path = "Final_RFP_Output.docx"
        template_file.seek(0)  # reset stream
        replace_placeholders_and_generate(template_file, uploaded_data, output_path)
        st.success("✅ Document Generated!")
        with open(output_path, "rb") as f:
            st.download_button("📥 Download Final RFP", f, file_name=output_path)


