# 🔐 CyberLexAI Assistant (RAG Chatbot)

## Overview
This project is an AI-powered chatbot that answers cybersecurity and cyber law-related questions using a Retrieval-Augmented Generation (RAG) approach. It ensures responses are grounded in provided data instead of relying solely on general model knowledge.

---

## Problem
Large Language Models (LLMs) often generate **hallucinated or inaccurate responses** when asked domain-specific questions. This is especially critical in cybersecurity, where incorrect information can lead to serious consequences.

---

## Solution
To address this, a **Retrieval-Augmented Generation (RAG)** approach was implemented:
- The chatbot uses a predefined knowledge base (cyber law data)
- It retrieves relevant information from the dataset
- Generates accurate, context-based responses

---

## Tools & Technologies Used
- Python  
- OpenAI API  
- Prompt Engineering  
- VS Code  
- Text-based dataset (cyber_law.txt)  

---

## How It Works
1. User inputs a question  
2. System reads the local dataset (`cyber_law.txt`)  
3. The model is prompted with:
   - Context (data)
   - User query  
4. AI generates a response strictly based on the provided data  

---

## Sample Questions & Answers

### 🔹 Question:
**What is phishing?**

### 🔹 Answer:
Phishing is a cyber attack where attackers trick users into revealing sensitive information such as passwords or financial details, often through deceptive emails or websites.

---

### 🔹 Question:
**What is Section 66 of the IT Act?**

### 🔹 Answer:
Section 66 of the IT Act deals with computer-related offences such as hacking and unauthorized access. It includes penalties like imprisonment up to 3 years or fines.

---

## Key Learnings
- Prompt engineering significantly improves output quality  
- Context-based prompting reduces hallucination  
- RAG enhances reliability of AI systems  
- Building AI systems requires debugging real-world issues  

---

## Future Improvements
- Add a user interface (Streamlit/Web App)  
- Expand dataset (real legal documents)  
- Implement vector database (FAISS) for better retrieval  
- Add evaluation metrics for response quality  

---

## Author
Himanshi  
AI/LLM Analyst | Cyber & Digital Forensics
