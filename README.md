# Test Technique - Indexation et Recherche d'Articles avec OpenSearch

Ce projet a été réalisé dans le cadre d'un test technique pour une alternance.  
Il permet d'ingérer des articles depuis un fichier JSON dans OpenSearch, d'y accéder via une API REST, et de les tester facilement avec Postman.

---

## Structure du projet

├── api/ # API Flask pour interagir avec OpenSearch
├── data/ # Données à indexer (articles.json)
├── ingest/ # Script Python pour l’ingestion
├── postman/ # Collection Postman de test
├── docker-compose.yml # Lancement d'OpenSearch
└── README.md


---

## Lancer le projet

### 1. Prérequis

- Python 3.x
- pip
- Docker + Docker Compose
- Postman (optionnel mais recommandé)

### 2. Lancer OpenSearch

```bash
docker compose up -d

Ingestion des articles :
pip install requests
python ingest/ingest_data.py

Tester l’API :
GET /articles

Rechercher un mot :
GET /articles?q=openai

Ajouter un article :

POST /articles
Content-Type: application/json
Body:
{
  "titre": "Exemple",
  "auteur": "Nikola",
  "contenu": "Contenu test",
  "date": "2025-07-06"
}
    
Tests avec Postman

Fichier à importer : postman/articles_collection.json
Contient :
GET /articles
GET /articles?q=...
POST /articles avec corps JSON

Réalisé par
Nikola, juillet 2025
Test technique alternance — projet OpenSearch + Flask