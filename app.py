from flask import Flask, render_template, request

from utils.parser import (
    extract_text_from_pdf,
    extract_skills,
    calculate_skill_match,
    get_missing_skills
)

from gemini_helper import get_resume_suggestions

import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        pdf_file = request.files["resume"]

        job_description = request.form["job_description"]

        pdf_path = os.path.join(
            UPLOAD_FOLDER,
            pdf_file.filename
        )

        pdf_file.save(pdf_path)

        resume_text = extract_text_from_pdf(pdf_path)

        resume_skills = extract_skills(resume_text)

        match_score = calculate_skill_match(
            resume_skills,
            job_description
        )

        missing_skills = get_missing_skills(
            resume_skills,
            job_description
        )

        ai_suggestions = get_resume_suggestions(
            resume_text,
            missing_skills
        )

        return render_template(
            "result.html",

            skills=resume_skills,

            score=match_score,

            missing=missing_skills,

            suggestions=ai_suggestions
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)