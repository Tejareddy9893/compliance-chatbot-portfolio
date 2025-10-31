from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd

model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

def load_embeddings():
    df = pd.read_csv("data/hipaa_faq.csv")
    questions = df["question"].tolist()
    answers = df["answer"].tolist()
    embeddings = model.encode(questions)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)
    return index, questions, answers

def semantic_answer(query, index, questions, answers):
    query_embedding = model.encode([query])
    _, I = index.search(query_embedding, k=1)
    return answers[I[0][0]]