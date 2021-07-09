import time

def play_again():
    play = input("Do you want to play again? (Y/N) ")

    if play.upper()== "Y":
        main_room()

    elif play.upper()=="N":
        print("Thanks for playing")
        exit()

    else:
        print("Invalid input. Type (Y/N)")
        play_again()

def game_over():
    print("Try again next time!")
    print("GAME OVER")
    play_again()

def win():
    print("CONGRATULATIONS!!! You have survived the game!")
    trophy = open("trophy.txt","r")
    print(trophy.read())
    trophy.close
    play_again()


def input_check(room1, room2):
    while True:
        user_choice = input("Room 1 or 2: ")
        if user_choice == "1":
            room1()
            break
        elif user_choice == "2":
            room2()
            break
        else:
            print("invalid input! Please type 1 or 2")
def main_room():
    print("Find the treasure!")
    print("_"*200)
    time.sleep(2)
    print("You have to find the treasure through these different rooms!")
    print("There are 6 rooms in total, each with 2 doors. ")
    print("To win, you must choose the correct door in each room to progress")
    print("Choose your first door...")
    print("Door 1: Highway")
    print("Door 2: Mines")

    input_check(highway, mines)

def highway():
    print("You've just been run over by a car!")
    game_over()

def mines():
    print("You have gone into a mine. Luckily this mine is safe.")
    print("Now time to choose the next door...")
    print("Door 1: Factory")
    print("Door 2: Airport")
    input_check(factory,airport)

def factory():
    print("There are machines in the room. You just ran into one of the machines!")
    game_over()

def airport():
    print("You have arrived at the airport. There are many flights to different locations.")
    print("Door 1: Floating Ruins")
    print("Door 2: Area Forest")
    print("")
    input_check(floating_ruins,area_forest)

def floating_ruins():
    print("You have fallen off the moving platforms to your demise!")
    game_over()

def area_forest():
    print("You have arrived at the forest. This forest has many different species of plants and animals. ")
    print("These animals won't harm you, so you're safe!")
    print("Door 1: Train")
    print("Door 2: Cyberspace")
    input_check(train, cyberspace)

def train():
    print("On board the train there is an evil guy who stabbed you!")
    game_over()

def cyberspace():
    print("You have arrived at the cyberspace. This is the place where real life and the internet meet.")
    print("You have one more room to go!")
    print("Door 1: Volcano")
    print("Door 2: Oil Field")
    input_check(volcano, oil_field)

def volcano():
    print("You have fallen into the magma inside the volcano! You have been burned!")
    game_over()

def oil_field():
    print("You have arrived at a desolate oil field. There is a buried treasure somewhere in the sand.")
    print("All you have to do is type the magic word.")
    print("CONGRATULATIONS")
    print("")
    choice = input("Type the magic word here: ")
    if choice.upper() == "CONGRATULATIONS":
        win()
    else:
        print("The word was not said correctly!")
        game_over()


main_room()
