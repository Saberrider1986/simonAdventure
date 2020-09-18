# Developer: Simon Wolf
# Date: 07.06.2020 # Review version 1.1 17.09.2020

import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

# Intro to the game


def intro():

    print_pause("Welcome to The Adventures of Miss Knubbelnase "
                "- Chapter 1 Paris")
    print_pause("You are Miss Knubbelnase, a 29 year old young bookshop clerk "
                "looking for an allegedly hidden treasure.")
    print_pause("With the help of an inherited map of Paris from your "
                "grandfather - where he marked hints on it - .")
    print_pause("After following the first steps your grandfather described, "
                "you find yourself standing in front of the statue of "
                "Henry IV on Quai de l'Horloge. ")
    print_pause("You step onto the statue and when you look down to a latin "
                "scribbling ..."
                "quis tangit me recta lucra clavem - who touches me right "
                "gains a key. ")
    print_pause("The next hint on your grandfathers notes on the map,"
                " describes a series of stone pushes on the statue.")
    print_pause("In the right order, to possibly acquire a key.")
    print_pause("However, you need to find the solution fast since an "
                "old cult hunting you is only a couple of minutes away. ")
    print_pause("Below the scribbling, you see a dented yellow stone on the "
                "left and a red stone on the right.")

# 1. Part - The statue - getting the key through pushing stones on the statue
# in the right order (yellow then red)


def push_stone(items):
    print_pause("Please enter the number 1 or 2 for the "
                "stone you'd like to push.")
    stone = input("1. Yellow stone on the left\n"
                  "2. Red stone on the right\n")
    if stone == "1":
        yellow_stone(items)
    elif stone == "2":
        red_stone(items)
    else:
        print("Sorry, I don't understand.")
        push_stone(items)


def yellow_stone(items):
    print_pause("You push the yellow stone on the left.")
    if "yellow" in items:
        print_pause("You touched the yellow stone already and nothing "
                    "seems to happen...")
    else:
        print_pause("A little click noise appears, while the stone moves an "
                    "inch into the statue.")
        items.append("yellow")
    print_pause("You pushed the yellow stone and staring again at the stones "
                "of the statue.")
    push_stone(items)


def red_stone(items):
    if "yellow" in items:
        print_pause("As you click the red stone after the yellow stone "
                    "on the statue, a hidden "
                    "compartment under the latin inscriptions opens up.")
        print_pause("You lean towards the statue and inside the compartment "
                    "and gaze upon a bronze intricate little key. ")
        print_pause("As you are still dazzled that such a secret in modern "
                    "Paris still existed, "
                    "you turn you head left and right and hope that nobody "
                    "saw you while touching the stones. ")
        items.append("red")
        key_or_touch_again(items)
    else:
        print_pause("Nothing seems to happen")
        push_stone(items)


# 2. Part - Get the key and return to the hotel afterwards


def key_or_touch_again(items):
    print_pause("Would you like to take the key "
                "and head back to the hotel "
                "or touch the stones again? ")
    further = input("1. Grab the key & head back to the hotel\n"
                    "2. Touch the stones again\n")

    if further == "1":
        items.append("key")
        print_pause("With the key in your hands, it's now time to head "
                    "back to the hotel room quickly not to get caught "
                    "by the cult.")
        narrow_alley(items)

    elif further == "2":
        print_pause("You touch the stones and nothing seems to happen "
                    "anymore...")
        key_or_touch_again(items)
    else:
        print("Sorry, I don't understand. Please enter number 1 or 2 for the "
              "choices.")
        key_or_touch_again(items)


def narrow_alley(items):
    print_pause("After some time you arrive in a narrow alley. "
                "You see a bunch of hooded men rushing towards you "
                "with a edgy grin on their faces.")
    print_pause("Please enter the number 1 or 2 for what to do next ")
    decide = input("1. Turn to another side street, start running and don't "
                   "look back\n"
                   "2. Face the hooded men\n")

    if decide == "1":
        print_pause("Smart move from you ... You are able to gain some meters "
                    "on the hooded men and end up ...")
        way_event(items)

    elif decide == "2":
        print_pause("They gain quickly on you and when you turn around to "
                    "face them, you feel a nerving pain in the back ... ")
        print_pause("...and you feel more and more tired as you sink "
                    "to the ground getting slowly unconscience. ")
        print_pause("As you get dragged away by two of the hodded man, "
                    "another one from the side packs away his little dagger "
                    "with some your blood on it. ")
        print_pause("GAME OVER - Please try again -")
        print("Would you like to play again? Enter 1 for a retry & 2 to "
              "quit")
        Retry = input("1. Retry\n"
                      "2. Quit game\n")
        if Retry == "1":
            play_game()
        elif Retry == "2":
            exit()
        else:
            print("Sorry, I don't understand. Please enter number 1 or 2 for "
                  "the choices.")
    else:
        print("Sorry, I don't understand.")
        narrow_alley(items)


def bridge(items):
    print_pause("on a bridge, where you turn around and hide among "
                "a strolling Chinese tourist group with the lead waving "
                "around with an extra big umbrella. ")
    print_pause("As they don't see you, they turn to different directions "
                "and you are able to return safely to the "
                "hotel and your room. ")
    print_pause("...Where secrets of the little box and the key in your hand"
                " will await you in chapter 2 - the Promise")
    print_pause(" Congratulations - THE END - ")
    exit()


def footpath(items):
    print_pause(" on a little side footpath where you rush to around "
                "the corner. You pass a big old tree, when a tree leave "
                "suddenly drops on your right shoulder. ")
    print_pause(" You turn around hectically and as they don't see you, "
                "you hide away behind the tree for a while until they are "
                "gone and return safely to the hotel and your room. ")
    print_pause("...Where secrets of the little box and the key in your hand"
                " will await you in chapter 2 - the Promise")
    print_pause(" Congratulations - THE END - ")
    exit()


# Random choice of bridge footpath or narrow alley back to the hotel
def way_event(items):
    list = [bridge(items), footpath(items)]
    random.choice(list)


def play_game():
    items = []
    intro()
    push_stone(items)


play_game()
