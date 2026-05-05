import pdfplumber

def extract_resume_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return " ".join(text.split()) # Normalizes whitespace