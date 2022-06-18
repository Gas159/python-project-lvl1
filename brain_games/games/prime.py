import random

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(question):
    d = 2
    while d * d <= question and question % d != 0:
        d += 1
    return d * d > question


def get_question_and_answer():
    question = random.randint(1, 20)
    if check_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
