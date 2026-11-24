import os
from pathlib import Path
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1 - let's load the API on .env file
load_dotenv()  

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not defined")

# 2 - Now we will configure the Gemini client
client = genai.Client(api_key=api_key)

# 3 - And define the image path
image_path = "./spfc.jpg"

try:
    with open(image_path, "rb") as f:
        image_bytes = f.read()
except FileNotFoundError:
    print(f" Error: File '{image_path}' not found.")
    print("Please set a valid file path.")
    exit(1)

prompt = """
Analyze this image and do the following:
1. Describe what you see in the image.
2. If there is any text in the image, transcribe it exactly as it appears.
"""    

print("🤖 Sending the image to Gemini...")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",  
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),  # Adjust mime_type if PNG
        prompt
    ]
)

print("\n--- Gemini's Response ---")
print(response.text)
