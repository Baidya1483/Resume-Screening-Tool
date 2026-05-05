import re

SKILLS_DB = ["python", "sql", "aws", "machine learning", "fastapi", "react"]

def extract_skills(text):
    text = text.lower()
    found_skills = [skill for skill in SKILLS_DB if re.search(rf'\b{skill}\b', text)]
    return list(set(found_skills))