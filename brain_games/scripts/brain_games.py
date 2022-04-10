#!/usr/bin/env python

# import brain_games.cli
import brain_games.cli

def greet():
    print("Welcome to the Brain Games!")


def main():
    greet()
    brain_games.cli.welcome_user()
    # brain_games.cli1.welcome_user()
    # welcome_user()


if __name__ == "__main__":
    main()
