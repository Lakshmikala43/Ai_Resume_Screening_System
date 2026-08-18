from flask import Flask, render_template, request
import os

from resume_parser import extract_text_from_pdf
from skills import extract_skills
from similarity import calculate_similarity, calculate_ats

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder automatically
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -----------------------------
# Analyze Resume
# -----------------------------
@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files["resume"]

    job_description = request.form["job_description"]

    # Save uploaded PDF
    resume_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(resume_path)

    # Extract Resume Text
    resume_text = extract_text_from_pdf(resume_path)

    # Extract Skills
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    # Similarity
    similarity = calculate_similarity(
        resume_text,
        job_description
    )

    # Skill Matching
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    # ATS Score
    ats = calculate_ats(
        similarity,
        len(matched),
        len(jd_skills)
    )

    # Candidate Recommendation
    if ats >= 85:
        status = "Excellent Candidate"

    elif ats >= 70:
        status = "Good Candidate"

    elif ats >= 50:
        status = "Average Candidate"

    else:
        status = "Not Suitable"

    return render_template(
        "result.html",

        similarity=round(similarity,2),

        ats=round(ats,2),

        matched=matched,

        missing=missing,

        status=status
    )

# -----------------------------
# Run Flask
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)