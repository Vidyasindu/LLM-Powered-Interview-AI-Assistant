import os
import streamlit as st

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv

# ---------------- LOAD ENV ---------------- #

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="INTERVIEW AI ASSISTANT WITH LLM ",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* MAIN BACKGROUND */

.stApp {

    background:
    radial-gradient(circle at left, rgba(236,72,153,0.28), transparent 25%),
    radial-gradient(circle at right bottom, rgba(244,63,94,0.28), transparent 25%),
    linear-gradient(135deg,#020617,#030712,#111827);

    color: white;
}

/* REMOVE STREAMLIT DEFAULT */

header, footer {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
    max-width: 1250px;
}

/* NAVBAR */

.navbar {

    display: flex;

    justify-content: space-between;

    align-items: center;

    padding: 20px 34px;

    border-radius: 26px;

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.10);

    backdrop-filter: blur(20px);

    box-shadow:
    0px 10px 35px rgba(0,0,0,0.35);

    margin-bottom: 80px;
}

.logo {

    font-size: 40px;

    font-weight: 800;

    color: white;
}

.logo span {

    background:
    linear-gradient(
    90deg,
    #ff4d9d,
    #ff69b4,
    #ffb347
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

.status {

    background: rgba(16,185,129,0.14);

    border: 1px solid rgba(16,185,129,0.30);

    padding: 12px 22px;

    border-radius: 40px;

    color: #6ee7b7;

    font-size: 15px;

    font-weight: 600;
}

/* HERO SECTION */

.hero {

    text-align: center;

    margin-bottom: 65px;
}

.hero-title {

    font-size: 60px;

    font-weight: 900;

    line-height: 1.05;

    margin-bottom: 28px;

    color: white;
}

.hero-title span {

    background:
    linear-gradient(
    90deg,
    #ff4d9d,
    #ff69b4,
    #d946ef
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

/* MAIN CARD */

.main-card {

    max-width: 900px;

    margin: auto;

    background:
    linear-gradient(
    135deg,
    rgba(255,0,128,0.07),
    rgba(168,85,247,0.06)
    );

    border: 1px solid rgba(255,255,255,0.10);

    border-radius: 34px;

    padding: 42px;

    backdrop-filter: blur(18px);

    box-shadow:
    0px 15px 55px rgba(255,0,128,0.18);

    margin-bottom: 70px;
}

.card-header {

    display: flex;

    align-items: center;

    gap: 16px;

    margin-bottom: 10px;
}

.chat-icon {

    font-size: 34px;
}

.card-title {

    font-size: 38px;

    font-weight: 800;

    color: white;
}

.card-subtitle {

    color: #d1d5db;

    font-size: 18px;

    margin-bottom: 30px;

    margin-left: 52px;
}

/* TEXT AREA */

.stTextArea textarea {

    background: rgba(255,255,255,0.04) !important;

    color: white !important;

    border-radius: 24px !important;

    border: 1px solid rgba(255,255,255,0.12) !important;

    padding: 20px !important;

    font-size: 18px !important;

    line-height: 1.6 !important;

    min-height: 110px !important;
}

/* BUTTON */

.stButton button {

    width: 100%;

    border: none;

    border-radius: 20px;

    padding: 18px;

    font-size: 22px;

    font-weight: 700;

    color: white;

    background:
    linear-gradient(
    90deg,
    #ff4d9d,
    #ff4fd8,
    #d946ef
    );

    transition: 0.3s ease;

    box-shadow:
    0px 15px 35px rgba(255,0,128,0.35);

    margin-top: 10px;
}

.stButton button:hover {

    transform: translateY(-3px);

    box-shadow:
    0px 18px 40px rgba(236,72,153,0.45);
}

/* RESPONSE CARD */

.response-card {

    max-width: 900px;

    margin: auto;

    margin-top: 35px;

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.10);

    border-radius: 28px;

    padding: 34px;

    box-shadow:
    0px 12px 40px rgba(0,0,0,0.35);
}

.response-title {

    font-size: 28px;

    font-weight: 800;

    margin-bottom: 18px;

    background:
    linear-gradient(
    90deg,
    #ff4d9d,
    #ff69b4,
    #f472b6
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

.response-content {

    font-size: 17px;

    line-height: 2;

    color: #f3f4f6;
}

/* FEATURES */

.features {

    display: grid;

    grid-template-columns: repeat(4,1fr);

    gap: 20px;

    margin-top: 20px;
}

.feature-box {

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 22px;

    padding: 24px;

    text-align: center;

    transition: 0.3s ease;
}

.feature-box:hover {

    transform: translateY(-4px);

    background: rgba(255,255,255,0.06);
}

.feature-icon {

    font-size: 42px;

    margin-bottom: 14px;
}

.feature-title {

    font-size: 20px;

    font-weight: 700;

    margin-bottom: 10px;

    color: white;
}

.feature-text {

    color: #d1d5db;

    line-height: 1.8;

    font-size: 15px;
}

/* FOOTER */

.footer {

    text-align: center;

    margin-top: 55px;

    color: #9ca3af;

    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ---------------- #

st.markdown("""
<div class="navbar">

<div class="logo">
🚀 LLM <span>POWERED</span> INTERVIEW <span>AI</span> ASSISTANT
</div>

<div class="status">
● AI Career Intelligence Active
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- HERO ---------------- #

st.markdown("""
<div class="hero">

<div class="hero-title">
Navigate Your Career<br>
<span>With AI Intelligence</span>
</div>


</div>
""", unsafe_allow_html=True)

# ---------------- TEMPLATE ---------------- #

with open("Template.txt", "r", encoding="utf-8") as file:
    template = file.read()

Prompt = ChatPromptTemplate([
    ("system", template),
    ("human", "{question}")
])

# ---------------- MODEL ---------------- #

model = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant"
)

chain = Prompt | model

# ---------------- MAIN CARD ---------------- #

st.markdown("""
<div class="main-card">

<div class="card-header">

<div class="chat-icon">
💬
</div>

<div class="card-title">
Ask Your Career Questions
</div>

</div>

<div class="card-subtitle">
Describe your question or what you need help with.
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- INPUT ---------------- #

user_input = st.text_area(
    "",
    placeholder="Example: Create a roadmap to become an AI Engineer and prepare me for technical interviews...",
    label_visibility="collapsed"
)

# ---------------- BUTTON ---------------- #

if st.button("⚡ Generate AI Guidance"):

    if user_input.strip() == "":
        st.warning("Please enter your question.")

    else:

        with st.spinner("Generating intelligent career insights..."):

            response = chain.invoke({
                "question": user_input
            })

            st.markdown("""
            <div class="response-card">

            <div class="response-title">
            ✨ AI Career Guidance
            </div>

            </div>
            """, unsafe_allow_html=True)

            st.markdown(response.content)

# ---------------- FEATURES ---------------- #

st.markdown("""
<div class="features">

<div class="feature-box">
<div class="feature-icon">📄</div>
<div class="feature-title">Resume Optimization</div>
<div class="feature-text">
Improve ATS score and stand out to recruiters
</div>
</div>

<div class="feature-box">
<div class="feature-icon">💼</div>
<div class="feature-title">Interview Preparation</div>
<div class="feature-text">
Prepare for HR, Technical, SQL, Python, ML & AI rounds
</div>
</div>

<div class="feature-box">
<div class="feature-icon">🛣️</div>
<div class="feature-title">Career Roadmaps</div>
<div class="feature-text">
Get personalized learning paths and growth plans
</div>
</div>

<div class="feature-box">
<div class="feature-icon">📈</div>
<div class="feature-title">Skill Development</div>
<div class="feature-text">
Strengthen skills and stay ahead in your career
</div>
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ---------------- #

st.markdown("""
<div class="footer">
Powered by Groq • LangChain • Streamlit
</div>
""", unsafe_allow_html=True)
