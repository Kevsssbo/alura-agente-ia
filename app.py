import os
from dotenv import load_dotenv

from pypdf import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)

from langchain_community.vectorstores import FAISS

load_dotenv()

# --------------------
# 1. Leer PDF
# --------------------

reader = PdfReader("ReglamentoEstudiantes.pdf")

texto = ""

for pagina in reader.pages:
    texto += pagina.extract_text()

# --------------------
# 2. Dividir en fragmentos
# --------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

fragmentos = splitter.create_documents([texto])

print(f"Fragmentos: {len(fragmentos)}")

# --------------------
# 3. Crear embeddings
# --------------------

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
)

# --------------------
# 4. Crear base FAISS
# --------------------

vectorstore = FAISS.from_documents(
    fragmentos,
    embeddings
)

print("Base de conocimiento creada correctamente.")

# --------------------
# 5. Buscar información
# --------------------

pregunta = input("\nEscribe una pregunta: ")

documentos = vectorstore.similarity_search(
    pregunta,
    k=3
)

# Unimos los fragmentos encontrados
contexto = "\n\n".join([doc.page_content for doc in documentos])

# Creamos el modelo de Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)

prompt = f"""
Eres un asistente que responde preguntas únicamente usando el reglamento proporcionado.

Reglamento:

{contexto}

Pregunta:
{pregunta}

Si la respuesta no aparece en el reglamento, responde:
'No encontré esa información en el documento.'
"""

respuesta = llm.invoke(prompt)

print("\nRespuesta:\n")
print(respuesta.text)
