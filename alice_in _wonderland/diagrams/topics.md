# Pipeline d’extraction des topics

## Objectif

Identifier les mots les plus importants dans différentes parties d’un livre.

---

## Première approche

Compter les mots les plus fréquents sur tout le texte.

### Avantages
- Simple
- Rapide

### Limites
- Ne reflète pas les différentes parties du livre
- Les mots globaux dominent
- Perte de structure

---

## Amélioration

Découper le livre en sections et analyser chaque section séparément.

---

## Pipeline final

Book ID  
↓  
Chargement du texte nettoyé  
↓  
Découpage en sections  
↓  
Tokenisation  
↓  
Normalisation  
↓  
Calcul des fréquences par section  
↓  
Sélection des mots les plus fréquents  
↓  
Retour des topics