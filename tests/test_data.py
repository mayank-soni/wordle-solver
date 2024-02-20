from collections.abc import Iterable

from src.data import solutions_path, guesses_path, get_words


def check_solutions(guesses: Iterable[str], solutions: Iterable[str]) -> bool:
    """Check if all solutions are in the guesses list.
    Prints the solutions that are not in the guesses list.
    Returns True if all solutions are in the guesses list, False otherwise.
    """
    output: bool = True
    guesses_set: set = set()
    for word in guesses:
        guesses_set.add(word)

    for word in solutions:
        if word not in guesses_set:
            print(f'Solution: "{word}" not found in guesses')
            output = False
    return output


def test_data():
    solutions = get_words(solutions_path)
    guesses = get_words(guesses_path)
    assert check_solutions(guesses, solutions) == True
