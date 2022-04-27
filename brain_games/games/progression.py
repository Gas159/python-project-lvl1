from random import randint

GAME_TASK = "What number is missing in the progression?"


def get_question_and_answer():
    a = randint(1, 10)
    c = randint(2, 7)
    length = randint(6, 10)
    b = c * length + a
    random_index = randint(0, length - 1)

    progression = list(range(a, b, c))
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
