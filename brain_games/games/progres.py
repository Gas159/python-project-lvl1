from random import randint

game_task = "What number is missing in the progression?"


def get_question():
    start = randint(1, 10)
    step = randint(2, 7)
    length = randint(5, 10)
    stop = step * length + start
    random_index_for_change = randint(0, length - 1)

    progresion = [*range(start, stop, step)]
    correct_answer = progresion.pop(random_index_for_change)
    progresion.insert(random_index_for_change, "..")
    question = progresion

    return question, correct_answer


# print(get_question())