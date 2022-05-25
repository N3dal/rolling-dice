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


def dice_generator():
    """this function will generate and print,
    random dices."""

    # note i use some unicode characters
    dic = '●'  # dice_char
    # note: i draw this rectangle using some special,
    # character in other words (unicode) from wikipedia,
    # the link:https://en.wikipedia.org/wiki/Box-drawing_character

    # create the dice template.
    # notice that the dice is function not a string.
    # dice is callable-object not a string-object.
    dice = """
┌─────────┐
│ {0}  {1}  {2} │
│ {3}  {4}  {5} │
│ {6}  {7}  {8} │
└─────────┘
""".format

    # note: any dice_char position will contain only,
    # a dice_char or space to fill the place.
    # we only have six positions, but if we flip,
    # ths number six for example we get two six,
    # and the same thing for two and three.
    dice_positions = (
        # one
        (" ", " ", " ", " ", dic, " ", " ", " ", " "),
        # two
        (" ", " ", dic, " ", " ", " ", dic, " ", " "),
        (dic, " ", " ", " ", " ", " ", " ", " ", dic),
        # three
        (" ", " ", dic, " ", dic, " ", dic, " ", " "),
        (dic, " ", " ", " ", dic, " ", " ", " ", dic),
        # four
        (dic, " ", dic, " ", " ", " ", dic, " ", dic),
        # five
        (dic, " ", dic, " ", dic, " ", dic, " ", dic),
        # six
        (dic, " ", dic, dic, " ", dic, dic, " ", dic),
        (dic, dic, dic, " ", " ", " ", dic, dic, dic)
    )

    random_dice = randint(0, len(dice_positions)-1)

    return dice(*dice_positions[random_dice])


def main():
    """"""


if __name__ == "__main__":
    main()
