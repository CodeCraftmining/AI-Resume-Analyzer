from utils.parser import extract_text_from_pdf
from utils.parser import extract_skills

resume_text = extract_text_from_pdf("sample_resume.pdf")

skills = extract_skills(resume_text)

print("Skills Found:\n")

print(skills)