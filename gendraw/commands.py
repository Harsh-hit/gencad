import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")
response = model.generate_content("give me commands to draw a rectangle of dimensions 100 length and 50 width in AUTOCAD, the bottom left corner of the rectangle should be at origin(0,0),\
    do not output anything except commands")
print(response.text) 