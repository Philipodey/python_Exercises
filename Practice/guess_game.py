import random
_philip = random.randint(1, 10)
number = int(input("Enter a number and enter 20 to quit: "))
if number != _philip:
    print("Try Again")
while number != _philip:
    number = int(input("Enter a number and enter 20 to quit: "))
    if number == _philip:
        print("Congratulations! You won!")
    else:
        print("Try Again!")



        # if number == _philip:
        #     print("Congratulations! You won!")
