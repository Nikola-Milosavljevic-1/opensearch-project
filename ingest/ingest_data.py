import json
import requests

# URL de base pour accéder à OpenSearch
OPENSEARCH_URL = "http://localhost:9200"
# Nom de l’index dans lequel on va insérer les articles
INDEX_NAME = "articles"
# Chemin du fichier contenant les articles à indexer
DATA_FILE = "data/articles.json"

# Fonction pour créer l’index OpenSearch s’il n’existe pas déjà
def create_index():
    url = f"{OPENSEARCH_URL}/{INDEX_NAME}"
    response = requests.put(url)

    if response.status_code == 200:
        print(f"Index '{INDEX_NAME}' créé.")
    elif response.status_code == 400 and 'resource_already_exists_exception' in response.text:
        print(f"L’index '{INDEX_NAME}' existe déjà.")
    else:
        print(f"Erreur création index: {response.status_code} {response.text}")

# Fonction pour lire les articles JSON et les envoyer à OpenSearch
def ingest_documents():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        articles = json.load(f)

    for i, article in enumerate(articles):
        # POST un document dans l’index (OpenSearch génère un ID automatiquement)
        response = requests.post(f"{OPENSEARCH_URL}/{INDEX_NAME}/_doc", json=article)

        if response.status_code not in [200, 201]:
            print(f"[{i}] Échec: {response.status_code} - {response.text}")
        else:
            print(f"[{i}] Document indexé.")

# Point d’entrée du script : on crée l’index, puis on indexe les articles
if __name__ == "__main__":
    create_index()
    ingest_documents()
