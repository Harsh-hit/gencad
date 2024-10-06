import google.generativeai as genai
import os
from typing import Any
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

prompt = "give me commands to draw a rectangle \
    of dimensions 100 length and 50 width in AUTOCAD,\
    the center of the rectanble should be at the center of the page,\
    do not output anything except commands"

def get_response_text(model: Any, prompt: str) -> str:
    '''
    This function takes the prompt as input and gives AUTOCAD commands,
    as output using gemini models.

    Args:
        model (Any): instance of generative model
        prompt (str): prompt for the model
    
    Returns:
        str: set of commands to be executed.
    '''
    response = model.generate_content(prompt)
    print(response.text)

def get_response_image(model:Any) -> str:
    '''
    This function is for taking both image and prompt, to generate
    AutoCad commands.
    '''
    myfile = genai.upload_file("..\media\download.png")
    result = model.generate_content(
    [myfile, "\n\n", "give commands for me to draw this shape in autocad, output\
     should only be commands and nothing else."]
    )
    print(result.text) 

get_response_text(model, prompt)
get_response_image(model)