def check_word(guess: str, solution: str) -> tuple[int, ...]:
    """Return a tuple for each position in the guess, containing:
    - 2 if the character is in the right position
    - 1 if the character is in the solution but in the wrong position
    - 0 if the character is not in the solution.
    Follows wordle rules for repeated letters"""
    output = [-1] * len(guess)
    solution_list: list[str | None] = list(solution)
    for index, guess_char in enumerate(guess):
        try:
            solution_index = solution_list.index(guess_char)
        except ValueError:
            output[index] = 0
            continue
        if solution_index == index:
            output[index] = 2
        else:
            output[index] = 1
        solution_list[solution_index] = None
    return tuple(output)
