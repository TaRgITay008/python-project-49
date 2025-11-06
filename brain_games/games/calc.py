import random


def play_game():
    import prompt
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print("What is the result of the expression?")
    
    for _ in range(3):
        a = random.randint(1, 30)
        b = random.randint(1, 30)
        с = random.choice(['+', '-', '*'])
        expression = f"{a} {с} {b}"
        correct = eval(expression)

        print(f"Question: {expression}")
        answer = input("Your answer: ")

        clean_answer = answer.strip()
        if clean_answer.isdigit() or (clean_answer.startswith('-') and 
        clean_answer[1:].isdigit()):
            if int(answer) == correct:
                print("Correct!\n")
            else:
                print(
                    f"'{answer}' is wrong answer ;(." 
                    f"Correct answer was '{correct}'."
                )
                print(f"Let's try again, {name}!")
                return
        else:
            print(
                    f"'{answer}' is wrong answer ;(." 
                    f"Correct answer was '{correct}'."
                )
            print(f"Let's try again, {name}!")
            return
   
    print(f'Congratulations, {name}!')
