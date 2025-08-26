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
        correct = progression[missing_index]
        progression[missing_index] = ".."

        question = ' '.join(str(x) for x in progression)
        print(f"Question: {question}")
        user = input("Your answer: ")

        user = user.strip()
        if user.isdigit() or (user.startswith('-') and user[1:].isdigit()):
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