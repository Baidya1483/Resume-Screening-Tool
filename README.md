# 📄 Automated Resume Screening Tool

An AI-powered Human Resources (HR) technology tool designed to automate the initial screening of resumes against specific job descriptions. This project utilizes **Natural Language Processing (NLP)** and **Semantic Similarity** to rank candidates objectively based on skill sets and experience.

---

## 🚀 Overview
The **Automated Resume Screening Tool** solves the challenge of manual high-volume recruitment. By extracting structured data from unstructured PDF/DOCX files, the system identifies "Must-Have" skills and calculates a weighted matching score, significantly reducing time-to-shortlist.

### ✨ Key Features
*   **Multi-Format Ingestion**: Supports text extraction from PDF and DOCX resumes using `pdfplumber`.
*   **Skill Extraction Engine**: Uses Regex and NLP to identify industry-specific technical skills.
*   **Semantic Ranking**: Employs **Transformer-based embeddings** (`all-MiniLM-L6-v2`) to understand the context of a candidate's experience beyond simple keyword matching.
*   **Explainable Scoring**: Provides a breakdown of why a candidate was ranked, including "Must-Have" skill coverage and experience verification[cite: 4].
*   **Recruiter Dashboard**: An interactive Streamlit interface for job creation and candidate ranking[cite: 4].

---

## 🛠️ Tech Stack
*   **Language**: Python 3.11+[cite: 4]
*   **NLP & ML**: SpaCy, Sentence-Transformers (BERT variants), Scikit-learn[cite: 4]
*   **Parsing**: PDFPlumber, Python-Docx[cite: 4]
*   **Web Framework**: Streamlit (Frontend), FastAPI (Backend API)[cite: 4]
*   **Database**: SQLite[cite: 4]

---

## 🏗️ Project Structure
```text
Automated-Resume-Screening-Tool/
├── resumes/            # Directory for sample PDF/DOCX resumes[cite: 4]
├── db/                 # SQLite storage for parsed candidate profiles[cite: 4]
├── src/                # Modular Python logic[cite: 4]
│   ├── parser.py       # Document text extraction[cite: 4]
│   ├── extractor.py    # NLP-based skill & entity extraction[cite: 4]
│   └── ranker.py       # Semantic similarity and scoring engine[cite: 4]
├── main.py             # Streamlit Dashboard entry point[cite: 4]
├── requirements.txt    # Project dependencies[cite: 4]
├── .gitignore          # Files excluded from version control[cite: 4]
└── README.md           # Documentation
