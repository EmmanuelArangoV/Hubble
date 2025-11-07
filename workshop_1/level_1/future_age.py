while True:
    print("How old will you be in ten years?")
    try:
        current_age = int(input("Please enter your current age: "))
        if current_age < 0:
            print("Please enter a valid age")
            continue
        future_age = current_age + 10
        print(f"In ten years, you will be {future_age} years old.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue

    respone = input("Would you like to continue? Press (Y) to continue: ").capitalize()
    if respone != "Y":
        break