# 4️⃣ `utils.md`

```markdown
# Utils Module

## Objectif

Regrouper des fonctions utilitaires communes utilisées dans plusieurs modules.


## Première approche
Sauvegarde de fichiers directement dans plusieurs fichiers :
```python
with open(path, "w", encoding="utf-8") as f:
f.write(text)
```

### Limites

- duplication du code
- encodage parfois oublié
- maintenance difficile

## Amélioration

Création d'une fonction utilitaire :

```python
def save_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
```
## Avantages
- code centralisé
- encodage garanti
- réutilisable dans tout le projet

# Pipeline final
Texte à sauvegarder

↓

save_text(path, text)

↓

écriture du fichier

↓

fichier créé en UTF-8