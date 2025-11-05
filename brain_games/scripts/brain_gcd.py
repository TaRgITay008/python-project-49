from brain_games.games import gcd
from brain_games.games.engine import run_game


def main():
    run_game(gcd, "Find the greatest common divisor of given numbers.")


if __name__ == "__main__":
    main()
