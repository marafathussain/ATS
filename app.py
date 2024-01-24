import streamlit as st
import google.generativeai as genai 
import os
import PyPDF2 as pdf 
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


# Gemini Pro Response Generation
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    
    for page in range(len(reader.pages)):
        page_content = reader.pages[page]
        text += str(page_content.extract_text())
        
    return text

input_prompt = """
Hey, act like a skilled or very experience application racking system (ATS) with deep understanding of the tech field, 
medical imaging, software engineering, data science, data analyst, and big data engineering. Your task is to evaluate a 
resume based on a given job description (JD). You must consider the job market being very competitive and you should provide 
the best assistance to improve the resume. Assign the percentage matching based on the the job description (JD) and missing 
keywords with high accuracy.

resume: {text}
job description: {jd}

I want the response in one single string having the structure
{{"JD Match" : "%"; "Missing Keywords: []"; "Profile Summary" : ""}}
"""

# Streamlit App
st.title("Smart ATS")
st.text("Improve your resume with the help of Gemini Pro")
jd = st.text_area("Paste the job description")
uploaded_file = st.file_uploader("Upload your resume", type = "pdf", help = "Please upload a PDF")

submit = st.button("Submit")


if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader(response)
        