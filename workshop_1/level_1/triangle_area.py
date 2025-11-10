# Calculate the area of a triangle from user-provided base and height.
# Validation: ensure numeric input and that base and height are non-negative.
# Behavior: compute (base * height) / 2 and print result; repeat on invalid input.

print("Let's go to calculate the area of a new Triangle")

while True:
    try:
        height = float(input("Enter the height of the triangle: "))
        base = float(input("Enter the base of the triangle: "))

        if height < 0 or base < 0:
            raise ValueError
        else:
            area = (height * base)/2
            print(f"The area of the triangle is {area}.")

    except ValueError:
        print("Please enter a positive number.")
