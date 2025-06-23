import streamlit as st
import os
import PyPDF2
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


# --- Function to read PDF ---
def read_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''
    return text


# --- Function to read TXT ---
def read_txt(file):
    return file.read().decode("utf-8")


# --- Function to process resumes ---
def process_resumes(files):
    resume_texts = []
    resume_names = []

    for file in files:
        file_name = file.name
        if file_name.endswith(".pdf"):
            text = read_pdf(file)
        elif file_name.endswith(".txt"):
            text = read_txt(file)
        else:
            text = ""
        resume_names.append(file_name)
        resume_texts.append(text)

    return resume_names, resume_texts


# --- Function to rank resumes based on similarity ---
def rank_resumes(job_desc, resumes):
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    all_docs = [job_desc] + resumes
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_docs)

    job_vec = tfidf_matrix[0]
    resume_vecs = tfidf_matrix[1:]

    similarity_scores = cosine_similarity(job_vec, resume_vecs).flatten()
    return similarity_scores


# --- Streamlit App ---
st.set_page_config(page_title="Resume Matcher", layout="wide")
st.title("📄 Resume Matcher using TF-IDF")
st.write("Upload a set of resumes and a job description. We'll rank resumes by relevance!")

job_desc = st.text_area("✍️ Paste the Job Description here")

resume_files = st.file_uploader("📁 Upload Resumes (.pdf or .txt)", type=["pdf", "txt"], accept_multiple_files=True)

if st.button("🔍 Match Resumes") and job_desc and resume_files:
    with st.spinner("Analyzing resumes..."):
        names, texts = process_resumes(resume_files)
        scores = rank_resumes(job_desc, texts)

        # Prepare and show results
        results_df = pd.DataFrame({
            "Resume Name": names,
            "Similarity Score": scores
        }).sort_values(by="Similarity Score", ascending=False).reset_index(drop=True)

        st.success("✅ Matching Complete!")
        st.dataframe(results_df)

        top_n = st.slider("📊 Download top N resumes as CSV:", min_value=1, max_value=len(names), value=3)
        top_results = results_df.head(top_n)

        st.download_button(
            label="📥 Download CSV",
            data=top_results.to_csv(index=False).encode("utf-8"),
            file_name="top_matched_resumes.csv",
            mime="text/csv"
        )

        for i, row in top_results.iterrows():
            st.markdown(f"### 🧾 {row['Resume Name']}")
            st.markdown(f"**Similarity Score:** `{row['Similarity Score']:.2f}`")
            st.text_area("Resume Preview", value=texts[names.index(row['Resume Name'])][:1000], height=200)

else:
    st.info("Please enter a job description and upload at least one resume to proceed.")
