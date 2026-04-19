# normalize.py

Cleans and normalizes a list of tokens.

## Dependencies
- `string` — punctuation reference
- `nltk.corpus.stopwords` — English stopwords list

## Functions

**`to_lowercase(tokens)`**
Converts all tokens to lowercase.

**`remove_punctuation(tokens)`**
Removes punctuation characters from the token list.

**`remove_stopwords(tokens)`**
Removes common English stopwords (e.g. "the", "is", "and").

**`normalize(tokens, remove_stops=True)`**
Runs the full pipeline: lowercase → remove punctuation → optionally remove stopwords.

## Usage
```python
from normalize import normalize

tokens = ["The", "cat", "sat", "."]
normalize(tokens)                    # ['cat', 'sat']
normalize(tokens, remove_stops=False) # ['cat', 'sat', '.'] — keeps stopwords, removes punctuation