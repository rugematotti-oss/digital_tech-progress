# lexdiv.py

Computes lexical diversity metrics from a text string.

## Dependencies
- `collections.Counter` — word frequency counting
- `normalize` — cleans and normalizes tokens
- `tokenizer` — splits text into word tokens

## Function

**`compute_lexdiv(text: str) -> dict`**

Tokenizes and normalizes the input text (stopwords kept intentionally), then returns a dictionary of 6 metrics.

| Key | Description |
|-----|-------------|
| `Total words` | Total token count |
| `Unique words` | Number of distinct words |
| `words used once` | Hapax legomena count |
| `vocabulary richness` | Type-Token Ratio (unique / total) |
| `Average word length` | Mean number of characters per word |
| `Average word frequency` | Mean times each word appears (total / unique) |

Returns all zeros if the input text is empty.

## Usage
```python
from lexdiv import compute_lexdiv

result = compute_lexdiv("some text here")
print(result)