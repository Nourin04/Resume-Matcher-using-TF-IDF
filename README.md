# Resume-Matcher-using-TF-IDF



This project is a smart resume scanning tool that compares multiple resumes against a job description and ranks them based on relevance using **TF-IDF** and **Cosine Similarity**. Built with **Streamlit** for an intuitive web interface, it supports `.pdf` and `.txt` resumes and provides real-time matching results.

---

## 🔍 About the Project

Manually screening resumes is time-consuming and error-prone. This project helps **automate** the process by analyzing the **textual similarity** between a job description and each candidate's resume using **natural language processing (NLP)**.

It uses:
- **TF-IDF (Term Frequency – Inverse Document Frequency)** to vectorize text
- **Cosine Similarity** to calculate how similar each resume is to the job description
- A **Streamlit** frontend for real-time interaction

---

## Demo


![image](https://github.com/user-attachments/assets/0a5b115e-4fff-4b3e-bd78-039e4b9cfe3f)

---

## Features

✅ Upload multiple resumes (.pdf or .txt)  
✅ Paste or type in a job description  
✅ Compute similarity scores using TF-IDF  
✅ Rank resumes by relevance  
✅ View resume previews directly in the browser  
✅ Download top-matching results as CSV  
✅ Fast, model-free — no training required

---

## Tech Stack

| Tool           | Purpose                                |
|----------------|----------------------------------------|
| `Python`       | Core programming language              |
| `scikit-learn` | TF-IDF vectorization & similarity calc |
| `Streamlit`    | Web app framework                      |
| `pdfplumber`   | Extract text from PDF resumes          |
| `pandas`       | Data handling and display              |

---

## How it Works

1. All uploaded resumes and the job description are converted to lowercase text.
2. TF-IDF is used to encode the job description and all resumes into numerical vectors.
3. Cosine similarity compares the vectors of each resume against the job description.
4. Resumes are sorted by similarity scores (from 0 to 1).
5. Top matches are displayed along with their score and preview.

---

## File Structure

```

resume-matcher/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Dependencies
├── sample\_resumes/       # Folder to keep sample resumes
└── README.md             # Project documentation

````

---

## 🔧 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/resume-matcher.git
cd resume-matcher
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Download/Prepare Resumes

* Add some `.pdf` or `.txt` files into a folder or upload them through the interface.

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

## Sample Input

### Job Description

```
We are looking for a machine learning intern with knowledge of NLP, deep learning, and Python. Experience with spaCy, Transformers, or TensorFlow is a plus.
```

### 📄 Resume Matches

* A resume mentioning "NLP", "transformers", and "Python" gets a high score (e.g., 0.82)
* A resume focused on "React", "web design", or "JavaScript" gets a lower score (e.g., 0.35)

---

## Understanding Similarity Scores

* Scores range from **0 to 1**
* Closer to **1** = better match
* Example:

  * `0.91` → Excellent match
  * `0.62` → Moderate match
  * `0.30` → Poor match

---





## Contributing

Pull requests and feedback are welcome. Please open an issue first to discuss your ideas or improvements.




