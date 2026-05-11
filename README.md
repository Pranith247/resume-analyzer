# 🎯 AI Resume Analyzer & ATS Checker

An AI-powered web application that analyzes resumes against job descriptions and provides detailed ATS (Applicant Tracking System) feedback using Google's Gemini 2.5 Flash model.

## 🚀 Live Demo

> Upload your resume PDF + paste any job description → get instant AI feedback in seconds.

![AI Resume Analyzer](https://img.shields.io/badge/Built%20With-Python%20%7C%20Streamlit%20%7C%20Gemini%20AI-blue)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

---

## ✨ Features

- 📄 **PDF Resume Parsing** — Extracts text from any PDF resume automatically
- 🤖 **AI-Powered Analysis** — Uses Google Gemini 2.5 Flash for intelligent feedback
- 📊 **ATS Match Score** — Get a score out of 100 showing how well your resume fits the JD
- 🔍 **Missing Skills Detection** — Identifies skill gaps between your resume and the job
- 💪 **Strengths & Weaknesses** — Honest breakdown of your profile
- 💡 **Actionable Suggestions** — Specific steps to improve your resume
- 🏷️ **Keyword Recommendations** — Keywords to add for better ATS performance
- 🎯 **Suitable Job Roles** — Alternative roles that better match your profile

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| AI Model | Google Gemini 2.5 Flash |
| PDF Parsing | PyPDF2 |
| Language | Python 3.10+ |
| API SDK | google-genai |

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer.git
cd resume-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

> Get your free API key at: [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📖 How It Works

```
User uploads PDF resume
        ↓
PyPDF2 extracts raw text from the PDF
        ↓
Text + Job Description → structured prompt
        ↓
Gemini 2.5 Flash AI analyzes the content
        ↓
Structured feedback displayed in the UI
```

1. **PDF Extraction** — `PyPDF2.PdfReader` reads each page and extracts text
2. **Prompt Engineering** — Resume text and JD are injected into a carefully crafted prompt
3. **AI Analysis** — Gemini 2.5 Flash processes the prompt via the Google Gen AI SDK
4. **Result Display** — Streamlit renders the markdown response in a clean UI

---

## 📁 Project Structure

```
resume-analyzer/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed to Git)
├── .gitignore          # Ignores .env and other sensitive files
└── README.md           # Project documentation
```

---

## 🔮 Future Improvements

- [ ] Visual ATS score gauge/chart
- [ ] Side-by-side resume vs JD comparison view
- [ ] DOCX file support
- [ ] Resume rewriting suggestions with AI
- [ ] Save and compare multiple analyses
- [ ] Deploy to Streamlit Cloud

---

## 👨‍💻 Author

**Pranith Basani**
- GitHub: [@Pranith247](https://github.com/Pranith247)
- Email: pranithbasani3@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
