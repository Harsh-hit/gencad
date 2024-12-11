import tkinter as tk
from tkinter import scrolledtext, filedialog
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from environment variable
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_autocad_commands():
    """
    Fetches the prompt input from the user and generates AutoCAD commands using the Gemini model.
    """
    user_prompt = prompt_text.get("1.0", tk.END).strip()
    if not user_prompt:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please provide a prompt.")
        return

    try:
        response = model.generate_content(user_prompt)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, response.text)
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}")

def upload_image():
    """
    Allows the user to upload an image file and generates AutoCAD commands based on the content.
    """
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if not filepath:
        return

    try:
        myfile = genai.upload_file(filepath)
        result = model.generate_content(
            [myfile, "\n\n", "give commands for me to draw this shape in autocad, output should only be commands and nothing else."]
        )
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.text)
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}")

# Create the main application window
app = tk.Tk()
app.title("AutoCAD Command Generator")
app.geometry("800x600")

# Create a label for the prompt input
prompt_label = tk.Label(app, text="Enter your prompt:", font=("Arial", 12))
prompt_label.pack(pady=5)

# Create a text box for prompt input
prompt_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=10, font=("Arial", 10))
prompt_text.pack(pady=5)

# Create a button to generate commands
generate_button = tk.Button(app, text="Generate Commands", command=generate_autocad_commands, font=("Arial", 12))
generate_button.pack(pady=10)

# Create a button to upload an image
upload_button = tk.Button(app, text="Upload Image", command=upload_image, font=("Arial", 12))
upload_button.pack(pady=10)

# Create a label for the output
output_label = tk.Label(app, text="Generated Commands:", font=("Arial", 12))
output_label.pack(pady=5)

# Create a text box for displaying the output
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=15, font=("Courier", 10))
output_text.pack(pady=5)

# Run the application
app.mainloop()
