from collections import Counter
from src.normalize import normalize
from src.tokenizer import tokenize_words


def compute_lexdiv(text: str) -> dict:

    #tokenize and normalize WITHOUT removing stopwords
    # (stopwords are real words and affect the metrics)
    tokens = tokenize_words(text)
    tokens = normalize(tokens, remove_stops=False)

    # Guard against empty text
    if not tokens:
        return {"tok": 0, "typ": 0, "hap": 0,
                "ttr": 0.0, "mwl": 0.0, "mwf": 0.0}

    # counting 
    tok = len(tokens)
    typ = len(set(tokens))

    freq = Counter(tokens)
    hap = sum(1 for count in freq.values() if count == 1)

    # calculating the  ratios
    ttr = round(typ / tok, 4)
    mwl = round(sum(len(t) for t in tokens) / tok, 4)
    mwf = round(tok / typ, 4)

    return {
        "Total words": tok,
        "Unique words": typ,
        "words used once": hap,
        "vocabulary richness": ttr,
        "Average word length": mwl,
        "Average word frequency": mwf,
    }