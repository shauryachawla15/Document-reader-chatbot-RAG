# 📄 Document Reader Chatbot (RAG-based)

A Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions about a PDF document and receive accurate answers strictly based on the document content.

---

## 🚀 Features

- PDF document ingestion
- Text chunking and semantic embeddings
- Cosine similarity–based retrieval
- OpenAI-powered answer generation
- Flask web interface
- No hallucinations (answers strictly from document)

---

## 🧠 Tech Stack

- Python
- Flask
- SentenceTransformers (`all-MiniLM-L6-v2`)
- OpenAI API (`gpt-4o-mini`)
- NumPy
- PyPDF

---

## 🏗️ How It Works (RAG Pipeline)

1. PDF is loaded and split into text chunks
2. Each chunk is converted into an embedding
3. User question is embedded
4. Most relevant chunk is retrieved using cosine similarity
5. Retrieved context is passed to the LLM
6. LLM answers strictly from the document

---

## 📂 Project Structure

---text
doc-reader-chatbot/
│
├── app.py
├── requirements.txt
├── data/
│ └── sample.pdf
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── README.md


###⚙️ Setup Instructions
--

2️⃣ Create a virtual environment (optional but recommended)
--
  python -m venv venv
  venv\Scripts\activate

3️⃣ Install dependencies
--
  pip install -r requirements.txt

4️⃣ Set OpenAI API Key
Windows (PowerShell):
--
  setx OPENAI_API_KEY "your_api_key_here"
  Restart terminal after this.

5️⃣ Run the application
--
  python app.py

Open your browser and visit:
-
  http://127.0.0.1:5000


##🧪 Example Questions
--
1) What is this document about?
2) What services are mentioned?
3) Summarize the document
4) Who is this document intended for?

##📌 Notes
--
This implementation uses in-memory embeddings
Suitable for small to medium-sized PDFs
Can be extended with FAISS / Pinecone for large-scale use
Designed for learning and demonstration purposes

## Output(Screenshots)
--
<img width="1748" height="891" alt="Screenshot 2026-01-01 151048" src="https://github.com/user-attachments/assets/cf38e3ee-ece2-4d3b-8264-b2fac9d87066" />
<img width="1357" height="722" alt="Screenshot 2026-01-01 151213" src="https://github.com/user-attachments/assets/0e55b0e7-fa64-4928-b489-bd2460a38130" />
<img width="1687" height="798" alt="Screenshot 2026-01-01 151428" src="https://github.com/user-attachments/assets/cde46a02-0ff7-4540-9fd8-70f1d261ae24" />
<img width="1615" height="731" alt="Screenshot 2026-01-01 151754" src="https://github.com/user-attachments/assets/87bb61b7-de18-4fd8-8f28-95394f38edf0" />



##📬 Author
--
Shaurya Chawla
