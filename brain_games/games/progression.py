from random import randint

GAME_TASK = "What number is missing in the progression?"


def get_question_and_answer():
    start = randint(1, 10)
    step = randint(2, 7)
    length = randint(6, 10)
    stop = step * length + start
    random_index = randint(0, length - 1)

    progression = list(range(start, stop, step))
    correct_answer = progression[random_index]
    progression[random_index] = ".."
    question = " ".join(map(str, progression))
    return question, str(correct_answer)
