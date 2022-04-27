from random import randint

GAME_TASK = "What number is missing in the progression?"


def get_question():
    start = randint(1, 10)
    step = randint(2, 7)
    length = randint(6, 10)
    stop = step * length + start
    random_index_for_change = randint(0, length - 1)

    progression = list(range(start, stop, step))
    correct_answer = progression[random_index_for_change]
    question = ""
    for i in range(length):
        if random_index_for_change == i:
            question += ".. "
        else:
            question += str(progression[i]) + " "
    return question, str(correct_answer)
