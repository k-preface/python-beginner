import random

rando = random.randint(1,4)

if rando == 1:
    print("you're a Slytherin")
elif rando == 2:
    print("you're a Gryfindor!")
elif rando == 3:
    print("you're a Ravenclaw")
else:
    print("you're a Hufflepuff")

# for lists in python, the pos number starts from 0
#
# houses[2] = "gryffindor"
# houses.append("preface coding")

# houses.remove("griffindor")
# del houses[0]

#for loops
#for number in range(1,11)
    #print(number)
import time

for number in range(1,51):
    if number % 5 ==0 and number % 3 ==0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

    time.sleep(2)







