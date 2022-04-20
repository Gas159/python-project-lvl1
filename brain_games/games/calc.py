import random

game_task = "What is the result of the expression?"


def get_operator(num1, num2):
    list_operator = ["+", "-", "*"]
    operator = random.choice(list_operator)
    if operator == "+":
        true_answer = num1 + num2
    elif operator == "-":
        true_answer = num1 - num2
    else:
        true_answer = num1 * num2
    return operator, true_answer


def get_question():
    random_num1 = random.randint(1, 10)
    random_num2 = random.randint(1, 10)
    operator, true_answer = get_operator(random_num1, random_num2)
    question = f"{random_num1} {operator} {random_num2}"
    # print(f"Question: {question} = {true_answer} ")
    return question, true_answer

# get_question()
