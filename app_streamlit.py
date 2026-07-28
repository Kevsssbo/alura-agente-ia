import streamlit as st

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

st.title("📚 Chat con PDF")


@st.cache_resource
def cargar_vectorstore():

    reader = PdfReader("ReglamentoEstudiantes.pdf")

    texto = ""

    for pagina in reader.pages:
        texto += pagina.extract_text()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    fragmentos = splitter.create_documents([texto])

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview"
    )

    return FAISS.from_documents(
        fragmentos,
        embeddings
    )


vectorstore = cargar_vectorstore()

pregunta = st.text_input("Haz una pregunta sobre el reglamento")

if st.button("Preguntar"):

    documentos = vectorstore.similarity_search(
        pregunta,
        k=3
    )

    contexto = "\n\n".join(
        [doc.page_content for doc in documentos]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview"
    )

    prompt = f"""
Eres un asistente que responde únicamente usando el reglamento.

Reglamento:

{contexto}

Pregunta:
{pregunta}

Si no encuentras la respuesta responde:

"No encontré esa información en el documento."
"""

    respuesta = llm.invoke(prompt)

    if isinstance(respuesta.content, list):
        st.write(respuesta.content[0]["text"])
    else:
        st.write(respuesta.content)