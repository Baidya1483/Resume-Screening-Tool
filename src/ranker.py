from sentence_transformers import SentenceTransformer, util
from src.extractor import extract_skills  # Corrected link

model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_match_score(jd_text, resume_text, must_have_skills):
    # Semantic Similarity
    embedding1 = model.encode(jd_text)
    embedding2 = model.encode(resume_text)
    similarity = util.cos_sim(embedding1, embedding2).item()
    
    # Skill Coverage
    resume_skills = extract_skills(resume_text)
    matches = sum(1 for s in must_have_skills if s.lower() in resume_skills)
    coverage = matches / len(must_have_skills) if must_have_skills else 0
    
    # Final Weighted Score
    return (0.6 * similarity) + (0.4 * coverage)