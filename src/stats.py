import argparse
import math


def number_of_games_to_100(stats: list[int]) -> int:
    """Return the number of games it takes to reach 100% (99.5% and above)."""
    wins = sum(stats[1:])
    return math.ceil((0.995 * stats[0] - wins) / 0.005)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stats", nargs=7, type=int)
    args = parser.parse_args()
    print(number_of_games_to_100(args.stats))
