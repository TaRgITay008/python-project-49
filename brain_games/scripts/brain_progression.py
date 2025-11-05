from brain_games.games import progression
from brain_games.games.engine import run_game


def main():
    run_game(progression, "What number is missing in the progression?")


if __name__ == "__main__":
    main()
