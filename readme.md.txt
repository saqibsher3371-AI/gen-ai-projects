# Gen AI Projects 🚀

A personal collection of Generative AI projects built with modern tools like LangChain, Streamlit, LLMs, and vector databases.

This repository serves as a portfolio and playground for experimenting with generative AI applications.

## Projects

### [AI Interview Pro 💼](./ai-interview-pro/)
An intelligent Streamlit app that generates tailored interview questions from uploaded PDFs (resumes, job descriptions, technical docs, etc.).

**Features:**
- PDF text extraction and chunking
- Embedding with sentence transformers
- Vector store indexing
- LLM-powered question generation

**Tech Stack:** Streamlit • LangChain • PyPDF • Sentence Transformers • FAISS • OpenAI/Anthropic/Local LLM

→ [Go to project folder](./ai-interview-pro/)

*(More projects coming soon...)*

## How to Run Any Project
Each project is self-contained with its own `requirements.txt`.

```bash
# Clone the repo
git clone https://github.com/your-username/gen-ai-projects.git
cd gen-ai-projects

# Enter a project folder
cd ai-interview-pro

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py