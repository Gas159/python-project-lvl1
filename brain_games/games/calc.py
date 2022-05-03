import random

GAME_TASK = "What is the result of the expression?"


def get_question_and_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operators = ["+", "-", "*"]
    operator = random.choice(operators)
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2
    question = f"{num1} {operator} {num2}"
    return question, answer
