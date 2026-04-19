# Pipeline de Similarity

## Objectif

Trouver les livres les plus similaires à un livre donné.

---

## Première approche

Comparer les livres en utilisant simplement le nombre de mots en commun.

### Avantages
- Facile à comprendre
- Implémentation rapide

### Limites
- Ne prend pas en compte l’importance des mots
- Résultats peu pertinents
- Sensibilité aux mots fréquents

---

## Amélioration

Nous avons utilisé TF-IDF et la similarité cosinus :

- TF-IDF permet de pondérer les mots selon leur importance
- Cosine similarity permet de comparer les textes de manière plus précise

---

## Pipeline final

Book ID  
↓  
Chargement du texte du livre cible  
↓  
Chargement des textes de la collection  
↓  
Vectorisation TF-IDF  
↓  
Calcul de la similarité cosinus  
↓  
Tri des scores  
↓  
Sélection des 5 livres les plus proches  
↓  
Retour des titres similaires