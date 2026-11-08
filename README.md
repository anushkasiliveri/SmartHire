# SmartHire — AI/ML Resume Matching Prototype

A beginner-friendly Streamlit project that compares candidate resumes with a job description.

## Features
- Upload multiple PDF or TXT resumes
- Paste a job description
- Extract selectable text from PDFs
- Detect a starter list of skills
- Calculate TF-IDF cosine similarity
- Combine text similarity (65%) and skill overlap (35%)
- Show ranked results, matched/missing listed skills, chart, and CSV export

## Requirements
- Python 3.11–3.13 recommended for easiest package compatibility
- Internet connection for installing packages
- VS Code (recommended)

## Run on Windows

Open Command Prompt or the VS Code terminal inside this folder:

```bash
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Streamlit should open the app in your browser. If it does not, open the local URL shown in the terminal, usually `http://localhost:8501`.

## How the score works
1. TF-IDF converts the job description and each resume into weighted word/phrase vectors.
2. Cosine similarity estimates how similar the resume text is to the job description.
3. Skill overlap checks which terms from the starter skills list occur in both texts.
4. Final score = 65% × text similarity + 35% × skill overlap.

The weights are design choices for this prototype, not scientifically validated hiring criteria. A match score is not a prediction of job performance. Human review is required.

## Limitations
- Scanned/image-only PDFs are not OCR processed.
- The skill list is intentionally small and should be expanded and tested.
- Similarity can be influenced by wording and formatting.
- Do not use protected or sensitive personal traits for ranking.
- This is an educational prototype, not a production hiring system.

## Suggested future improvements
- Add DOCX support
- Add OCR for scanned resumes
- Store jobs and candidate results in SQLite
- Add unit tests and sample test documents
- Evaluate the scoring method on a labeled, consented dataset
- Deploy to Streamlit Community Cloud and link the source repository
