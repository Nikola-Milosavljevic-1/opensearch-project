from flask import Flask, request, jsonify
import requests

# Création de l’app Flask
app = Flask(__name__)

# Configuration de base
OPENSEARCH_URL = "http://localhost:9200"
INDEX_NAME = "articles"

# Route GET /articles
# - Si un paramètre q=... est fourni, on fait une recherche plein texte
# - Sinon, on retourne tous les articles
@app.route("/articles", methods=["GET"])
def get_articles():
    query = request.args.get("q")

    if query:
        # Recherche dans les champs "titre" et "contenu"
        body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["titre", "contenu"]
                }
            }
        }
    else:
        # Si aucune requête, retourne tous les documents
        body = { "query": { "match_all": {} } }

    res = requests.get(f"{OPENSEARCH_URL}/{INDEX_NAME}/_search", json=body)
    hits = res.json()["hits"]["hits"]

    # On renvoie uniquement le contenu original (_source)
    return jsonify([hit["_source"] for hit in hits])

# Route POST /articles
# Permet d’ajouter un nouvel article dans l’index
@app.route("/articles", methods=["POST"])
def add_article():
    article = request.json  # Données JSON envoyées par le client
    res = requests.post(f"{OPENSEARCH_URL}/{INDEX_NAME}/_doc", json=article)
    return jsonify(res.json()), res.status_code

@app.route("/")
def home():
    return "Bienvenue sur l'API Flask pour OpenSearch"


# Point d’entrée de l’app Flask
if __name__ == "__main__":
    app.run(debug=True)
