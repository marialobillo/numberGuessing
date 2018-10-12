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
    print("*** Welcome to Number Guessing Game! ***")
    print("Enter 'BYE' to stop the game.")


def get_random(a, b):
    return random.randint(a, b)



def start_game():

    show_intro()
    rounds = 0
    answer = ''
    winner = False
    random_number = get_random(1, 10)

    while answer != 'BYE':
        answer = input("Your guess number from 1 to 10 --> ")

        rounds += 1
        if answer == 'BYE':
            print('Oh we will miss you. Bye Bye!')
            break

        try:
            user_number = int(answer)
        except ValueError:
            print('The number should be a digit.Try again')
            continue

        if user_number > 10 or user_number < 1:
            print("Your guess number from 1 to 10.")
            continue
        if user_number == random_number:
            print("Got it!")
            winner = True
            break
        elif user_number > random_number:
            print("It's lower")
        elif user_number < random_number:
            print("It's higher")

    if winner:
        print("You won only in {} attemps!".format(rounds))
        print("Bye Bye")



if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
