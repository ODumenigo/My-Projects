import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(enemy):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, and "
                f"has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")


def house_or_cave(items, enemy):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = input("(Please enter 1 or 2.)")
    if choice == '1':
        house(items, enemy)
    elif choice == '2':
        cave(items, enemy)
    else:
        print_pause("Sorry, I don't understand.")
        house_or_cave(items, enemy)


def cave(items, enemy):
    if "sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        house_or_cave(items, enemy)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Excalibur!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        print_pause("You walk back out to the field.")
        items.append("sword")
        house_or_cave(items, enemy)


def door(enemy):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps "
                f"a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")


def house(items, enemy):
    if "sword" in items:
        door(enemy)
        print_pause("Would you like to (1) fight or (2) run away?")
        choice = valid_input()
        if choice == '1':
            print_pause(f"As the {enemy} moves to attack, you unsheathe your"
                        f" new sword.")
            print_pause("The Sword of Excalibur shines brightly in your hand"
                        " as you brace yourself for the attack.")
            print_pause(f"But the {enemy} takes one look at your shiny new toy"
                        f" and runs away!")
            print_pause(f"You have rid the town of the {enemy}."
                        f" You are victorious!")
            play_again()
        elif choice == '2':
            print_pause("You run back into the field. Luckily, you don't seem"
                        " to have been followed.")
            house_or_cave(items, enemy)
    else:
        door(enemy)
        print_pause("You feel a bit under-prepared for this, what with only"
                    " having a tiny dagger.")
        print_pause("Would you like to (1) fight or (2) run away?")
        choice = valid_input()
        if choice == '1':
            print_pause("You do your best...")
            print_pause(f"Your dagger is no match for the {enemy}.")
            print_pause("You have been defeated!")
            play_again()
        elif choice == '2':
            print_pause("You run back into the field. Luckily, you don't seem"
                        " to have been followed.")
            house_or_cave(items, enemy)


def valid_input():
    while True:
        choice = input("Please enter 1 or 2")
        if choice == '1':
            break
        elif choice == '2':
            break
        else:
            print_pause("Sorry, I don't understand.")
    return choice


def play_again():
    choice = input("Would you like to play again? (y/n)").lower()
    if choice == "y":
        play_game()
    elif choice == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        print_pause("Sorry, I don't understand.")
        play_again()


def play_game():
    items = []
    enemy = random.choice(["wicked fairy", "dragon", "ogre", "pirate",
                           "gorgon", "troll"])
    intro(enemy)
    house_or_cave(items, enemy)


play_game()
