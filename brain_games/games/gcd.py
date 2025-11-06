import math
import random


def play_game():
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.\n")

    for _ in range(3):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        correct = math.gcd(a, b)

        print(f"Question: {a} {b}")
        user = input("Your answer: ")

        if user.strip().isdigit():
            if int(user) == correct:
                print("Correct!\n")
            else:
                print(
                    f"'{user}' is wrong answer ;(." 
                    f"Correct answer was '{correct}'."
                )
                print(f"Let's try again, {name}!")
                return
        else:
            print(
                    f"'{user}' is wrong answer ;(." 
                    f"Correct answer was '{correct}'."
                )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")