# 🤖 AI Resume Screening System using Machine Learning
# 📌 Project Overview

The **AI Resume Screening System** is a Machine Learning and Natural Language Processing (NLP) based web application designed to automate the initial resume screening process. Recruiters often receive hundreds of resumes for a single job opening, making manual evaluation time-consuming and prone to human error.

This project intelligently compares candidate resumes with recruiter-provided job descriptions using **TF-IDF (Term Frequency–Inverse Document Frequency)** and **Cosine Similarity** algorithms. Based on the comparison, the system generates an **ATS (Applicant Tracking System) Score**, identifies **matched and missing skills**, and provides a recommendation about the candidate's suitability for the role.

The application features a user-friendly web interface built with **Flask**, allowing recruiters to upload PDF resumes, enter job descriptions, and receive instant screening results.

---

# 🎯 Problem Statement

Recruiters spend significant time reviewing resumes manually, especially when there are hundreds of applicants for a single position. Traditional screening methods are slow, inconsistent, and may overlook qualified candidates.

This project aims to automate the resume screening process using Machine Learning techniques, helping recruiters shortlist candidates efficiently while providing applicants with insights into how well their resumes match job requirements.

---

# ✨ Objectives

* Automate the resume screening process.
* Reduce recruiter workload.
* Improve candidate shortlisting accuracy.
* Calculate ATS compatibility score.
* Compare resumes with job descriptions.
* Extract technical and soft skills automatically.
* Display matched and missing skills.
* Provide candidate recommendations.
* Demonstrate practical application of Machine Learning and NLP.

---

# 🚀 Features

* 📄 Upload Resume in PDF Format
* 📝 Enter Job Description
* 📚 Automatic Resume Text Extraction
* 🧹 Text Preprocessing
* 🧠 Skill Extraction
* 📊 TF-IDF Vectorization
* 📈 Cosine Similarity Calculation
* 🎯 ATS Score Generation
* ✅ Matched Skills Detection
* ❌ Missing Skills Identification
* 💡 Candidate Recommendation
* 🌐 Interactive Flask Web Application

---

# 🛠️ Technologies Used

### Programming Language

* Python

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Flask

### Machine Learning

* Scikit-learn

### NLP

* TF-IDF Vectorizer
* Cosine Similarity

### PDF Processing

* PDFPlumber

### Python Libraries

* Flask
* pdfplumber
* scikit-learn
* pandas
* numpy
* re
* os

---

# ⚙️ System Workflow

1. Recruiter uploads candidate resume.
2. Recruiter enters job description.
3. Resume text is extracted using PDFPlumber.
4. Resume and job description undergo preprocessing.
5. Skills are extracted from both documents.
6. TF-IDF converts text into numerical vectors.
7. Cosine Similarity compares both vectors.
8. ATS Score is calculated.
9. Matched and missing skills are identified.
10. Candidate recommendation is displayed.

---

# 🧠 Machine Learning Algorithms

## 1️⃣ TF-IDF (Term Frequency–Inverse Document Frequency)

TF-IDF is a feature extraction technique used in Natural Language Processing.

It converts textual information into numerical vectors while assigning higher importance to meaningful words and reducing the importance of common words.

### Components

### Term Frequency (TF)

Measures how frequently a word appears in a document.

Example:
If **Python** appears multiple times in the resume, it receives a higher TF value.

### Inverse Document Frequency (IDF)

Reduces the weight of commonly occurring words such as:

* the
* is
* and
* with

This emphasizes important keywords like:

* Python
* Machine Learning
* SQL
* Flask
* Data Analysis
* Communication

The output is a numerical vector representation of the text.

---

## 2️⃣ Cosine Similarity

Cosine Similarity measures how similar two documents are by calculating the cosine of the angle between their TF-IDF vectors.

### Formula

Similarity = (A · B) / (||A|| × ||B||)

### Score Interpretation

| Score     | Meaning         |
| --------- | --------------- |
| 1.0       | Perfect Match   |
| 0.8–0.9   | Excellent Match |
| 0.6–0.8   | Good Match      |
| Below 0.5 | Low Match       |

---

# 🎯 ATS Score

The ATS Score represents how closely the resume matches the job description.

The score is generated using:

* Cosine Similarity Score
* Extracted Skills
* Resume Content Matching

A higher ATS score indicates better compatibility with the job requirements.

---

# 🔍 Skill Extraction

The system compares technical and soft skills from both the resume and job description.

Example Output

### Matched Skills

* Python
* Machine Learning
* Flask
* HTML
* CSS

### Missing Skills

* Docker
* AWS
* Kubernetes

---

# 📂 Project Structure

```text
AI-Resume-Screening-System/
│
├── app.py
├── requirements.txt
├── README.md
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── index.html
│   └── result.html
├── uploads/
├── models/
├── utils/
└── dataset/
```

---

# ▶️ Installation

```bash
git clone https://github.com/yourusername/AI-Resume-Screening-System.git

cd AI-Resume-Screening-System

pip install -r requirements.txt

python app.py
```

Open your browser:

```text
http://127.0.0.1:5000/
```

---

# 📊 Future Enhancements

* Deep Learning-based Resume Ranking
* BERT/Sentence Transformers for Semantic Matching
* OCR Support for Scanned Resumes
* Multi-language Resume Analysis
* Resume Formatting Suggestions
* Recruiter Dashboard
* Resume Database Integration
* Cloud Deployment
* User Authentication
* Email Notifications

---

# 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Machine Learning
* Natural Language Processing
* TF-IDF Feature Extraction
* Cosine Similarity
* Resume Parsing
* Flask Web Development
* PDF Processing
* Skill Extraction
* ATS Score Generation
* End-to-End AI Application Development

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👩‍💻 Author

**V. Lakshmi Kala**

🎓 B.Tech – Computer Science and Engineering

💡 Passionate about Artificial Intelligence, Machine Learning, Cloud Computing, and Full-Stack Development.

---

## ⭐ If you found this project helpful, please give it a Star on GitHub!

Contributions, suggestions, and feedback are always welcome.
