import random

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_check_prime_num(question, div_num, correct_answer):
    while div_num > 1 and correct_answer == "yes":
        if question % div_num == 0:
            correct_answer = "no"
        div_num -= 1
    return correct_answer


def get_question():
    question = random.randint(3, 20)
    div_num = question // 2
    correct_answer = "yes"
    return question, get_check_prime_num(question, div_num, correct_answer)
