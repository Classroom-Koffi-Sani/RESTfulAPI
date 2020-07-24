# RESTfull API
Application Programming Interface

Création d'une API

## Outils

- Python
- FastAPI
- Uvicorn
- MySQL/MariaDB

## Installation

Créer un environnement virtuel
```
virtualenv -p python3 venv
```

Installer le module fastAPI de python  avec `pip` :
```
pip install fastapi
```

Install uvicorn comme serveur web :
```
pip install uvicorn
```

## Création de l'API

Créer un fichier `main.py` :
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {'Hello': 'World'}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

## Exécution

Démarrer le serveur
```
uvicorn main:app --reload
```
et visiter l'adresse http://127.0.0.1:8000/ dans le navigateur.

## Documentation interactive

FastAPI dispose d'une documentation interactive accessible lorsqu'on crée un projet. Pour le nôtre, on peut y accéder à l'adresse suivante : http://127.0.0.1:8000/docs