# Pipeline de Summarize

## Objectif

Générer un résumé court et pertinent d’un livre en sélectionnant les phrases les plus importantes.

---

## Première approche

La première idée était de prendre simplement les premières phrases du texte.

### Avantages
- Très simple à implémenter
- Rapide

### Limites
- Résumé peu représentatif du contenu global
- Peut manquer les parties importantes du texte
- Dépend fortement de l’introduction du livre

---

## Amélioration

Nous avons choisi une approche basée sur la fréquence des mots :

- Identifier les mots importants dans le texte
- Donner un score aux phrases en fonction de ces mots
- Sélectionner les phrases les plus pertinentes

---

## Pipeline final

Book ID  
↓  
Chargement du texte brut  
↓  
Découpage en phrases  
↓  
Tokenisation des mots  
↓  
Normalisation (minuscules, suppression ponctuation, stopwords)  
↓  
Calcul des fréquences de mots  
↓  
Score de chaque phrase  
↓  
Filtrage des phrases peu pertinentes  
↓  
Sélection des meilleures phrases  
↓  
Remise dans l’ordre original  
↓  
Concaténation  
↓  
Résumé final