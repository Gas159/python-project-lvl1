import prompt

ROUND_COUNTS = 3


def run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game.GAME_TASK)

    for _ in range(ROUND_COUNTS):
        question, correct_answer = game.get_question_and_answer()
        print(f"Question: {question}")
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
