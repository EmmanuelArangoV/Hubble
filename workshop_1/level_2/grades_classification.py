# Brief: Classify a numeric grade into Failed, Approved or Excellent.
# Input: reads a float grade, validates numeric input and checks ranges.
# Edge cases: handles grades outside expected range and non-numeric input.
# Flow: repeats until the user declines to continue.

print("Welcome to the Grades Classification")

while True:
    try:
        grade = float(input("Enter your grade: "))

        if 0 <= grade <= 2.9:
            print(f"Your grade {grade} is classified as: Failed")
        elif 2.9 < grade <= 4.0:
            print(f"Your grade {grade} is classified as: Approved")
        elif 4.0 < grade <= 5.0:
            print(f"Your grade {grade} is classified as: Excellent")
        elif grade >= 5.1 or grade < 0.0:
            print(f"Your grade {grade} is classified as: Unavailable")

    except ValueError:
        print("Please enter a numeric value")
        continue

    response = input("Would you like to continue with another grade? Press (Y) to continue: ").capitalize()
    if response != "Y":
        break