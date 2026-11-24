import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  

api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise RuntimeError("DEEPSEEK_API_KEY not defined")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "user", "content": "What is the highest mountain in the world?"}
    ]
)

print(response.choices[0].message.content)