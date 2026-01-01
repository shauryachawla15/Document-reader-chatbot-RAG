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


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/doc-reader-chatbot.git
cd doc-reader-chatbot






# OUTPUT
<img width="1748" height="891" alt="Screenshot 2026-01-01 151048" src="https://github.com/user-attachments/assets/9a539ef0-b194-431f-8222-9143b4018dc5" />
<img width="1357" height="722" alt="Screenshot 2026-01-01 151213" src="https://github.com/user-attachments/assets/9fe1e0e0-c458-45dc-aea7-ca094b2b7ec5" />
<img width="1687" height="798" alt="Screenshot 2026-01-01 151428" src="https://github.com/user-attachments/assets/09a7db7a-7009-4879-b6f6-cdb72846bc16" />
<img width="1615" height="731" alt="Screenshot 2026-01-01 151754" src="https://github.com/user-attachments/assets/dea31d40-31e5-41f0-a618-1f66499346ed" />
