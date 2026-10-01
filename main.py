"""Number guessing game: reach a secret number using arithmetic operations."""

import random
import time
from fractions import Fraction

import functions as utils

MIN_NUMBER, MAX_NUMBER = 1, 1000


def ask_seed():
    """Ask for the starting number until a valid one is given. None = exit."""
    while True:
        raw = input(f"Insert your seed number ({MIN_NUMBER}-{MAX_NUMBER}): ").strip()
        if raw.lower() == "exit":
            return None
        try:
            seed = int(raw)
        except ValueError:
            print("Please insert a whole number.")
            continue
        if MIN_NUMBER <= seed <= MAX_NUMBER:
            return seed
        print(f"Insert a number between {MIN_NUMBER} and {MAX_NUMBER}.")


def play_game():
    """Run a single game."""
    target = random.randint(MIN_NUMBER, MAX_NUMBER)
    print("Secret number generated! Try to guess it using operations.")
    print("(Type 'exit' at any time to abandon the game.)")

    seed = ask_seed()
    if seed is None:
        print("You have abandoned the game.")
        return

    guess = Fraction(seed)
    attempts = 1
    if utils.process_hint(guess, target, attempts):
        return

    print("Use operations to get closer.")
    while True:
        operation = input("Insert an operation in the format operator number: ").strip()
        if operation.lower() == "exit":
            print("You have abandoned the game.")
            return

        new_guess = utils.process_operation(guess, operation)
        if new_guess is None:  # invalid input: doesn't count as an attempt
            continue

        guess = new_guess
        attempts += 1
        if utils.process_hint(guess, target, attempts):
            return


def show_rules():
    rules = [
        f"Start from a number of your choice between {MIN_NUMBER} and {MAX_NUMBER}.",
        "Use the basic operations (+, -, *, /) to reach the secret number.",
        "After each move you will be told how close you are to the goal.",
        "Remember that the goal is always a whole number!",
        "Win with the fewest moves possible!",
    ]
    for line in rules:
        time.sleep(0.5)
        print(line)


def main():
    while True:
        print("\nWELCOME TO THE NUMBER GUESSING GAME!")
        print("Press 1 to play")
        print("Press 2 to see the rules")
        print("Press 3 to exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "3":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Please choose 1, 2 or 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")