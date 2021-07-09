import random
win = 0
tries = 1
computer_number = random.randint(1,20)
while tries <=3:
    user_number = int(input("Enter a number from 1 to 20: "))
    if user_number == computer_number:
        print("Congratulations! You won the lottery. Contact us to claim your prize.")
        win = 1
        break
    elif user_number > computer_number:
        print("your guess is too large!")
    elif user_number < computer_number:
        print("your guess is too small!")
    tries = tries+1 #tries+=1
if win == 0:
    print("Sorry, you've exhausted all your tries and you've lost the game! The number is", computer_number)