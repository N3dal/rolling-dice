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

# TODO: let the user change the dice char.


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
    DICE_C = DICE_CHAR = '●'  # dice_char
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
        (" ", " ", " ", " ", DICE_C, " ", " ", " ", " "),
        # two
        (" ", " ", DICE_C, " ", " ", " ", DICE_C, " ", " "),
        (DICE_C, " ", " ", " ", " ", " ", " ", " ", DICE_C),
        # three
        (" ", " ", DICE_C, " ", DICE_C, " ", DICE_C, " ", " "),
        (DICE_C, " ", " ", " ", DICE_C, " ", " ", " ", DICE_C),
        # four
        (DICE_C, " ", DICE_C, " ", " ", " ", DICE_C, " ", DICE_C),
        # five
        (DICE_C, " ", DICE_C, " ", DICE_C, " ", DICE_C, " ", DICE_C),
        # six
        (DICE_C, " ", DICE_C, DICE_C, " ", DICE_C, DICE_C, " ", DICE_C),
        (DICE_C, DICE_C, DICE_C, " ", " ", " ", DICE_C, DICE_C, DICE_C)
    )

    random_dice = randint(0, len(dice_positions)-1)

    return dice(*dice_positions[random_dice])


def dice_dot_count(dice: str):
    """calculate the overall,
    dots that show in the dice."""

    DICE_CHAR = '●'  # dice_char
    return dice.count(DICE_CHAR)


def dice_game(dice_count: int = 1, usr_choice=None, usr_name=None):
    """show to the user,
    the dice rolling animation."""

    period = 0
    # keep generate random dice ever randint(1, 50) or for 25 times,
    # for 2 seconds.
    while period < randint(1, 50):
        period += 1
        delay(100e-3)
        clear()
        dices = [dice_generator() for _ in range(dice_count)]
        print(*dices)
        dices_sum = sum(dice_dot_count(dice) for dice in dices)

    # check out if user choice is correct or not.
    print(f"your choice:'{usr_choice}', dice sum:'{dices_sum}'")
    print(f"Nice choice '{usr_name.capitalize()}'." if usr_choice ==
          dices_sum else f"Good luck next time '{usr_name.capitalize()}'.")


def usr_choice_input(msg: str = ""):
    """return int value,
    depend on the user input."""

    usr_input = input(msg).strip()

    try:
        usr_input = int(usr_input)
        return usr_input if usr_input in range(1, 13) else -1

    except ValueError:
        # if the user input was string or any type except numbers.
        return -1


def usr_input_in_range(usr_choice: int):
    """make sure that the users will give us,
    number between 1 to 12 or we will keep,
    asking them to enter number between 1 to 12,
    and this will also handle other types that,
    the user can give for us.

    this work as Guard-Condition."""

    while usr_choice < 1:
        clear()
        usr_choice = usr_choice_input(
            "Choose only numbers between '1' ~ '12': ")

    return usr_choice


def main():
    """"""
    user_name = welcome_screen()

    while ask("Start Rolling the Dices? [Y]es/[N]o: "):
        clear()

        usr_choice = usr_choice_input("Choose number between 2 and 12: ")

        # guard condition.
        usr_choice = usr_input_in_range(usr_choice)

        dice_game(2, usr_choice=usr_choice, usr_name=user_name)

        if ask("\nRolling Again? [Y]es/[N]o, enter[E]xit if you want to quit:"):
            continue
        else:
            break


if __name__ == "__main__":
    main()
