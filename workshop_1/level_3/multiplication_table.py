print("Do you want to learn the multiplication table?")

while True:
    try:
        number = int(input("Enter the number to generate its multiplication table: "))
        for i in range(11):
            result = number * i
            print(f"{number} * {i} = {result}")

        response = input("Would you like to continue? Press Y to continue ").capitalize()
        if response != "Y":
            break
    except ValueError:
        print("This is not a valid number.")