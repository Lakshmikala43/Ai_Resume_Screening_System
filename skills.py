import re

# List of skills recognized by our AI system
SKILLS = [

    "python",
    "java",
    "c",
    "c++",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "mysql",
    "sql",
    "mongodb",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "nlp",
    "tensorflow",
    "keras",
    "pandas",
    "numpy",
    "scikit-learn",
    "flask",
    "django",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "linux",
    "communication",
    "teamwork",
    "problem solving"
]


def extract_skills(text):
    """
    Extract matching skills from resume/job description.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill)

    return found_skills