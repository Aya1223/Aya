import time
import random


def begin():
    print_pause("option 1: You decide to face the monsters alone, "
                "hoping to save the person")
    print_pause("option 2: go deep into the forest to search for "
                "a weapon that might help you eliminate monsters "
                "and save a person")
    answer = input("choose option 1 or 2 ?").lower()
    while answer != '1' and answer != '2':
        answer = input("choose option 1 or 2 ?").lower()
    if '1' in answer:
        try_save_him_alone()
    elif '2' in answer:
        go_to_forest()


def go_to_forest():
    print_pause("Instead of a direct confrontation, "
                "you decided to head deep into the forest")
    print_pause("searching for a weapon with which you could "
                "defeat the monster and save the person")
    print_pause("You find an old man sitting under a tree, "
                "holding a huge sword")
    print_pause("The old man asks you to bring him a certain "
                "stone found deep in the forest in exchange "
                "for him giving you the sword")
    man_options()


def man_options():
    print_pause("option1: accept the old man's request "
                "and go to get the thing he asked for\n")
    print_pause("option2: You go and search deep in the "
                "forest for something else to help you\n")
    answer = input("choose option 1 or 2 ?").lower()
    while answer != '1' and answer != '2':
        answer = input("choose option 1 or 2 ?").lower()
    if '1' in answer:
        mission()
    elif '2' in answer:
        go_deep_in_forest()


def go_deep_in_forest():
    print_pause("You decided to ignore the old man's request "
                "and continue searching for another weapon"
                "that could help you in the confrontation.")
    print_pause("You ran, climbed, and explored for days, "
                "but you couldn't find a suitable weapon"
                "with which to take down the monster")
    print_pause("After you were tired and frustrated")
    print_pause("option 1: go back to the old man and do "
                "the mission he asked to get the sword\n")
    print_pause("option 2: go deep into the forest and search more\n")
    answer = input("choose option 1 or 2 ?").lower()
    while answer != '1' and answer != '2':
        answer = input("choose option 1 or 2 ?").lower()
    if '1' in answer:
        mission()
    elif '2' in answer:
        go_deep_in_forest()


def mission():
    print_pause("You agreed to the old man's request, and went to "
                "search for the required item.")
    print_pause("You went through the challenges of the forest, "
                "faced dangerous creatures and various problems")
    print_pause("You couldn't find the required stone "
                "yet and started to give up")
    print_pause("What will you do?\n")
    print_pause("option 1: You bring a fake stone, "
                "knowing that it may expose you\n")
    print_pause("option 2: Do not give up and search deeper into the forest\n")
    answer = input("choose option 1 or 2 ?").lower()
    while answer != '1' and answer != '2':
        answer = input("choose option 1 or 2 ?").lower()
    if '1' in answer:
        finish_mission()
    elif '2' in answer:
        try_more()


def try_more():
    global stone
    print_pause("After a very long search, you have finally found the stone")
    stone = True
    finish_mission()


def finish_mission():
    print_pause("You turned back to the old man")
    if stone:
        print_pause("The old man checked that the stone "
                    "was the same one he wanted")
        print_pause("He gave you the sword you wanted")
        print_pause("You went to fight the monster"
                    "and saved the person (you won!)")
        play_again()
    elif not stone:
        print_pause("The old man could tell you were lying to him")
        print_pause("But he gave you another chance to bring the stone")
        print_pause("option 1: You go and look again for the real stone\n")
        print_pause("option 2: refuse the old man's request\n")
        answer = input("choose option 1 or 2 ?").lower()
        while answer != '1' and answer != '2':
            answer = input("choose option 1 or 2 ?").lower()
        if '1' in answer:
            try_more()
        elif '2' in answer:
            refuse()


def refuse():
    print_pause("You refused the old man's request")
    print_pause("The old man will never give you the sword")
    print_pause("The monsters killed the person who wanted to help ")
    GameOver()


def try_save_him_alone():
    print_pause("You rush at the monster and attack it")
    print_pause("unfortunately it turns out that he is very"
                "strong and you cannot confront him without a weapon")
    GameOver()


def GameOver():
    print_pause("You've been eliminated (You've lost)")
    play_again()


def play_again():
    answer = input("Do you wanna play again?(yes/no)").lower()
    while answer != 'no' and answer != 'yes':
        answer = input("Do you wanna play again?(yes/no)").lower()
    if answer == 'yes':
        intro()
    elif answer == 'no':
        print("Goodbye!")


def start():
    global monster
    global stone
    stone = False
    monster = random.choice(monsters)


def print_pause(text):
    print(text)
    time.sleep(2)


def intro():
    start()
    print_pause("While you are walking in a forest"
                "in the middle of the night\n")
    print_pause("you hear the sound of screaming coming"
                "from behind the trees\n")
    print_pause("You find a weak person being attacked by "
                f"{monster} monster and you have no weapon to confront")
    begin()


monsters = ['Dracula', 'Werewolf', 'Kraken', 'Bigfoot']
monster = random.choice(monsters)
stone = False
intro()
