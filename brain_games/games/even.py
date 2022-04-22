import random

game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    question = random.randint(1, 100)
    correct_answer = "no"
    if question % 2 == 0:
        correct_answer = "yes"
    return question, correct_answer
