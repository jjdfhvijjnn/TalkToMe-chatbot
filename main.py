import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Loads .env file variables

api_key = os.getenv("OPENAI_API_KEY")  # Make sure this is before using api_key

client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{'role': "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("chatbot: ", response)