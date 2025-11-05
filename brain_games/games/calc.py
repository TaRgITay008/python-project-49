import operator
import random


def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operations = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    operation = random.choice(list(operations.keys()))

    question = f"{num1} {operation} {num2}"
    correct_answer = str(operations[operation](num1, num2))

    return question, correct_answer
