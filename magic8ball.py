import random
print("Welcome to the Magic 8 Ball")
print("_"*100)
print("You're about to unleash your future!")
print("1.Career")
print("2.Relationships")
print("3.Kids")
career = ["You'll have a prosperous career","You will be bankrupt by 40", "You will end up unemployed" "You will be a millionare by 45"]
relationships = ["You will have a good future with your partner","You will be the love of someone's life", "You will have a happy family" "You will breakup and divorce"]
kids = ["Your kids will behave well." ]
name = input("what's your name? ")
user_choice = input("What do you want to know about (1/2/3)")
if user_choice == "1":
    response = str(random.choices(career)).replace('[','').replace(']','').replace("'","")
    print(f"{name}, {response}")

elif user_choice == "2":
    response = str(random.choices(relationships)).replace('[','').replace(']','').replace("'","")
    print(f"{name}, {response}")

elif user_choice == "3":
    response = str(random.choices(kids)).replace('[','').replace(']','').replace("'","")
    print(f"{name}, {response}")

