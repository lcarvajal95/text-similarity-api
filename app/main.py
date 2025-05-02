from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.model import embed_text, get_similarity_score
from app.schemas import TextRequest, SimilarityRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API de similitud de textos está corriendo"}

@app.post("/embed")
def embed_endpoint(req: TextRequest):
    embedding = embed_text(req.text)
    return {"embedding": embedding.tolist()}

@app.post("/similarity")
def similarity_endpoint(req: SimilarityRequest):
    score = get_similarity_score(req.text1, req.text2)
    return {"similarity_score": score}
