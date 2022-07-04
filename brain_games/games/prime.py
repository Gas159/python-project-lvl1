import random

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    return True


def get_question_and_answer():
    question = random.randint(2, 20)
    if is_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, str(correct_answer)
