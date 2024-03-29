import random
import os
from playsound import playsound

def quit():
    raise SystemExit

def dicesound():
    dir = os.path.dirname(__file__) + '/Sounds/diceroll.mp3'
    playsound(dir)

def correctsound():
    dir = os.path.dirname(__file__) + '/Sounds/correct.mp3'
    playsound(dir)

def wrongsound():
    dir = os.path.dirname(__file__) + '/Sounds/wrong.mp3'
    playsound(dir)

def storesound():
    dir = os.path.dirname(__file__) + '/Sounds/storesound.mp3'
    playsound(dir)


title_screen = ("""
.----------------.  .----------------.  .----------------.  .----------------.  .----------------.   .----------------. .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |      __      | || |     ______   | || |  ____  ____  | || |  _________   | | | |    ______    | || |      __      | || | ____    ____ | || |  _________   | |
| | |_  _||_  _| | || |     /  \     | || |   .' ___  |  | || | |_   ||   _| | || | |  _   _  |  | | | |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | |
| |   \ \  / /   | || |    / /\ \    | || |  / .'   \_|  | || |   | |__| |   | || | |_/ | | \_|  | | | | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | |
| |    \ \/ /    | || |   / ____ \   | || |  | |         | || |   |  __  |   | || |     | |      | | | | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | |
| |    _|  |_    | || | _/ /    \ \_ | || |  \ `.___.'\  | || |  _| |  | |_  | || |    _| |_     | | | | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | |
| |   |______|   | || ||____|  |____|| || |   `._____.'  | || | |____||____| | || |   |_____|    | | | |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------' 
""")



dice_art = (("""
    _______            
  /\       \           
 /()\   ()  \          
/    \_______\         
\    /()     /         
 \()/   ()  /          
  \/_____()/
"""))

game_over_art = """
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
"""

total_score = 0
rolls = 3

aside = ["Empty", "Empty", "Empty"]


usedOptions = []

optionList = {
    1: "Ones",
    2: "Twos",
    3: "Fours",
    4: "Fives",
    5: "Sixes",
    6: "Full House",
    7: "Four-Of-A-Kind",
    8: "Little Straight",
    9: "Big Straight",
    10: "Choice",
    11: "Yacht"
}




def showoptions():
    options = [
        "Name:                    Description:                                 Score:",
        "======================================================================================================= ",
        "|(1) Ones:              | Any combination                          | The sum of dice with the 1 face |",
        "|(2) Twos:              | Any combination                           | The sum of dice with the 2 face |",
        "|(3) Fours:             | Any combination                           | The sum of dice with the 4 face |",
        "|(4) Fives:             | Any combination                           | The sum of dice with the 5 face |",
        "|(5) Sixes:             | Any combination                           | The sum of dice with the 6 face |",
        "|(6) Full House:        | Three of one same face and two of another | Sum of all dice                 |",
        "|(7) Four-Of-A-Kind:    | At least four dice showing the same face  | Sum of those four dice          |",
        "|(8) Little Straight:   | 1-2-3-4-5                                 | 30                              |",
        "|(9) Big Straight:      | 2-3-4-5-6                                 | 30                              |",
        "|(10) Choice:           | Any combination                           | Sum of all dice                 |",
        "|(11) Yacht:            | All five dice showing the same face       | 50                              |",
        "======================================================================================================="
    ]

    for i in options:
        print(i)


def diceroll():
    dicelist = []

    min = 1
    max = 6

    for i in range(5):
        roll = random.randint(min, max)
        dicelist.append(roll)


    print("Rolling the dice...")
    print("")
    print(dice_art)
    print("")
    dicesound()

    return dicelist


