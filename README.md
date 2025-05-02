# Text Similarity API

Este proyecto es una API REST construida con **FastAPI** y **Docker** que permite:

- Obtener el _embedding_ de una frase utilizando **Sentence Transformers**.
- Calcular la **similaridad coseno** entre dos frases.

---

## Tecnologías utilizadas

- Python 3.10
- FastAPI
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Scikit-learn
- Docker

---

## Instalación y ejecución con Docker

### 1. Clona este repositorio

```bash
git clone https://github.com/lcarvajal95/text-similarity-api.git
cd text-similarity-api

# Prueba de /embed
curl -X POST http://localhost:8000/embed \
     -H "Content-Type: application/json" \
     -d '{"text": "Hola mundo"}'

# Prueba de /similarity
curl -X POST http://localhost:8000/similarity \
     -H "Content-Type: application/json" \
     -d '{"text1": "Hola", "text2": "Hola mundo"}'

# Resultado esperado

{"embedding": [0.12, -0.35, ...]}
{"similarity_score": 0.87}


