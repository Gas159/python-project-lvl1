import random

game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    question = random.randint(3, 20)
    div_num = question // 2
    correct_answer = "yes"
    while div_num > 1 and correct_answer == "yes":
        if question % div_num == 0:
            correct_answer = "no"
        div_num -= 1
    return question, correct_answer
