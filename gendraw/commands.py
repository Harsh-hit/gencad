import google.generativeai as genai
import os
from typing import Any
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

prompt = """"Generate AutoCAD commands to create a house plan with the following specifications: two bedrooms, a hall, 
and a bathroom. Ensure the dimensions are proportional for practical use, and all rooms are connected with proper doors. 
Include walls with a standard thickness of 150 mm, and doors with a width of 900 mm. 
The dimensions for the rooms should be as follows:

Bedroom 1: 4m x 4m
Bedroom 2: 3.5m x 3.5m
Hall: 5m x 4m
Bathroom: 2m x 3m
The plan should include the following commands:

Drawing walls using the 'LINE' or 'RECTANGLE' command.
Placing doors using the 'ARC' or 'LINE' command.
Adding labels for each room using the 'TEXT' command.
IT IS VERY IMPORTANT THAT YOU Output only the sequence of AutoCAD commands required to create this house plan. Do not output any headings or explanations. just the commands"""

def get_response_text(model: genai.GenerativeModel, prompt: str) -> str:
    '''
    This function takes the prompt as input and gives AUTOCAD commands,
    as output using gemini models.

    Args:
        model (Any): instance of generative model
        prompt (str): prompt for the model
    
    Returns:
        str: set of commands to be executed.m
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
