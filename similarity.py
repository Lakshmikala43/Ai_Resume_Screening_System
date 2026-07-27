from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_text, job_description):
    """
    Calculate similarity percentage between resume and job description.
    """

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return similarity * 100


def calculate_ats(similarity, matched_skills, total_required_skills):
    """
    Calculate ATS Score using:
    60% Similarity
    40% Skill Match
    """

    if total_required_skills == 0:
        skill_score = 100
    else:
        skill_score = (
            matched_skills /
            total_required_skills
        ) * 100

    ats_score = (
        similarity * 0.6 +
        skill_score * 0.4
    )

    return ats_score