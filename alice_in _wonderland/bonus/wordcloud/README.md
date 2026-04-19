### Wordcloud Bonus
## Description :
Ce bonus permet de générer un nuage de mot à partir d'un livre du projet Gutenberg 
Les mots les plus fréquents du texte sont mis en avant visuellement, ce qui permet d'avoir une vue rapide sur les thèmes sprincipaux du livre 

## Fonctionnement :
Le programme :
1. charge le texte du livre 
2. nettoie du texte (minuscules, usppression des caractères spéciaux)
3. tokenize et normalise les mots
4. filtre certains mots fréquents inutiles 
5. calcule les fréquences 
5. génère une image avec les mots les plus importants 

## Utilisation :
Depuis la racine du projet 

python bonus/wordcloud/wordcloud_generator.py [id]

## Résultat : 
L'image générée est enregistrée dans : 
bonus/wordcloud/output

## Dépendances : 
Ce bonus nécessite : 
pip install wordcloud matplotlib