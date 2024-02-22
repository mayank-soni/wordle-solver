from collections.abc import Generator, Iterable
import pathlib
import pickle

import numpy as np
from tqdm import tqdm
import wordfreq

data_folder: pathlib.Path = pathlib.Path(__file__).parent.parent / "data"
solutions_path: pathlib.Path = data_folder / "wordlist_nyt20230701_hidden.txt"
guesses_path: pathlib.Path = data_folder / "wordlist_nyt20220830_all.txt"
probabilities_path: pathlib.Path = data_folder / "word_probabilities.pkl"
first_guess_indices_path: pathlib.Path = data_folder / "first_guess_wordlists.pkl"

language: str = "en"


def get_words(filepath: pathlib.Path) -> list[str]:
    """Return a list of words from the file at filepath.
    One word per line."""
    with filepath.open() as file:
        return file.read().splitlines()


def get_zipf_frequencies(
    words: Iterable[str], save_path: pathlib.Path | None = None
) -> dict[str, float]:
    """Return a dictionary with the frequency (Zipf scale) of each word in words.
    Optionally, save the dictionary to a pickle file at save_path."""
    frequencies: dict[str, float] = {}
    print("Getting Zipf frequencies for words")
    for word in tqdm(words):
        frequencies[word] = wordfreq.zipf_frequency(word, language)
    if save_path:
        with save_path.open("wb") as file:
            pickle.dump(frequencies, file)
    return frequencies


def get_modified_word_probabilities(
    words: list[str], save_path: pathlib.Path | None = None
) -> np.ndarray:
    """Return a dictionary with probability of occurence of each word in words.
    Probability is calculated as the normalised sigmoid of the Zipf frequency.
    Since zipf frequencies lie between 0 and 9, this ensures that the min probability is >= 0.5 * the max probability.
    For the wordle english list, it also leads to a distribution where ~90% of the words
    have a probability within 0.9 of the max probability. These are desirable properties for the distribution
    since most wordle answers, even if uncommon words, are approximately equally likely to occur.
    Only the really rare words should have a much lower probability, but even then not much lower.
    """
    zipf_frequencies: np.ndarray = np.array(
        [wordfreq.zipf_frequency(word, language) for word in words]
    )
    sigmoid_frequencies: np.ndarray = 1 / (1 + np.exp(-zipf_frequencies))
    probabilities = sigmoid_frequencies / np.sum(sigmoid_frequencies)
    return probabilities
