# Medical Record Summarizer

This is is a web application that helps healthcare professionals, patients, and researchers quickly generate summaries of medical records. The app uses AI-powered summarization via Google Gemini and PDF extraction via PyMuPDF.

### Features

- Upload PDF medical records.
- Extract text from PDFs with PyMuPDF.
- Generate concise summaries using Google Gemini AI.
- Easy-to-use web interface powered by Streamlit.

---

## 💻 Installation

Follow the steps below to get Sehatify up and running locally.

### Prerequisites

- Python 3.7+
- Streamlit
- Google Gemini API Key

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/sehatify.git
    cd sehatify
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the Google Gemini API key:
   - Obtain your API key from [Google Generative AI](https://developers.google.com/ai/generative).
   - Replace the placeholder in the `main.py` file with your actual API key:

    ```python
    genai.configure(api_key="Enter your API key here")
    ```

---

## 🚀 Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open the app in your browser (usually at `http://localhost:8501`).

3. Upload a PDF file containing a medical record.

4. The app will:
   - Display the extracted text from the PDF.
   - Show a generated summary of the medical record.

---

## 📦 Requirements

The following Python libraries are required for the project:

- `streamlit`: Framework to build the web interface.
- `python-dotenv`: For managing environment variables (e.g., API key).
- `requests`: To send HTTP requests (optional for further API calls).
- `google-generativeai`: Google Gemini API for content generation.
- `pymupdf`: Library to extract text from PDF documents.

To install these dependencies, run:

```bash
pip install -r requirements.txt
