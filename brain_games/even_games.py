#!/usr/bin/env python

from random import randint

import prompt


def is_even():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        random_num = randint(1, 100)
        even_or_no = random_num % 2
        if even_or_no == 0:
            true_answer = "yes"
        else:
            true_answer = "no"
        print(f"Question: {random_num}")

        user_answer = input("Your answer: ")

        if user_answer == true_answer:
            print("Correct!")

        else:
            return print(
                f"'{user_answer}' is wrong answer ;(."
                f" Correct answer was '{true_answer}'."
                f"\nLet's try again, {name}!")

    return print(
        f"****************************"
        f"\n  Congratulations, {name}!!!"
        f"\n****************************")
