# `preprocess.md`

# Preprocess Module

## Objectif

Nettoyer le texte des livres afin de le rendre exploitable pour les traitements NLP :

- lexical diversity
- topics extraction
- entity recognition

## Première approche

Fonction simple de nettoyage :

```python
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text
```
## Étapes
- conversion en minuscules
- suppression des caractères non alphabétiques
## Limites
- le texte devait être chargé manuellement
- duplication du code dans plusieurs modules
## Amélioration
Ajout d'une fonction pipeline :
```python
from src.loader import load_book_text
```
Puis :
```python
def get_clean_text(book_id):
    text = load_book_text(book_id)
    return clean_text(text)
```
# Pipeline final  
Book ID

↓

load_book_text()

↓

texte brut

↓

clean_text()

↓

lowercase

↓

suppression ponctuation

↓

texte prêt pour NLP