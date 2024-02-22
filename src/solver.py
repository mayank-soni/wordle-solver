# import argparse
from collections import Counter, defaultdict

import numpy as np
from tqdm import tqdm

from src.wordle import check_word


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


def get_best_guess(
    solutions: list[str], allowed_guesses: list[str], solution_probabilities: np.ndarray
) -> tuple[str, dict[tuple[int, ...], list[int]]]:
    """Return the word from allowed_guesses that maximises the expected reduction in entropy.
    Also return the indices of the subsets of solutions that would remain
    based on each possible outcome of the best guess.
    """
    lowest_average_entropy: float = float("inf")
    for guess in tqdm(allowed_guesses):
        results: dict[tuple[int, ...], list[int]] = defaultdict(list)
        # Get subsets of solutions based on the result you'd get for the guess
        for index, solution in enumerate(solutions):
            outcome: tuple[int, ...] = check_word(guess, solution)
            results[outcome].append(index)
        # Calculate the weighted average entropy of the subsets
        # TODO: vectorise the average entropy calculation
        # TODO: if multiple guesses have the same entropy, choose the one that could actually be a solution
        entropies = []
        total_probs = []
        for _, indices in results.items():
            entropies.append(entropy(solution_probabilities[indices]))
            total_probs.append(np.sum(solution_probabilities[indices]))
        average_entropy = np.average(entropies, weights=total_probs)
        if average_entropy < lowest_average_entropy:
            best_guess: str = guess
            best_results: dict[tuple[int, ...], list[int]] = results
            lowest_average_entropy = average_entropy
    return best_guess, best_results


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("words", nargs="+")
#     args = parser.parse_args()
#     print(choose_word(args.words))