def taketurn(dicelist, total_score, usedOptions):
    dice = dicelist
    score = 0
    user_option = ""

    input("Press enter to see the move set!\n")
    showoptions()
    print(f"You rolled {dice}")

    while True:
        try:
            user_option = int(input("Please Select Your Option!"))
            if user_option not in range(12):
                print("Invalid Option! Please Try Again!")
            else:
                break
        except ValueError:
            print("That was not a number, Please input a number")
            continue

    if user_option in usedOptions:
        name = optionList.get(user_option)
        print(f"You have chosen {name} Before, Please select a different move!")
        taketurn(dicelist, total_score, usedOptions)
    else:
        pass


    if user_option == 1:
        ones = []
        for i in dice:
            if i == 1:
                ones.append(1)

        if len(ones) == 0:
            print("You had no ones in your dice roll set\nScore this round is 0")
            usedOptions.append(user_option)
            wrongsound()
            game_over_check(usedOptions, total_score)

        else:
            score = len(ones) * 1
            total_score = total_score + score

            print(f"You had {len(ones)} ones in your dice roll set\nScore this round is {score}")
            correctsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)


    elif user_option == 2:
        twos = []
        for i in dice:
            if i == 2:
                twos.append(2)

        if len(twos) == 0:
            print(f"You had no twos in your dice rolls set\nScore this round is 0")
            wrongsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)

        else:
            score = len(twos) * 1
            total_score = total_score + score

            print(f"You had {len(twos)} twos in your dice roll set\nScore this round is {score}")
            correctsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)

    elif user_option == 3:
        fours = []
        for i in dice:
            if i == 4:
                fours.append(4)

        if len(fours) == 0:
            print(f"You had no fours in your dice rolls set\nScore this round is 0")
            wrongsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)

        else:
            score = len(fours) * 1
            total_score = total_score + score

            print(f"You had {len(fours)} fours in your dice roll set\nScore this round is {score}")
            correctsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)


    elif user_option == 4:
        fives = []
        for i in dice:
            if i == 5:
                fives.append(5)

        if len(fives) == 0:
            print(f"You had no fives in your dice rolls set\nScore this round is 0")
            wrongsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)

        else:
            score = len(fives) * 1
            total_score = total_score + score

            print(f"You had {len(fives)} fives in your dice roll set\nScore this round is {score}")
            correctsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)

    elif user_option == 5:
        sixes = []
        for i in dice:

            if i == 6:
                sixes.append(6)

        if len(sixes) == 0:
            print(f"You had no sixes in your dice rolls set\nScore this round is 0")
            wrongsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)

        else:
            score = len(sixes) * 1
            total_score = total_score + score

            print(f"You had {len(sixes)} sixes in your dice roll set\nScore this round is {score}")
            correctsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)

    elif user_option == 6:

        dice = sorted(dice)
        print(dice)

        result = False

        if dice[0] == dice[1] and dice[0] == dice[2]:
            if dice[3] == dice[4]:
                result = True
        elif dice[0] == dice[1]:
            if dice[2] == dice[3] and dice[2] == dice[4]:
                result = True
        else:
            pass

        if result:
            score = sum(dice)
            total_score = total_score + score

            print(f"You rolled a Full House!\nScore this round is {score}")
            correctsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)
        else:
            print(f"You did not roll a Full house!\nScore this round is {score}")
            wrongsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)

    elif user_option == 7:

        result = dice.count(dice[0]) == 4
        if not result:
            result = dice.count(dice[1]) == 4
        else:
            result = result

        if result:
            score = dice[0] * 4
            total_score = total_score + score

            print(f"You rolled four of the same dice\nScore this round is {score}")
            correctsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)

        else:
            print(f"You did not roll four of the same dice\nScore this round is {score}")
            wrongsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)



    elif user_option == 8:
        list = [1, 2, 3, 4, 5]

        result = dice == list

        if result:
            score = 30
            total_score = total_score + score

            print(f"You rolled 1-2-3-4-5! Score this round is {score}")
            correctsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)
        else:
            print(f"You did not roll 1-2-3-4-5 Score this round is 0")
            wrongsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)


    elif user_option == 9:
        list = [2, 3, 4, 5, 6]

        result = dice == list

        if result:
            score = 30
            total_score = total_score + score

            print(f"You rolled 2-3-4-5-6 Score this round is {score}")
            correctsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)
        else:
            print(f"You did not roll 2-3-4-5-6 Score this round is 0")
            wrongsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)

    elif user_option == 10:
        score = sum(dice)
        total_score = total_score + score

        print(f"You rolled {str(dice)} Score this round is {score}")
        correctsound()
        usedOptions.append(user_option)
        game_over_check(usedOptions, total_score)


    elif user_option == 11:
        el = dice[0]

        if dice.count(el) == 5:
            score = 50
            total_score = total_score + score
            print(f"All your dices were the same! Score this round is {score}")
            correctsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)
        else:
            print(f"Your dices were not the same! Score this round is 0")
            wrongsound()
            usedOptions.append(user_option)
            game_over_check(usedOptions, total_score)

    else:
        print("[!] Something went wrong!")
        quit()




