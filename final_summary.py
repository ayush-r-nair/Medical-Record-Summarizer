#Importing the libraries
import google.generativeai as genai
import fitz 
import os

#Extraction of text from medical record
def extract_text(path):
    file = fitz.open(path)
    
    text = ""
    for page_num in range(len(file)):
        page = file.load_page(page_num)
        text += page.get_text("text")
    
    return text

#Summary generation using Gemini
def summarizer(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([f"Please summarize the following medical record:\n\n{text}"])
    return response.text

#Main function to call extraction and summarizer
def main(path):
    medical_text=extract_text(path)
    summary = summarizer(medical_text)
    
    print("Summary:\n", summary)

#API Key and pdf path provided  
genai.configure(api_key="Enter your api key from gemini")
pdf_path="Enter the pdf path"

main(pdf_path)
