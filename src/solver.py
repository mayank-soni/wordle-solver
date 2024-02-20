# import argparse
from collections import Counter

import numpy as np


def choose_word(words: list[str]) -> str:
    """Return the word from the list
    containing the characters that appear in the most words."""
    counts: Counter = Counter()
    for word in words:
        for character in set(word):
            counts[character] += 1
    max_score: int = 0
    for word in words:
        score = sum(counts[character] for character in set(word))
        if score > max_score:
            best_word: str = word
            max_score = score
    return best_word


def entropy(probs: np.ndarray) -> float:
    return -np.sum(probs * np.log2(probs))


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("words", nargs="+")
#     args = parser.parse_args()
#     print(choose_word(args.words))
