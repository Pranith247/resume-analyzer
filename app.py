import streamlit as st
from google import genai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import os

load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("🎯 AI Resume Analyzer & ATS Checker")

# New Google Gen AI SDK - uses genai.Client()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=200)

if st.button("Analyze Resume", type="primary"):
    if resume_file and job_description:
        pdf_reader = PdfReader(resume_file)
        resume_text = ""
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                resume_text += text

        prompt = f"""
You are an expert ATS resume analyzer.

Analyze the following resume against the job description.

Give:
1. ATS Match Score out of 100
2. Missing Skills
3. Strengths
4. Weaknesses
5. Suggestions to Improve
6. Recommended Keywords
7. Suitable Job Roles

Resume:
{resume_text}

Job Description:
{job_description}
"""

        with st.spinner("Analyzing Resume..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",   # correct model name for new SDK
                contents=prompt
            )

        st.success("✅ Analysis Complete!")
        st.markdown(response.text)

    else:
        st.warning("⚠️ Please upload a resume PDF and enter a job description.")
