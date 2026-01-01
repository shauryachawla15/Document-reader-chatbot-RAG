from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
import numpy as np
from openai import OpenAI
import os
from pypdf import PdfReader

# ------------------------
# Setup
# ------------------------
app = Flask(__name__)

# OpenAI client (NEW API)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("API KEY FOUND:", bool(os.getenv("OPENAI_API_KEY")))

# Load embedding model (FREE, local)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# ------------------------
# Load and prepare document
# ------------------------
def load_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted
    return text

text = load_pdf_text("data/sample.pdf")

# Split document into chunks
def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks

chunks = chunk_text(text)

# Create embeddings for chunks
chunk_embeddings = embedder.encode(chunks, normalize_embeddings=True)

# ------------------------
# Routes
# ------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    print("Received request")

    data = request.get_json()
    print("Data:", data)

    question = data.get("question", "").strip()
    print("Question:", question)

    question_embedding = embedder.encode(
        question, normalize_embeddings=True
    )
    print("Question embedded")

    similarities = np.dot(chunk_embeddings, question_embedding)
    best_chunk = chunks[np.argmax(similarities)]
    print("Best chunk selected")

    prompt = f"""
Answer the question using ONLY the context below.

Context:
{best_chunk}

Question:
{question}
"""

    print("Calling OpenAI...")

    response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "system",
            "content": "You answer strictly using the document context."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

    print("OpenAI response received")

    answer = response.output_text.strip()
    return jsonify({"answer": answer})

# ------------------------
# Run app
# ------------------------
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=False, use_reloader=False)

