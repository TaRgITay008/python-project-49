from brain_games.games import even
from brain_games.games.engine import run_game


def main():
    run_game(even, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == "__main__":
    main()
