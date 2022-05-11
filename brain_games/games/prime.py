import random
from math import sqrt

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(question):
    for i in range(2, int(sqrt(question) + 1)):
        if question % i == 0:
            return False
    return True


def get_question_and_answer():
    question = random.randint(2, 20)
    if check_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
