import random

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = random.randint(1, 100)
    correct_answer = "no"
    if question % 2 == 0:
        correct_answer = "yes"
    return question, str(correct_answer)