def reroll(dice, rolls):
    spare_one = aside[0]
    spare_two = aside[1]
    spare_three = aside[2]

    print("====================")
    print(f"Rolls left: {rolls}")
    print("====================")
    print(f"Stored Dice One: [{spare_one}]"
          f"\nStored Dice Two: [{spare_two}]"
          f"\nStored Dice Three: [{spare_three}]")
    print("====================")

    while True:
        try:
            choice = int(input("Please Select an option!"
                               "\n========================="
                               "\n(1) Re roll a dice"
                               "\n(2) Set aside a dice"
                               "\n(3) Select a stored dice"
                               "\n(4) Exit and take turn"
                               "\n========================="))

            if choice not in range(5):
                print("Invalid Choice, Try again!")
                continue
            else:
                break

        except ValueError:
            print("That was not a number! Please try again")
            continue

        except Exception as err:
            print(f"Something went wrong! >>> {err}")
            quit()

    if choice == 1:
        if rolls == 0:
            print("You have 0 rolls left! Please select another option!\n")
            reroll(dice, rolls)
        else:
            pass
        print(f"You rolled {dice}")
        while True:
            try:
                selection = int(input("Please select the dice number you would like to re-roll"))

                if selection not in range(7):
                    print("Invalid Selection! Please Try again!")
                    continue
                elif selection not in dice:
                    print("The number you selected is not in your dice set! Please try again!")
                    continue
                else:
                    break

            except ValueError:
                print("That was not a number! Please try again!")
                continue

            except Exception as err:
                print(f"Something went wrong! >>> {err}")
                quit()

        new = diceroll()
        new = random.choice(new)
        rolls = rolls - 1
        print(f"You re-rolled {selection} and got a {new}")
        dice.remove(selection)
        dice.append(new)
        print(f"Your dice set is now {dice}")



    elif choice == 2:
        print(f"You rolled {dice}")
        while True:
            try:
                selection = int(input("Please select the dice number you would like to set aside"))

                if selection not in range(7):
                    print("Invalid Selection! Please Try again!")
                    continue
                elif selection not in dice:
                    print("The number you selected is not in your dice set! Please try again!")
                    continue
                else:
                    break

            except ValueError:
                print("That was not a number! Please try again!")
                continue

            except Exception as err:
                print(f"Something went wrong! >>> {err}")
                quit()

        storesound()
        aside.append(selection)
        aside.remove("Empty")
        dice.remove(selection)
        print(f"You have set aside {selection}")

        while True:
            try:
                choicethree = int(input("Would you like to roll a new dice? or access a stored dice to replace the "
                                        "one you set aside?"
                                        "\n==========================================================================="
                                        "======="
                                        "\n(1) Re-roll"
                                        "\n(2) Set aside"))

                if choicethree not in range(3):
                    print("Invalid selection! Please try again!")
                    continue

                else:
                    break

            except ValueError:
                print("That was not a number! Please try again")
                continue

        if choicethree == 1:
            if rolls == 0:
                print("You have 0 rolls left! Please select another option!\n")
                reroll(dice, rolls)
            else:
                pass

            new = diceroll()
            rolls = rolls - 1
            new = random.choice(new)
            dice.append(new)
            print(f"You rolled {new}")
            print(f"Your full dice set is {dice}")

        elif choicethree == 2:
            if aside.count("Empty") == 3:
                print("You have no dice set aside! Please select another option!\n")
            else:
                pass

            while True:
                try:
                    selection = int(input("Please Select A Dice!"
                                        "\n========================"
                                        "Stored Dice:"
                                        f"\n(1) Dice One: {spare_one}"
                                        f"\n(2) Dice Two: {spare_two}"
                                        f"\n(3) Dice Three: {spare_three}"
                                        f"\n========================"))

                    if selection not in range(4):
                        print("Invalid Choice! Please try again!")
                        continue

                    else:
                        if selection == 1:
                            if spare_one == "Empty":
                                print("This slot is empty! Please try again!")
                                continue
                            else:
                                new = spare_one
                                break
                        if selection == 2:
                            if spare_two == "Empty":
                                print("This slot is empty! Please try again!")
                                continue
                            else:
                                new = spare_two
                                break
                        if selection == 3:
                            if spare_three == "Empty":
                                print("This slot is empty! Please try again!")
                                continue
                            else:
                                new = spare_three
                                break

                except ValueError:
                    print("That was not a number! Please try again!")
                    continue

            storesound()
            dice.append(new)
            aside.remove(new)
            print(f"You have selected {new} and it has been added to your dice set!"
                  f"\nYour full dice set is now {dice} ")

    elif choice == 3:
        if aside.count("Empty") == 3:
            print("You do not have any dice set aside! Please select another option!")
            reroll(dice, rolls)
        else:
            pass

        while True:
            try:
                selection = int(input("Please Select A Dice!"
                                      "\n========================"
                                      "Stored Dice:"
                                      f"\n(1) Dice One: {spare_one}"
                                      f"\n(2) Dice Two: {spare_two}"
                                      f"\n(3) Dice Three: {spare_three}"
                                      f"\n========================"))

                if selection not in range(4):
                    print("Invalid Choice! Please try again!")
                    continue

                else:
                    if selection == 1:
                        if spare_one == "Empty":
                            print("This slot is empty! Please try again!")
                            continue
                        else:
                            new = spare_one
                            break
                    if selection == 2:
                        if spare_two == "Empty":
                            print("This slot is empty! Please try again!")
                            continue
                        else:
                            new = spare_two
                            break
                    if selection == 3:
                        if spare_three == "Empty":
                            print("This slot is empty! Please try again!")
                            continue
                        else:
                            new = spare_three
                            break

            except ValueError:
                print("That was not a number! Please try again!")
                continue


        while True:
            try:
                swap = int(input("Please select the dice you would like to swap out!"
                                 f"\nYour dice set is {dice}"))

                if swap not in range(7):
                    print("Invalid choice! Please try again!")
                    contnue
                elif swap not in dice:
                    print("The dice you have selected is not in your dice set! Please try again!")
                else:
                    break

            except ValueError:
                print("That was not a number! Please try again")
                continue


        storesound()
        dice.remove(swap)
        dice.append(new)
        aside.remove(new)
        print(f"You have selected {new} and it has been added to your dice set!"
              f"\nYour full dice set is now {dice} ")


    elif choice == 4:
        taketurn(dice, total_score,  usedOptions)

    else:
        print("[!] Something Went Wrong!")
        quit()




    while True:
        try:
            choicetwo = int(input("Would you like select another option or continue?"
                                  f"\nRolls left: {rolls}"
                                  f"\n==============================================================="
                                  "\n(1) Select another option"
                                  "\n(2) Continue..."
                                  "\n==================================================================="))

            if choicetwo not in range(3):
                print("Invalid choice! Please try again!")
                continue

            else:
                break

        except ValueError:
            print("That was not a number! Please try again!")
            continue

    if choicetwo == 1:
        reroll(dice, rolls)

    elif choicetwo == 2:
        taketurn(dice, total_score,  usedOptions)


    else:
        print("[!] Something went wrong!")
        quit()


