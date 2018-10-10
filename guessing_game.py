"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can
totally do that by clicking: File -> Download Workspace in the file menu after
you fork the snapshot of this workspace.

"""

import random

def show_intro():
    print("Welcome to Number Guessing Game!")
    print("""
Enter 'BYE' to stop the game.
""")


def get_random(a, b):
    return random.randint(a, b)



def start_game():

    show_intro()
    rounds = 0
    answer = ''
    random_number = get_random(1, 11)

    while answer != 'BYE':
        answer = input("Please introduce a guess number from 1 to 10 --> ")

        if answer == 'BYE':
            break

        user_number = int(answer)
        rounds += 1
        if user_number > 10 or user_number < 1:
            print("The guess number should be from 1 to 10. Try again.")
            continue
        if user_number == random_number:
            print("Got it!")
            break
        elif user_number > random_number:
            print("It's lower")
        elif user_number < random_number:
            print("It's higher")


    print("You won only in {} attemps!".format(rounds))



if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
