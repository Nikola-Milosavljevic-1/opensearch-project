import json
import requests

OPENSEARCH_URL = "http://localhost:9200"
INDEX_NAME = "articles"
DATA_FILE = "../data/articles.json"

# Création de l’index si besoin
def create_index():
    url = f"{OPENSEARCH_URL}/{INDEX_NAME}"
    response = requests.put(url)
    if response.status_code == 200:
        print(f"Index '{INDEX_NAME}' créé.")
    elif response.status_code == 400 and 'resource_already_exists_exception' in response.text:
        print(f"L’index '{INDEX_NAME}' existe déjà.")
    else:
        print(f"Erreur création index: {response.status_code} {response.text}")

# Envoi des documents
def ingest_documents():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        articles = json.load(f)

    for i, article in enumerate(articles):
        response = requests.post(f"{OPENSEARCH_URL}/{INDEX_NAME}/_doc", json=article)
        if response.status_code not in [200, 201]:
            print(f"[{i}] Échec: {response.status_code} - {response.text}")
        else:
            print(f"[{i}] Document indexé.")

if __name__ == "__main__":
    create_index()
    ingest_documents()
