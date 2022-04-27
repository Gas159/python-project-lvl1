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
    question = []
    for i in range(length):
        if random_index == i:
            question += [".."]
        else:
            question.append(str(progression[i]))
    question = " ".join(question)
    return question, str(correct_answer)


print(get_question_and_answer())
