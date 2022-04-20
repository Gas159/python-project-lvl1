import random

game_task = "Find the greatest common divisor of given numbers."


def get_num():
    base_num = random.randint(2, 10)
    num1 = random.randint(1, 10) * base_num
    num2 = random.randint(1, 10) * base_num
    # print(base_num, num1, num2)
    question = "{} {}".format(num1, num2)
    return num1, num2, question


def get_question():
    num1, num2, question = get_num()
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
        # print(num1, num2)
    max_div = num1 + num2
    # print("Max-div",max_div)
    return question, max_div


# print(get_NOD())
