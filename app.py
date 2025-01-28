import google.generativeai as genai
import fitz
import streamlit as st

# Extraction of text from medical record
def extract_text(path):
    file = fitz.open(path)
    
    text = ""
    for page_num in range(len(file)):
        page = file.load_page(page_num)
        text += page.get_text("text")
    
    return text

# Summary generation using Gemini
def summarizer(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([f"Please summarize the following medical record:\n\n{text}"])
    return response.text

# Streamlit App
def main():
    # Set the title of the app
    st.markdown("<h1 style='text-align: center; color : cyan'>Sehatify</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color : cyan'>Where wellness meets innovation</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Medical Record Summarizer</h1>", unsafe_allow_html=True)
    
    # Upload PDF file
    uploaded_file = st.file_uploader("Upload a Medical Record (PDF)", type="pdf")
    
    if uploaded_file is not None:
        # Extract text from the PDF
        medical_text = extract_text(uploaded_file)
        
        # Display the extracted text (optional, for debugging)
        st.subheader("Extracted Text:")
        st.text(medical_text)
        
        # Generate the summary
        st.subheader("Summary:")
        summary = summarizer(medical_text)
        st.text(summary)
        
# Configure the API Key (set your actual API key here)
genai.configure(api_key="AIzaSyD6Pgjy_DejFx759dTD4UsEiFRQGhaWuRk")

main()