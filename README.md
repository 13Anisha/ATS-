# 📄 Resume Analyzer using Streamlit & Gemini AI

The **Resume Analyzer** is an intelligent web application built with **Streamlit** and **Google Gemini AI** that evaluates how well a resume aligns with a job description.

It helps:
- Job seekers tailor their resumes to specific roles
- Developers explore the integration of LLMs like Gemini into real apps
- Learn how natural language prompts can power smart web tools

---

## Project Objective

**Why Resume Analyzer?**

Recruiters often rely on **Applicant Tracking Systems (ATS)** that use keyword matching and skill relevance to filter candidates. This tool replicates that logic using **Gemini 1.5 Flash**, giving feedback such as:

- What’s **strong** in your resume
- What’s **missing** based on the job description
- How to **improve skills**
- What **percentage match** your resume has for the job

It’s like having a smart HR assistant that helps optimize your resume for every job!

---

## Features

- Upload a PDF Resume (no DOCX or TXT needed!)
- Extracts and processes resume content using PyMuPDF
- Uses Gemini AI for job description comparison
- Analysis Options:
  - **Resume Evaluation**: Strengths and weaknesses
  - **Missing Keywords**: Keywords not present in resume
  - **Skill Improvement Suggestions**
  - **Job Match Score** (0–100%) like an ATS system
- Clean, modern UI with Streamlit and custom HTML/CSS

---

## How It Works

1. **Upload Resume** (PDF only)
2. **Enter Job Description** in a text box
3. **Choose Analysis Type** (e.g., “Match Score”)
4. App sends your resume & job description to **Google Gemini API** using carefully crafted prompts
5. Gemini returns an intelligent response → displayed to user

---

## Tech Stack

| Technology        | Purpose                                  |
|------------------|------------------------------------------|
| Python 3.10+      | Core backend logic                       |
| Streamlit         | Web framework for UI                    |
| PyMuPDF (fitz)    | PDF resume parsing                       |
| Google Generative AI (Gemini) | LLM for analysis               |



