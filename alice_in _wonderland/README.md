#  Bookworm - NLP Project

##  Description

Bookworm est une application en ligne de commande permettant d’analyser des livres issus du projet Gutenberg.

Le projet propose plusieurs fonctionnalités de traitement du langage naturel (NLP) telles que :

* analyse de la diversité lexicale
* extraction de mots clés (topics)
* détection d’entités (personnages et lieux)
* génération de résumé
* recherche de similarité entre livres

Une commande globale permet de regrouper toutes ces informations dans une **book card**.

---

## Installation

### 1. Cloner le repository

```bash
git clone <repo_url>
cd <repo_name>
```

### 2. Créer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Données nécessaires

### Télécharger le catalogue Gutenberg (obligatoire)

```bash
mkdir -p data/catalog
cd data/catalog
wget https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv
```

 Ce fichier n’est pas versionné (voir `.gitignore`).

---

##  Utilisation

### Commandes principales

```bash
python bookworm.py --info <ID>
python bookworm.py --lexdiv <ID>
python bookworm.py --topics <ID>
python bookworm.py --entities <ID>
python bookworm.py --summarize <ID>
python bookworm.py --similar <ID>
python bookworm.py --card <ID>
```

### Exemple

```bash
python bookworm.py --card 11
```

---

##  Fonctionnalités

### 🔹 Informations (`--info`)

Récupère :

* titre
* auteur(s)
* catégories (`bookshelves`)

👉 Les métadonnées sont extraites du **catalogue CSV Gutenberg** pour garantir leur fiabilité.

---

###  Diversité lexicale (`--lexdiv`)

Calcule :

* nombre total de mots (TOK)
* nombre de mots uniques (TYP)
* hapax (HAP)
* TTR, MWL, MWF

---

### 🔹 Topics (`--topics`)

Extrait les mots les plus fréquents par section du livre.

---

### 🔹 Entités (`--entities`)

Détecte :

* personnages
* lieux

---

### 🔹 Résumé (`--summarize`)

Génère un résumé basé sur la fréquence des mots et la pertinence des phrases.

---

### 🔹 Similarité (`--similar`)

Trouve les livres les plus proches en utilisant :

* TF-IDF
* similarité cosinus

---

### 🔹 Book Card (`--card`)

Regroupe toutes les analyses dans un seul objet JSON.

---

##  Documentation

Les pipelines de chaque fonctionnalité sont disponibles dans le dossier :

```bash
docs/
```

Chaque fichier décrit :

* l’objectif
* l’approche initiale
* les limites
* les améliorations
* le pipeline final

---

##  Bonus

###  Word Cloud

Génération d’un nuage de mots basé sur les mots les plus fréquents.

```bash
python bonus/wordcloud/wordcloud_generator.py 11
```

---

###  Frontend Streamlit

Interface interactive pour visualiser les résultats.

```bash
streamlit run bonus/frontend/app.py
```

Fonctionnalités :

* affichage complet de la book card
* visualisation des données
* génération de la word cloud

---
### Retrieve books by author

Ce bonus permet de retrouver tous les livres d’un auteur donné à partir du catalogue Gutenberg.

Commande dédiée :

```bash
python bonus/author/author_books.py "Lewis Carroll"

---

##  Structure du projet

```bash
project/
├── src/
├── data/
│   ├── books/
│   └── catalog/
├── docs/
├── bonus/
│   ├── wordcloud/
│   └── frontend/
├── bookworm.py
├── requirements.txt
└── README.md
```

---

## Limitations

* certains livres Gutenberg ne sont pas disponibles sous le format attendu
* certaines métadonnées peuvent être absentes dans les fichiers texte
* le champ `bookshelves` dépend du catalogue CSV


