import random


def even(number):
    return number % 2 == 0


def play_game():
    import prompt
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct = 0
    while correct < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user = prompt.string('Your answer: ').strip().lower()

        corrects = 'yes' if even(number) else 'no'

        if user not in ['yes', 'no']:
            print(
                    f"'{user}' is wrong answer ;(." 
                    f"Correct answer was '{corrects}'."
                )
            print(f"Let's try again, {name}!")
            return

        if user == corrects:
            print('Correct!')
            correct += 1
        else:
            print(
                    f"'{user}' is wrong answer ;(." 
                    f"Correct answer was '{corrects}'."
                )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
