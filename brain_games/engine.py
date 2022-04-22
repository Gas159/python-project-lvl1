import prompt


def greeting(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game.game_task)

    for _ in range(3):
        question, correct_answer = game.get_question()
        print(f"Question: {question}")
        print("Правильный ответ(тест) -", correct_answer)
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")

        else:
            return print(
                f"'{user_answer}' is wrong answer ;(."
                f" Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!")

    return print(
        f"****************************"
        f"\n  Congratulations, {name}!!!"
        f"\n****************************")
