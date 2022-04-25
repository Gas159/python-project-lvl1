import prompt


def run_engine(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game.GAME_TASK)
    attempt_number = 3

    for _ in range(attempt_number):
        question, correct_answer = game.get_question()
        print(f"Question: {question}")
        # print("Правильный ответ(тест) -", correct_answer)
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")

        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f" Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!")
            break

    else:
        print(f"Congratulations, {name}!")
