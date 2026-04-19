# tokenizer.py

Tokenizes text into words or sentences using NLTK.

## Dependencies
- `re` — regular expressions (imported for potential use)
- `nltk` — natural language toolkit
- `nltk.tokenize.word_tokenize` — word-level tokenization
- `nltk.tokenize.sent_tokenize` — sentence-level tokenization

## Functions

**`tokenize_words(text: str) -> list[str]`**
Splits text into a list of word tokens.

**`tokenize_sentences(text: str) -> list[str]`**
Splits text into a list of sentence strings.

## Usage
```python
from tokenizer import tokenize_words, tokenize_sentences

words = tokenize_words("Hello world.")       # ['Hello', 'world', '.']
sentences = tokenize_sentences("Hi. Bye.")   # ['Hi.', 'Bye.']