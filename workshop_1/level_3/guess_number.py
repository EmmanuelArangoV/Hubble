import random

print("Guess the number")

while True:
    try:
        range1 = int(input("Please enter one of the limits: "))
        range2 = int(input("Please enter one of the limits: "))
        if range1 > range2:
            number = random.randint(range2, range1)
        elif range2 > range1:
            number = random.randint(range1, range2)
        else:
            print("The intervale is not valid")
            continue

        guess = 0
        while number != guess:
            guess = int(input("Guess the number: "))
            if number > guess:
                print("The real number is greater than the guess.")
            elif number < guess:
                print("The real number is less than the guess.")
        print("You guessed the number!")
        
        response = input("Would you like to continue? Press Y to continue ").capitalize()
        if response != "Y":
            break
    except ValueError:
        print("This is not a valid number.")
