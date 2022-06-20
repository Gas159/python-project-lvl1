import random

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    div = 2
    while div * div <= num and num % div != 0:
        div += 1
    return div * div > num


def get_question_and_answer():
    question = random.randint(2, 20)
    if is_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
