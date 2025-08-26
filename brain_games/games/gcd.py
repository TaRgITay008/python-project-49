import random
import math

def play_game():
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.\n")

    for _ in range(3):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        correct = math.gcd(a, b)

        print(f"Question: {a} {b}")
        user_answer = input("Your answer: ")

        if user_answer.strip().isdigit():
            if int(user_answer) == correct:
                print("Correct!\n")
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.")
                print(f"Let's try again, {name}!")
                return
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")