import streamlit as st
from openai import OpenAI
import random

st.set_page_config(page_title="CyberLex AI", layout="wide")

# ---------- HIDE STREAMLIT UI ----------
st.markdown("""
<style>
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- STYLES + PARTICLES ----------
st.markdown("""
<style>

/* BASE */
.stApp {
    background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)),
    url("https://images.unsplash.com/photo-1550751827-4bd374c3f58b");
    background-size: cover;
    background-position: center;
    color: white;
    overflow-x: hidden;
}
            
/* PARTICLES CANVAS */
canvas {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 0;
}

.particles span {
    position: absolute;
    display: block;
    width: 3px;
    height: 3px;
    background: rgba(255,255,255,0.3);
    border-radius: 50%;
    animation: float 20s linear infinite;
}

@keyframes float {
    0% { transform: translateY(100vh) scale(0.5); }
    100% { transform: translateY(-10vh) scale(1); }
}            

/* HERO */
.hero {
    height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    position: relative;
    z-index: 2;
}

.hero-card {
     background: linear-gradient(
        135deg,
        rgba(255,255,255,0.06),
        rgba(255,255,255,0.02)
    );
    backdrop-filter: blur(20px);
    padding: 70px 60px;
    border-radius: 28px;
    border: 1px solid rgba(255,255,255,0.08);
    max-width: 900px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}

.hero-card h1 {
    font-size: 52px;
    margin-bottom: 10px;
}

.hero-card p {
    color: #bbb;
    font-size: 18px;
}

/* CTA */
.cta {
    margin-top: 25px;
}

.cta button {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    border: none;
    padding: 12px 24px;
    border-radius: 12px;
    color: white;
    font-weight: 500;
    margin: 5px;
    cursor: pointer;
}
            
/* SECTION WRAPPER */
.section {
    max-width: 1000px;
    margin: auto;
    padding: 40px 20px;
}

/* GLASS CARD */
.card {
    margin-bottom: 25px;
    padding: 30px;
    border-radius: 18px;
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.08);
    animation: fadeUp 1s ease;
}

/* TITLE */
.card-title {
    font-size: 22px;
    margin-bottom: 18px;
    font-weight: 600;
}

/* TEXT */
.card p {
    color: #ccc;
    line-height: 1.7;
}

/* RADIO */
div[role="radiogroup"] {
    justify-content: center;
    margin-top: 20px;
}

/* CHAT AREA */
[data-testid="stChatMessage"] {
    max-width: 800px;
    margin: auto;
}

/* INPUT */
[data-testid="stChatInput"] textarea {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 12px !important;
    color: white !important;
}

/* BUTTON */
button[kind="primary"] {
    border-radius: 10px !important;
}

/* ANIMATION */
@keyframes fadeUp {
    from { opacity:0; transform: translateY(20px); }
    to { opacity:1; transform: translateY(0); }
}
            
</style>
""", unsafe_allow_html=True)

# ---------- PARTICLES HTML ----------
particles_html = "<div class='particles'>"
for i in range(40):
    left = random.randint(0, 100)
    delay = random.uniform(0, 20)
    duration = random.uniform(10, 25)
    particles_html += f"<span style='left:{left}%; animation-delay:{delay}s; animation-duration:{duration}s;'></span>"
particles_html += "</div>"

st.markdown(particles_html, unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <div class="hero-card">
        <h1>🔐 LexCyber AI</h1>
        <p>Understanding cybercrime through structured intelligence</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- MODE ----------
mode = st.radio("", ["Learn", "Ask AI"], horizontal=True)

st.markdown('<div class="section">', unsafe_allow_html=True)

# ---------- LEARN MODE ----------
if mode == "Learn":

    st.markdown("""
    <div class="card">
        <div class="card-title">Cybercrime Overview</div>
        <p>
        Cybercrime has evolved into a persistent and large-scale threat.
        Attacks such as phishing, ransomware, and identity fraud are no longer isolated events —
        they are continuous and adaptive.
        </p>
        <p>
        Modern threats combine technical vulnerabilities with human manipulation,
        making awareness as important as technical defense.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-title">How this system works</div>
        <p>
        • Ask a cybersecurity question<br>
        • Relevant dataset is retrieved<br>
        • AI generates a structured response
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ---------- FIXED INSIGHT ----------
    facts = [
        "Phishing remains the most common entry point for cyber attacks.",
        "Ransomware groups now operate like businesses.",
        "Deepfakes are increasingly used in fraud.",
        "Human error causes most data breaches.",
        "Cyber law continues to evolve with digital threats."
    ]

    if "insight" not in st.session_state:
        st.session_state.insight = random.choice(facts)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Insight</div>', unsafe_allow_html=True)

    st.info(st.session_state.insight)

    if st.button("Refresh insight"):
        st.session_state.insight = random.choice(facts)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- ASK AI ----------
else:
    st.markdown("""
    <div class="card">
        <div class="card-title">AI Assistant</div>
        <p>
        Ask anything about cybersecurity, cyber law, or digital threats.
        The system responds using structured dataset-backed reasoning.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------- AI ----------
client = OpenAI()

with open("cyber_law.txt", "r") as file:
    data = file.readlines()

def find_relevant_data(query):
    relevant = []
    for line in data:
        if any(word.lower() in line.lower() for word in query.split()):
            relevant.append(line)
    return " ".join(relevant[:5])

# ---------- CHAT ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask a cybersecurity question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    relevant_data = find_relevant_data(user_input)
    if not relevant_data:
        relevant_data = "No relevant data found."

    prompt = f"""
    Answer ONLY using this data:

    {relevant_data}

    Question: {user_input}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
    except:
        answer = relevant_data

    st.session_state.messages.append({"role": "assistant", "content": answer})

# ---------- DISPLAY CHAT ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built by Himanshi | AI/LLM + CyberSecurity Project")