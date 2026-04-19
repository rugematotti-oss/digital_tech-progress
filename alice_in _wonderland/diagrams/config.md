# Config Module

## Objectif

Centraliser tous les chemins utilisés dans le projet afin d'éviter les chemins hardcodés dans plusieurs fichiers.

Cela permet :
- une meilleure maintenance
- un code plus lisible
- un changement rapide de structure si nécessaire

---

## Première approche

Au début du projet, les chemins étaient écrits directement dans les fichiers.

Exemple dans `loader.py` : path = "data/books/123.txt"

### Avantages

- Très simple
- Rapide à écrire

### Limites

- Chemins dupliqués dans plusieurs fichiers
- Si la structure change → tout casse
- Mauvaise maintenabilité
- Impossible de gérer facilement d'autres sources comme un catalogue CSV

---

## Amélioration

Création d'un fichier central `config.py` contenant les constantes de chemins.

```python
BOOKS_PATH = "data/books/"
CACHE_PATH = "data/cache/"
CATALOG_PATH = "data/catalog/pg_catalog.csv"
```
Les autres modules importent ensuite la configuration : 
```python 
from src.config import BOOKS_PATH
```
## Avantages

- Un seul endroit à modifier
- Code plus propre
- Réduction des erreurs
- Pipeline final
### Pipeline final 
Besoin d'un chemin
↓

Import depuis config.py

↓

Utilisation :
```python
BOOKS_PATH + f"{book_id}.txt"
```
↓

Fichier accessible

