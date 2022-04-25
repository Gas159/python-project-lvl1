import random

GAME_TASK = "What is the result of the expression?"


def get_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    list_operator = ["+", "-", "*"]
    operator = random.choice(list_operator)
    if operator == "+":
        true_answer = num1 + num2
    elif operator == "-":
        true_answer = num1 - num2
    else:
        true_answer = num1 * num2
    question = f"{num1} {operator} {num2}"
    return question, true_answer
