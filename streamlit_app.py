import streamlit as st
from openai import OpenAI

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://media.istockphoto.com/id/1247569904/vector/arrows-light-blue-abstract-futuristic-speed-on-black-background-vector-illustration.jpg?s=612x612&w=0&k=20&c=FsTw_Yq6QkfYQems8ysJtzE8kbMAR3x1_dv7TrwBqdI=");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    .main-container {
        background: rgba(0, 0, 0, 0.7);
        padding: 30px;
        border-radius: 15px;
        color: white;
        max-width: 700px;
        margin: auto;
        margin-top: 50px;
    }

    .answer-box {
        background-color: rgba(255,255,255,0.1);
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
client = OpenAI()

# Load your data
with open("cyber_law.txt", "r") as file:
    data = file.readlines()

def find_relevant_data(query, data):
    relevant = []
    
    for line in data:
        if any(word.lower() in line.lower() for word in query.split()):
            relevant.append(line)
    
    return " ".join(relevant[:5])  # limit to top matches

st.set_page_config(page_title="Cyber Law AI Assistant")

st.title("🔐 LexCyber AI Assistant")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://media.istockphoto.com/id/1247569904/vector/arrows-light-blue-abstract-futuristic-speed-on-black-background-vector-illustration.jpg?s=612x612&w=0&k=20&c=FsTw_Yq6QkfYQems8ysJtzE8kbMAR3x1_dv7TrwBqdI=");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .main-container {
        background: rgba(0, 0, 0, 0.6);
        padding: 30px;
        border-radius: 15px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.info("This chatbot answers based on a predefined cybersecurity dataset.")
st.write("Ask questions related to Cybersecurity and Cyber Law.")

# User input
query = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if query:
        relevant_data = find_relevant_data(query, data)

        if not relevant_data:
            relevant_data = "No relevant data found in dataset."

        prompt = f"""
        You are a cybersecurity assistant.
        Answer the question ONLY using the relevant data below.

        DATA:
        {relevant_data}

        QUESTION:
        {query}
        """

        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )

                answer = response.choices[0].message.content

            except Exception:
                # fallback if API fails
                st.warning("API unavailable. Showing data-based answer.")
                answer = relevant_data

            st.subheader("Answer:")
            st.write(answer)

    else:
        st.warning("Please enter a question.")
st.markdown("---")
st.caption("Built by Himanshi | AI/LLM + Cybersecurity Project")