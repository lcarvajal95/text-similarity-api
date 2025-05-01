from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_text(text: str) -> np.ndarray:
    return model.encode([text])[0]

def get_similarity_score(text1: str, text2: str) -> float:
    emb1 = embed_text(text1).reshape(1, -1)
    emb2 = embed_text(text2).reshape(1, -1)
    return float(cosine_similarity(emb1, emb2)[0][0])
