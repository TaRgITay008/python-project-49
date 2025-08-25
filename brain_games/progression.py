import random

def play_game():
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?\n")

    for _ in range(3):
     
        length = random.randint(5, 10)
        start = random.randint(1, 20)
        step = random.randint(1, 10)
        progression = [start + step * i for i in range(length)]

        missing_index = random.randint(0, length - 1)
        correct_answer = progression[missing_index]
        progression[missing_index] = ".."

        question = ' '.join(str(x) for x in progression)
        print(f"Question: {question}")
        user_input = input("Your answer: ")

        if user_input.strip().isdigit() or (user_input.strip().startswith('-') and user_input.strip()[1:].isdigit()):
            if int(user_input) == correct_answer:
                print("Correct!\n")
            else:
                print(f"'{user_input}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return
        else:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")