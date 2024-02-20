from collections.abc import Generator, Iterable
import pathlib
import pickle

from tqdm import tqdm
import wordfreq

data_folder: pathlib.Path = pathlib.Path(__file__).parent.parent / "data"
solutions_path: pathlib.Path = data_folder / "wordlist_nyt20230701_hidden.txt"
guesses_path: pathlib.Path = data_folder / "wordlist_nyt20220830_all.txt"
frequencies_path: pathlib.Path = data_folder / "word_frequencies.pkl"


def get_words(filepath: pathlib.Path) -> Generator[str, None, None]:
    """Yield words from a file storing one word per line."""
    for line in filepath.open():
        yield line.strip()


def get_zipf_frequencies(
    words: Iterable[str], save_path: pathlib.Path | None = None
) -> dict[str, float]:
    """Return a dictionary with the frequency (Zipf scale) of each word in words.
    Optionally, save the dictionary to a pickle file at save_path."""
    frequencies: dict[str, float] = {}
    for word in tqdm(words):
        frequencies[word] = wordfreq.zipf_frequency(word, "en")
    if save_path:
        with save_path.open("wb") as file:
            pickle.dump(frequencies, file)
    return frequencies
