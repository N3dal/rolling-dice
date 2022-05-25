#!/usr/bin/python3
# -----------------------------------------------------------------
# this project is one of the 50 python project challenge.
#
#
#
# Author:N84.
#
# Create Date:Sun Oct 10 17:22:22 2021.
# ///
# ///
# ///
# -----------------------------------------------------------------


# NOTE!!!:
# My English language is not great, don't be surprised if you find something strange or a new word.


from random import randint
from os import system
from os import name as OS_NAME
from time import sleep as delay


def clear():
    """wipe the terminal screen."""

    if OS_NAME == "posix":
        # for *nix machines.
        system("clear")

    else:
        # for windows machines.
        system("cls")


clear()


def welcome_screen():
    """asking the user about the name and getting,
    the name also using this function."""

    print("(Rolling Dice)".center(120, "-"))

    return input("\nEnter your name please: ".strip())


def ask(msg: str):
    """ask the players,if they want to play again, or if they want to exit.
    this function will ask question, and depending on that question,
    the answer will be "yes" or "no", or 'n', 'y'.
    and after that return True if the answer, is "yes", and return False if the answer,
    is "no", any thing except "yes", 'y', will consider as "no".
    first remove the colon, and then add it.
    if the user forget about it we will ad it."""

    msg = msg.strip(':')+": "
    return True if input(msg).strip().lower() in ("yes", 'y') else False


def main():
    """"""


if __name__ == "__main__":
    main()
