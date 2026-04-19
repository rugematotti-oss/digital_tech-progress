# Pipeline de génération de card

## Objectif

Regrouper toutes les analyses d’un livre dans une seule structure.

---

## Première approche

Exécuter chaque fonction séparément sans centralisation.

### Limites
- Pas pratique à utiliser
- Pas de vue globale

---

## Amélioration

Créer une fonction centrale qui appelle toutes les analyses.

---

## Pipeline final

Book ID  
↓  
Récupération des informations  
↓  
Calcul de la diversité lexicale  
↓  
Extraction des topics  
↓  
Extraction des entités  
↓  
Génération du résumé  
↓  
Calcul des similarités  
↓  
Assemblage des résultats  
↓  
Retour de la carte complète