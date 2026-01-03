from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from langchain_core.documents import Document


def format_docs(docs: list[Document]) -> str:
    return "\n\n".join(doc.page_content for doc in docs)


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def generate_questions(vector_store):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0.7,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert HR interviewer. Using ONLY the provided context, "
                "generate exactly 5 high-quality interview questions.\n\n"
                "Context:\n{context}",
            ),
            ("human", "Generate the interview questions now."),
        ]
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": 6})

    rag_chain = {"context": retriever | format_docs} | prompt | llm | StrOutputParser()

    # You MUST pass a query to the retriever
    return rag_chain.invoke("Generate interview questions")
