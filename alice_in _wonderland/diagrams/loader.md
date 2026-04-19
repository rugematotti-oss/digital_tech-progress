# loader.md

```markdown
# Loader Module

## Objectif

Le module `loader.py` permet de :

- télécharger un livre depuis Project Gutenberg
- charger le texte d'un livre
- extraire les métadonnées (titre, auteur, bookshelf)


# Première version (v1)
Au début, le loader faisait uniquement la lecture locale d'un fichier texte.

```python
def load_book_text(book_id):
    path = f"data/books/{book_id}.txt"
    with open(path, "r") as f:
        return f.read()
```        

## Avantages
- Code très simple
- Fonctionne si les fichiers sont déjà présents

## Limites
- Aucun téléchargement automatique
- Chemins hardcodés
- Pas de gestion d'erreur
- Pas de métadonnées

# Deuxieme version(v2)
Ajout du téléchargement automatique depuis Project Gutenberg.
Utilisation de la librairie`requests.`

```python
url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
response = requests.get(url)
```

Si le fichier n'existe pas:
```python
load_book_text()
↓
download_book()
↓
sauvegarde dans data/books
```

## Améliorations
- création automatique du dossier avec os.makedirs()
- téléchargement automatique

# Troisieme version(v3)
Ajout de l'extraction des métadonnées.
Au départ les métadonnées étaient souvent :
```python
Unknown bookshelf
```
car certains livres ne contiennent pas ces informations dans le header.

## Approche 1 : extraction dans le header
Utilisation de regex pour chercher les champs :
- Title
- Author
- Bookshelf
```python
extract_metadata_field()
```
### Limite :
certains livres Gutenberg n'ont pas ces champs.

## Approche 2 : utilisation du catalogue Gutenberg
Ajout d'une lecture du catalogue officiel :

``data/catalog/pg_catalog.csv``

Lecture avec pandas :
```python
df = pd.read_csv(CATALOG_PATH)
row = df[df["Text#"] == int(book_id)]
```
Cela permet d'obtenir :
- titre
- auteurs
- bookshelf

### Avantage
Beaucoup plus fiable que l'analyse du header.

## Fallback
Si le CSV ne conteint pas le livre :

CSV lookup
↓
si trouvé → métadonnées
↓
sinon → analyse du header
↓
sinon → Unknown

# Pipeline final

Book ID

↓

load_book_text()

↓

Fichier absent ?

→ download_book()

↓

Texte brut récupéré

↓

get_book_info()

↓

CSV catalogue

↓

si trouvé → métadonnées

↓

sinon → regex header

↓

Retour :
```python
{
  id
  title
  authors
  bookshelves
}