# students: mapping of student document -> dict with subjects and their grades
# menu/submenu: strings displayed to the user for main and subject choices
students = {}
menu = "1. Enter student.\n2. Enter/Update grades.\n3. Calculate grades.\n4.Delete student.\n5. Show students.\n6. Exit\n"
submenu = "1. Programming.\n2. English.\n3. Exit\n"

# ingresarNotas: collect three valid grades (0-5) from user and return them as a list
def ingresarNotas():
    grades = []
    i = 0
    while i < 3:
        try:
            grade = float(input(f"Enter the grade {i + 1}: "))
            if 0 <= grade <= 5:
                grades.append(grade)
                i += 1
            else:
                raise ValueError
        except ValueError:
            print("You have entered and invalid value for the grade. Please make sure is a positive number.")
    return grades

# calculateGrades: compute average of a grades list, round to 2 decimals; return "No grades" if None
def calculateGrades(grades):
    if grades is None:
        return "No grades"
    averageGrade = sum(grades) / len(grades)
    return round(averageGrade, 2)

# Main welcome and interactive loop: present menu and handle user choices repeatedly
print("Welcome to the Grade System.")
while True:
    choice = input(menu)
    # Option 1: Register a new student if not already present
    if choice == "1":
        student = input("Enter the student document: ")
        if student not in students:
            students[student] = {"Programming": None, "English": None}
        else:
            print("This student has already been registered.")
    # Option 2: Enter or update grades for a selected subject via submenu
    elif choice == "2":
        student = input("Enter the student document: ")
        if student in students:
            while True:
                print(f"You're working on student {student}.")
                subchoice = input(submenu)
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
    # Option 3: Calculate and display average for a subject (Programming or English)
    elif choice == "3":
        student = input("Enter the student document: ")
        if student in students:
            while True:
                print(f"You're working on student {student}.")
                subchoice = input(submenu)
                if subchoice == "1":
                    if students[student]["Programming"] is None:
                        print("There is no grades in this subject for this student.")
                    else:
                        grade = calculateGrades(students[student]["Programming"])
                        print(f"The student {student} has {grade} in the subject of Programming.")
                elif subchoice == "2":
                    if students[student]["English"] is None:
                        print("There is no grades in this subject for this student.")
                    else:
                        grade = calculateGrades(students[student]["English"])
                        print(f"The student {student} has {grade} in the subject of English.")
                elif subchoice == "3":
                    break
                else:
                    print("Invalid option")
        else:
            print("The student doesn't exist.")
    # Option 4: Delete a student after confirmation
    elif choice == "4":
        student = input("Enter the student document: ")
        if student in students:
            subchoice = input("Are you sure on deleting the student. Press (Y) to continue.").capitalize()
            if subchoice == "Y":
                students.pop(student)
                print("Student deleted successfully.")
            else:
                print("Delete action cancelled.")
        else:
            print("The student doesn't exist.")
    # Option 5: Show all students with their computed averages per subject
    elif choice == "5":
        for student in students:
            english = calculateGrades(students[student]["English"])
            programming = calculateGrades(students[student]["Programming"])
            print(f"The student {student}: English: {english}, Programming: {programming}")
    # Option 6: Exit the program
    elif choice == "6":
        print("Thank you for using Grade System.")
        break
    else:
        # Handle invalid menu input
        print("Invalid option.")