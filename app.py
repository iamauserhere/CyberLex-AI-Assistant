from openai import OpenAI
client = OpenAI()

# Load your file
with open("cyber_law.txt", "r") as file:
    data = file.read()

print("Chatbot ready! Type 'exit' to quit.\n")

while True:
    query = input("Ask a question: ")
    
    if query.lower() == "exit":
        break

    prompt = f"""
    You are a cybersecurity assistant.
    Answer the question ONLY using the data below.

    DATA:
    {data}

    QUESTION:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    print("\nAnswer:", response.choices[0].message.content)