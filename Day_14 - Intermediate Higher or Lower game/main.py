from game_data import data
from art import logo, vs, fail
import random


def format_data(account):
    """Returns name, description and country data in a printable format."""

    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description} from {country}."


def check_answer(user_guess, count_a, count_b):
    """Checks if user guess is correct proposing an equality."""

    if count_a > count_b:
        return user_guess == "a"

    else:
        return user_guess == "b"


def get_random_account():
    """Take a random account from data."""

    return random.choice(data)

b_account = get_random_account()

print(logo)
points = 0

game_continues = True
while game_continues:

    a_account = b_account
    b_account = get_random_account()

    a_follower = a_account["follower_count"]
    b_follower = b_account["follower_count"]

    while a_account == b_account or a_follower == b_follower:
        
        b_account = random.choice(data)

    print(f"Compare A: {format_data(a_account)} \n {vs} \nAgainst B: {format_data(b_account)}")
    print(a_follower)
    print(b_follower)
    guess = input("Guess who has more follower. Type 'A' or 'B'. ").lower()

    if check_answer(guess, a_follower, b_follower):
        points += 1
        print(f"\n\n\nYou got this! Your score is: {points}.")
    else:
        game_continues = False
        print(f"{fail}\nSorry, you wrong. Game over. Your final score is: {points}")
