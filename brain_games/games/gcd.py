import random

GAME_TASK = "Find the greatest common divisor of given numbers."


def get_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def get_question():
    base_num = random.randint(2, 10)
    num1 = random.randint(1, 10) * base_num
    num2 = random.randint(1, 10) * base_num
    question = "{} {}".format(num1, num2)
    return question, get_gcd(num1, num2)
