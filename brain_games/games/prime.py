import random


def play_game():
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for _ in range(3):
        number = random.randint(1, 100)
        correct = "yes" if is_prime(number) else "no"

        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        if answer == correct:
            print("Correct!\n")
        else:
            print(
                    f"'{answer}' is wrong answer ;(." 
                    f"Correct answer was '{correct}'."
                )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")