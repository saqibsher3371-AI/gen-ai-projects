from src.processor import process_pdf
from src.vector_store import embed_and_store
import streamlit as st
import os

save_path = "data/temp.pdf"

st.set_page_config(
    page_title="AI Interview Pro", layout="centered"
)  # Changed to centered for cleaner look

# Load custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main title with emoji and subtitle
st.markdown(
    "<h1 style='text-align: center;'>💼 AI Interview Pro</h1>", unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size: 1.2rem; color: #666;'>Upload a resume or job-related PDF to generate tailored interview questions instantly.</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Main content in columns for better spacing
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    with st.container():
        st.header("📄 Upload Your PDF")
        uploaded_file = st.file_uploader(
            "Choose a PDF file (e.g., resume, job description)", type="pdf"
        )

        if st.button(
            "🚀 Process & Upload PDF", type="primary", use_container_width=True
        ):
            if uploaded_file is not None:
                os.makedirs("data", exist_ok=True)
                with st.spinner("Saving and processing PDF..."):
                    with open(save_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    chunks = process_pdf(save_path)

                st.success(
                    f"✅ PDF processed successfully! Created {len(chunks)} chunks."
                )

                with st.spinner("🤖 Building knowledge base with embeddings..."):
                    st.session_state.vector_store = embed_and_store(chunks)

                st.success("🎉 Knowledge base ready! You can now generate questions.")
                st.balloons()  # Fun feedback

            else:
                st.error("⚠️ Please upload a PDF file first.")

# Question generation section
st.markdown("---")
st.header("❓ Generate Interview Questions")

if "vector_store" not in st.session_state:
    st.info("👆 Upload and process a PDF first to enable question generation.")
else:
    if st.button("Generate Questions Now", type="primary", use_container_width=True):
        with st.spinner("🧠 AI is generating tailored questions..."):
            from src.llm_service import generate_questions

            questions = generate_questions(st.session_state.vector_store)

        st.success("✅ Questions generated successfully!")

        # Display questions nicely (assuming questions is a string with numbered list or \n separated)
        st.markdown("### Generated Interview Questions")
        if isinstance(questions, str):
            # If it's a plain string, split and number
            question_lines = [q.strip() for q in questions.split("\n") if q.strip()]
            for i, q in enumerate(question_lines, 1):
                with st.expander(
                    f"Question {i}: {q.split('.')[0].strip() if '.' in q else q[:60]}..."
                ):
                    st.markdown(f"**{i}.** {q}")
        else:
            st.write(questions)  # Fallback
