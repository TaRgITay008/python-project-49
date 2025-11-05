from brain_games.games import calc
from brain_games.games.engine import run_game


def main():
    run_game(calc, "What is the result of the expression?")


if __name__ == "__main__":
    main()
