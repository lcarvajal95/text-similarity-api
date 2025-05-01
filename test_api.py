import requests

def test_embed():
    response = requests.post("http://localhost:8000/embed", json={"text": "Hola mundo"})
    print("Embed:", response.status_code, response.json())

def test_similarity():
    data = {"text1": "Hola", "text2": "Hola mundo"}
    response = requests.post("http://localhost:8000/similarity", json=data)
    print("Similarity:", response.status_code, response.json())

test_embed()
test_similarity()
