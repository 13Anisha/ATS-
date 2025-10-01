import streamlit as st
import fitz
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def pdf_text_extractor(uploaded_file):  
    if uploaded_file is not None:
        pdf_data = uploaded_file.read()
        doc = fitz.open(stream=pdf_data, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    else:
        raise FileNotFoundError("File not Uploaded!")

def generate_response(prompt, resume_text, job_input):
    model = genai.GenerativeModel('models/gemini-2.5-pro')
    response = model.generate_content([
        prompt,
        "Resume:\n" + resume_text,
        "Job Description:\n" + job_input
    ])
    return response.text

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    .section-header {
        font-size: 24px !important;
        font-weight: 600;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Resume Analyzing System</div>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>Enter the Job Description</div>", unsafe_allow_html=True)
job_input = st.text_area("", height=120)

st.markdown("<div class='section-header'>Upload Resume</div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully.")

input_prompt_1 = """
You are an experienced HR with tech experience. Review the provided resume against the job description and share a professional evaluation.
Highlight strengths and weaknesses in relation to the role.
Keep it concise and short.
"""

input_prompt_2 = """
Compare the resume to the job description.

List the results in this format:

Job Keywords:
- key skill 1
- key skill 2

Present in Resume:
- skill 1
- skill 2

Missing Keywords:
- skill a
- skill b

Only use bullet points.
"""

input_prompt_3 = """
Find 2–3 important skills that are missing or weak in the resume.

For each skill, say:
- The skill name
- Why it matters
- A short suggestion to improve

Be clear and simple.
"""

input_prompt_4 = """
You are an expert ATS system that calculates a job-resume match score between 0% to 100%.

Instructions:
- Base the score only on skills, experience, keywords, and relevance.
- A generic resume should get 40–60%.
- A highly relevant resume should get 85–95%.

Output format:

**<span style='font-size:30px;'>Match Score: XX%</span>**

### Evaluation Summary:
Give a short summary explaining why this score was given.
"""

st.markdown("<div class='section-header'>Choose an Analysis Option</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    button1 = st.button("Analyze the Resume")
    button2 = st.button("Find Missing Keywords")
with col2:
    button3 = st.button("How Can I Improve My Skills?")
    button4 = st.button("Job Match % Score")

if uploaded_file and job_input:
    resume_text = pdf_text_extractor(uploaded_file)

    if button1:
        st.subheader("Resume Evaluation")
        with st.spinner("Analyzing resume..."):
            response = generate_response(input_prompt_1, resume_text, job_input)
        st.write(response)

    elif button2:
        st.subheader("Missing Keywords from Resume")
        with st.spinner("Extracting keywords..."):
            response = generate_response(input_prompt_2, resume_text, job_input)
        st.write(response)

    elif button3:
        st.subheader("Suggestions to Improve Skills")
        with st.spinner("Identifying skill gaps..."):
            response = generate_response(input_prompt_3, resume_text, job_input)
        st.write(response)

    elif button4:
        st.subheader("Resume Match Score")
        with st.spinner("Calculating match percentage..."):
            response = generate_response(input_prompt_4, resume_text, job_input)
        st.markdown(response, unsafe_allow_html=True)

elif any([button1, button2, button3, button4]):
    st.warning("Please upload a resume and enter a job description before analyzing.")