def play(total_score):

    print(f"Total Score: {total_score}")
    input("Press ENTER to roll the dice!")
    dice = diceroll()
    print(f"You rolled {dice}")

    while True:
        try:
            choice = int(input("Would you like to re-roll, set aside or access set aside dice?"
                               "\n==============================================================="
                               "\n(1) >>> YES"
                               "\n(2) >>> NO\n"
                               "=================================================================\n"))

            if choice not in range(3):
                print("Invalid Choice! Please try again!")
                continue

            elif choice == 1:
                reroll(dice, rolls)
                os.system("cls")
                break

            elif choice == 2:
                taketurn(dice, total_score,  usedOptions)
                os.system("cls")
                break


        except ValueError:
            print("That was not a number! Try again!")
            continue


def game_over(total_score):
    print(game_over_art)
    print("==================================")
    print(f"TOTAL SCORE: [{total_score}]      ")
    print("===================================")
    quit()

def game_over_check(usedOptions, total_score):
    if len(usedOptions) == 11:
        game_over(total_score)
    else:
        play(total_score)


if __name__ == "__main__":
    print(title_screen)
    print("The aim of the game is to roll sets of 5 dice in order to score points in "
          "accordance with the 12 available moves, each move may only be used once so pick carefully")
    print("")
    print("You may re-roll any dice up to 3 times! You may also set aside dice and re-roll. These set aside dice"
          "may be accessed later one!\n")


    game_over_check(usedOptions, total_score)