import random

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return None
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num


def get_question_and_answer():
    question = random.randint(2, 20)
    if is_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
