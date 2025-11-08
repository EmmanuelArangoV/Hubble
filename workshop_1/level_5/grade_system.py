students = {}

menu = "1. Enter student.\n2. Enter grades.\n3. Calculate grades.\n4. Exit"
submenu = "1. Programming.\n2. English.\n3. Exit"

def ingresarNotas():
    grades = []
    i = 0
    while i < 3:
        try:
            grade = float(input(f"Enter the grade {i + 1}"))
            if 0 <= grade <= 5:
                grades.append(grade)
                i += 1
            else:
                raise ValueError
        except ValueError:
            print("You have entered and invalid value for the grade. Please make sure is a positive number.")
    return grades

print("Welcome to the Grade System.")
while True:
    choice = input(menu)

    if choice == "1":
        student = input("Enter the student document")
        students[student] = {"Programming": [], "English": []}
    elif choice == "2":
        student = input("Enter the student document")
        if student in students:
            while True:
                print(submenu)
                subchoice = input(menu)
                if subchoice == "1":
                    grades = ingresarNotas()
                    students[student]["Programming"] = grades
                elif subchoice == "2":
                    grades = ingresarNotas()
                    students[student]["English"] = grades
                elif subchoice == "3":
                    break
                else:
                    print("Invalid option")
        else:
            print("The student doesn't exist.")