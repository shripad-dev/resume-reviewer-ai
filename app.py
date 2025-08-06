# from openai import OpenAI

import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash-latest')

with open("./utils/res_sample.txt", "r") as f :
    content = f.read()

# print(content)

prompt = f"""
You have to review each and every detail in following resume.

Resume :
{content}
"""


response = model.generate_content(prompt)

with open("./utils/output_ai.txt", "w") as fw:
    fw.write(response.text)

