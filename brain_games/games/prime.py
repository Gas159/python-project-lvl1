import random

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(question):
    div_num = question // 2
    answer = True
    while div_num > 3 and answer:
        if question % div_num == 0:
            answer = False
        div_num -= 1
    return answer


def get_question_and_answer():
    question = random.randint(2, 20)
    if check_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
