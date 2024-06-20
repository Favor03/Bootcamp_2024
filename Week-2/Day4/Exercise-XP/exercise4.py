import random

def food(number):
    if number < 1 or number > 100:
        print("\n Please enter a number between 1 and 100\n")
        return number
    else:
        random_number = random.randint(1, 100)
        if random_number == number:
            print("\n !!!!! Good Boy.!!!!! You have made it\n")
        else:
            print("\n!!! Sorry. Try again next time\n")

food(4)

