import pdfplumber
from skills import SKILLS

def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    return text


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text:

            found_skills.append(skill)

    return list(set(found_skills))


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(resume_text, job_description):

    documents = [resume_text, job_description]

    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    score = round(similarity[0][0] * 100, 2)

    return score

def get_missing_skills(resume_skills, job_description):

    job_description = job_description.lower()

    required_skills = []

    for skill in SKILLS:

        if skill.lower() in job_description:

            required_skills.append(skill)

    missing_skills = []

    for skill in required_skills:

        if skill not in resume_skills:

            missing_skills.append(skill)

    return missing_skills

def calculate_skill_match(resume_skills, job_description):

    job_description = job_description.lower()

    required_skills = []

    for skill in SKILLS:

        if skill.lower() in job_description:

            required_skills.append(skill)

    matched_skills = []

    for skill in required_skills:

        if skill in resume_skills:

            matched_skills.append(skill)

    if len(required_skills) == 0:
        return 0

    score = (len(matched_skills) / len(required_skills)) * 100

    return round(score, 2)