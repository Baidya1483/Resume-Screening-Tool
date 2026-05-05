import streamlit as st
import os
from src.parser import extract_resume_text
from src.ranker import calculate_match_score

# Define the absolute path to your specific resume
RESUME_PATH = r'D:\APSB\PROJECT\Resume-Screening-Tool\data\sample_resume.pdf'

st.title("📂 Automated Candidate Screener")

# Sidebar for Job Description
jd_input = st.text_area("Enter Job Description", placeholder="e.g., Seeking a Python Developer with SQL skills...")
must_haves = st.multiselect("Must-Have Skills", ["Python", "SQL", "Machine Learning", "FastAPI"])

if st.button("Analyze Local Sample Resume"):
    if os.path.exists(RESUME_PATH):
        # Step 1: Extraction
        text = extract_resume_text(RESUME_PATH)
        
        # Step 2: Scoring
        score = calculate_match_score(jd_input, text, must_haves)
        
        # Step 3: UI Output
        st.success(f"Successfully parsed: {os.path.basename(RESUME_PATH)}")
        st.metric(label="Match Score", value=f"{round(score * 100, 2)}%")
    else:
        st.error(f"File not found at: {RESUME_PATH}. Please verify the path.")