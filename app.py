import re
from io import BytesIO

import pandas as pd
import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="SmartHire | AI Resume Matcher", page_icon="🧑‍💼", layout="wide")

# A starter skills list. You can expand this as your project grows.
SKILL_TERMS = [
    "python", "java", "c++", "c", "javascript", "typescript", "sql", "mysql",
    "postgresql", "mongodb", "html", "css", "react", "node.js", "flask",
    "django", "streamlit", "machine learning", "deep learning", "artificial intelligence",
    "natural language processing", "nlp", "scikit-learn", "pandas", "numpy",
    "tensorflow", "pytorch", "data analysis", "power bi", "tableau", "excel",
    "git", "github", "docker", "aws", "azure", "linux", "rest api",
    "communication", "teamwork", "problem solving", "project management"
]

def extract_pdf_text(uploaded_file):
    """Read selectable text from a PDF file."""
    try:
        reader = PdfReader(BytesIO(uploaded_file.getvalue()))
        pages = []
        for page in reader.pages:
            pages.append(page.extract_text() or "")
        return "\n".join(pages).strip()
    except Exception as exc:
        st.warning(f"Could not read {uploaded_file.name}: {exc}")
        return ""

def extract_resume_text(uploaded_file):
    name = uploaded_file.name.lower()
    if name.endswith(".pdf"):
        return extract_pdf_text(uploaded_file)
    if name.endswith(".txt"):
        try:
            return uploaded_file.getvalue().decode("utf-8", errors="ignore").strip()
        except Exception:
            return ""
    return ""

def find_skills(text):
    text_lower = text.lower()
    found = []
    for skill in SKILL_TERMS:
        # Match phrase/term boundaries while allowing punctuation in terms.
        pattern = r"(?<![a-z0-9])" + re.escape(skill.lower()) + r"(?![a-z0-9])"
        if re.search(pattern, text_lower):
            found.append(skill)
    return sorted(set(found))

def calculate_scores(job_text, resume_texts):
    """Combine TF-IDF text similarity and skill overlap into an explainable score."""
    all_texts = [job_text] + resume_texts
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    try:
        matrix = vectorizer.fit_transform(all_texts)
        similarities = cosine_similarity(matrix[0:1], matrix[1:]).flatten()
    except ValueError:
        similarities = [0.0] * len(resume_texts)

    job_skills = set(find_skills(job_text))
    results = []
    for idx, resume_text in enumerate(resume_texts):
        resume_skills = set(find_skills(resume_text))
        if job_skills:
            skill_score = len(job_skills & resume_skills) / len(job_skills)
        else:
            skill_score = 0.0
        text_score = float(similarities[idx]) if idx < len(similarities) else 0.0
        # Weighted score: 65% text similarity + 35% listed skill overlap.
        total = (0.65 * text_score + 0.35 * skill_score) * 100
        matched = sorted(job_skills & resume_skills)
        missing = sorted(job_skills - resume_skills)
        results.append({
            "Match score (%)": round(total, 1),
            "Text similarity (%)": round(text_score * 100, 1),
            "Skill overlap (%)": round(skill_score * 100, 1),
            "Matched skills": ", ".join(matched) if matched else "No listed skills matched",
            "Skills not found": ", ".join(missing) if missing else "None from the starter list",
            "_score": total
        })
    return job_skills, results

st.title("🧑‍💼 SmartHire")
st.subheader("AI/ML Resume Screening and Job Matching")
st.write(
    "Compare resumes with a job description using TF-IDF text similarity and a transparent "
    "skills-overlap score. This is a student project prototype, not an automated hiring decision system."
)

with st.sidebar:
    st.header("About this prototype")
    st.write("**NLP method:** TF-IDF + cosine similarity")
    st.write("**Scoring:** 65% text similarity + 35% listed-skill overlap")
    st.info("The score is a text-match indicator only. A recruiter must review the resume and make all hiring decisions.")
    st.caption("Tip: scanned/image-only PDFs may need OCR and may not produce readable text in this version.")

job_title = st.text_input("Job title", placeholder="e.g., Python Developer Intern")
job_description = st.text_area(
    "Paste the job description and required skills",
    height=190,
    placeholder="Example: We need a Python intern with SQL, pandas, machine learning, Git and communication skills."
)

uploaded_files = st.file_uploader(
    "Upload candidate resumes (PDF or TXT)",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

if st.button("Analyze resumes", type="primary", use_container_width=True):
    if not job_description.strip():
        st.error("Please enter a job description before analyzing resumes.")
    elif not uploaded_files:
        st.error("Please upload at least one resume (PDF or TXT).")
    else:
        candidate_names = []
        resume_texts = []
        for file in uploaded_files:
            text = extract_resume_text(file)
            if text:
                candidate_names.append(file.name)
                resume_texts.append(text)
            else:
                st.warning(f"No readable text was found in {file.name}. Try a text-based PDF or TXT file.")

        if not resume_texts:
            st.error("I couldn't extract readable text from the uploaded files.")
        else:
            job_skills, results = calculate_scores(job_description, resume_texts)
            rows = []
            for name, result in zip(candidate_names, results):
                rows.append({
                    "Candidate file": name,
                    "Match score (%)": result["Match score (%)"],
                    "Text similarity (%)": result["Text similarity (%)"],
                    "Skill overlap (%)": result["Skill overlap (%)"],
                    "Matched skills": result["Matched skills"],
                    "Skills not found": result["Skills not found"],
                    "_score": result["_score"]
                })
            df = pd.DataFrame(rows).sort_values("_score", ascending=False).reset_index(drop=True)
            df.insert(0, "Rank", range(1, len(df) + 1))
            st.success(f"Analyzed {len(df)} resume(s) for: {job_title or 'the provided role'}")
            st.write("**Skills detected in the job description:**", ", ".join(sorted(job_skills)) if job_skills else "No terms from the starter skill list were detected.")
            best = df.iloc[0]
            col1, col2, col3 = st.columns(3)
            col1.metric("Resumes analyzed", len(df))
            col2.metric("Top text-match score", f"{best['Match score (%)']}%")
            col3.metric("Skills in job description", len(job_skills))
            st.markdown("### Candidate comparison")
            st.dataframe(df.drop(columns=["_score"]), use_container_width=True, hide_index=True)
            st.markdown("### Match score chart")
            chart_data = df[["Candidate file", "Match score (%)"]].set_index("Candidate file")
            st.bar_chart(chart_data)
            csv = df.drop(columns=["_score"]).to_csv(index=False).encode("utf-8")
            st.download_button("Download results as CSV", data=csv, file_name="smarthire_results.csv", mime="text/csv")
            st.warning(
                "Review the original resumes before making any decision. Scores can be affected by resume wording, "
                "formatting, and the limited starter skill list; they do not measure a person's full ability."
            )

st.divider()
st.caption("SmartHire student prototype • Built with Python, Streamlit, pandas, scikit-learn and pypdf")
