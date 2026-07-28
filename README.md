# Agente Inteligente para Consultas sobre un Reglamento en PDF

## Descripción

Este proyecto consiste en un agente de inteligencia artificial desarrollado en Python que permite responder preguntas a partir del contenido de un documento PDF. Para este caso se utilizó el Reglamento de Estudiantes de la Pontificia Universidad Javeriana como fuente de información.

El sistema procesa el documento, lo divide en fragmentos, genera representaciones vectoriales (embeddings) y almacena la información en una base de conocimiento con FAISS. Cuando el usuario realiza una pregunta, el agente recupera los fragmentos más relacionados con la consulta y utiliza el modelo Gemini para generar una respuesta basada únicamente en el contenido del documento.

La aplicación cuenta con una interfaz sencilla desarrollada en Streamlit para facilitar la interacción con el usuario.

---

## Arquitectura de la solución

El funcionamiento del proyecto se divide en las siguientes etapas:

1. Lectura del documento PDF.
2. Extracción del texto.
3. División del contenido en fragmentos.
4. Generación de embeddings mediante Google Gemini.
5. Almacenamiento de los embeddings en un índice vectorial utilizando FAISS.
6. Búsqueda de los fragmentos más relevantes para cada consulta.
7. Envío del contexto recuperado al modelo Gemini.
8. Generación de una respuesta fundamentada en el documento.

---

## Tecnologías utilizadas

- Python 3
- Streamlit
- LangChain
- Google Gemini API
- FAISS
- PyPDF
- Python Dotenv

---

## Estructura del proyecto

```
alura-agente-ia/
│
├── app.py
├── app_streamlit.py
├── ReglamentoEstudiantes.pdf
├── requirements.txt
├── .env
└── README.md
```

---

## Instalación

1. Clonar el repositorio.

```bash
git clone https://github.com/USUARIO/alura-agente-ia.git
```

2. Entrar al proyecto.

```bash
cd alura-agente-ia
```

3. Instalar las dependencias.

```bash
pip install -r requirements.txt
```

4. Crear un archivo `.env` con la clave de la API de Gemini.

```env
GOOGLE_API_KEY=TU_API_KEY
```

5. Ejecutar la aplicación.

```bash
streamlit run app_streamlit.py
```

---

## Ejemplos de preguntas

- ¿Cuáles son los derechos del estudiante?
- ¿Qué promedio necesito para permanecer en la universidad?
- ¿Cuáles son las causales de pérdida de la calidad de estudiante?

## Ejemplos de respuestas

**Pregunta:** ¿Cuáles son los derechos del estudiante?

**Respuesta:** El agente responde con el listado de derechos establecidos en el reglamento, como el derecho a ser tratado con dignidad, expresar libremente sus ideas, acceder a los servicios de la universidad y participar en los espacios de representación estudiantil.

---

**Pregunta:** ¿Qué promedio necesito para permanecer en la universidad?

**Respuesta:** El agente indica que, según el reglamento, el estudiante debe mantener un promedio ponderado de período igual o superior a 2.5 y cumplir con el promedio acumulado establecido en el currículo.

## Aplicación desplegada

La aplicación puede probarse en el siguiente enlace:

https://alura-agente-ia-np6p4qtkkdvztqrvzxxappx.streamlit.app/

## Autor

Proyecto desarrollado por Kevin Bolívar como parte del Challenge Alura Agente IA.