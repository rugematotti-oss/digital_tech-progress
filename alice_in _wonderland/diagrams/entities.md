# Pipeline Entities

## Objectif

Identifier les personnages et les lieux dans un texte.

---

## Première approche

Utiliser tous les mots commençant par une majuscule.

### Avantages
- Très simple
- Rapide

### Limites
- Beaucoup de faux positifs
- Difficulté à distinguer personnages et lieux

---

## Amélioration

- Filtrer les mots inutiles (blocklist)
- Utiliser la fréquence pour garder les entités importantes
- Ajouter une liste de lieux connus pour améliorer la classification

---

## Pipeline final

Book ID  
↓  
Chargement du texte brut  
↓  
Extraction des mots avec majuscule  
↓  
Filtrage (blocklist)  
↓  
Comptage des occurrences  
↓  
Sélection des mots les plus fréquents  
↓  
Classification (personnages / lieux)  
↓  
Retour des entités