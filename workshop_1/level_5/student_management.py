students = {
    "1013341987": {"name": "Emmanuel", "birthday": "21/12/2006", "phone": "3193696490", "city": "Medellín", "age": 19, "subject": []},
    "21490227": {"name": "Valentina", "birthday": "22/11/2005", "phone": "3217910940", "city": "Bogotá", "age": 20, "subject": []}
}

menu = (""
        "1. Add students\n"
        "2. Remove student\n"
        "3. Print students\n"
        "4. Filter students\n"
        "5. Update student info\n"
        "6. Show specific student\n"
        "7. Inscribe subjects for student\n"
        "8. Exit program\n")

subjects = [
    "Chemistry",
    "Physics",
    "Maths",
    "Arts",
    "Biology"
]

filter_menu = (""
               "1. For a subject\n"
               "2. For two subjects\n"
               "3. For age\n"
               "4. For city of residency\n"
               "5. Exit\n")

# Brief: main loop - prompt user for action until they choose to exit
while True:
    print("Please select an option:")
    choice = input(menu)

    # Option 1: Add student - collect personal info, validate age and add to 'students' if new
    if choice == "1":
        document = input("Enter student document: ")
        if document not in students:
            name = input("Enter student name: ").capitalize()
            birthday = input("Enter student birthday (DD/MM/YYYY): ")
            phone = input("Enter student phone number: ")
            city = input("Enter student residency city: ").capitalize()
            while True:
                try:
                    age = int(input("Enter student age: "))
                    if age <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid age.")
            students[document] = {"name": name, "birthday": birthday, "phone": phone, "city": city, "age": age, "subject": []}
        else:
            print("It's seems like this student is already registered on the database.")
    # Option 2: Remove student - check existence, confirm, then delete entry
    elif choice == "2":
        document = input("Enter student document: ")
        if document in students:
            answer = input("Do you want to remove this student. Press (Y) to continue: ").capitalize()
            if answer == "Y":
                students.pop(document)
                print("Student removed successfully.")
            else:
                print("Student removement cancelled.")
        else:
            print("This student is not registered on the database.")
    # Option 3: Print students - list document and name for each registered student
    elif choice == "3":
        print("Students in the database: ")
        for document in students:
            print(f"Document: {document}, Name: {students[document]['name']}")
    # Option 4: Filter students - allow filtering by subject(s), age or city and print matches
    elif choice == "4":
        while True:
            print("How do you want to filter the students?")
            subchoice = input(filter_menu)
            filter_students = {}
            # Filter by single subject: check subject validity and collect matching students
            if subchoice == "1":
                subject = input("Enter subject: ").capitalize()
                if subject in subjects:
                    for document in students:
                        student_subject = students[document]["subject"]
                        if subject in student_subject:
                            filter_students[document] = students[document]["name"]
                    print("Result of the filter:")
                    for student in filter_students:
                        print(f"Student: {student}, Name: {filter_students[student]}")
                else:
                    print("Invalid subject.")
            # Filter by two subjects: require both subjects present for each student
            elif subchoice == "2":
                subject1 = input("Enter subject: ").capitalize()
                subject2 = input("Enter subject: ").capitalize()
                if subject1 in subjects and subject2 in subjects:
                    for document in students:
                        student_subject = students[document]["subject"]
                        if subject1 in student_subject and subject2 in student_subject:
                            filter_students[document] = students[document]["name"]
                    print("Result of the filter:")
                    for student in filter_students:
                        print(f"Student: {student}, Name: {filter_students[student]}")
                else:
                    print("Invalid subject or subjects.")
            # Filter by age: parse and validate age, then match equality
            elif subchoice == "3":
                try:
                    age = int(input("Enter student age: "))
                    if age <= 0:
                        raise ValueError
                    for document in students:
                        student_age = students[document]["age"]
                        if student_age == age:
                            filter_students[document] = students[document]["name"]
                    print("Result of the filter:")
                    for student in filter_students:
                        print(f"Student: {student}, Name: {filter_students[student]}")
                except ValueError:
                    print("Invalid age.")
            # Filter by city: compare city names (capitalization normalized)
            elif subchoice == "4":
                city = input("Enter city: ").capitalize()
                for document in students:
                    student_city = students[document]["city"]
                    if student_city == city:
                        filter_students[document] = students[document]["name"]
                print("Result of the filter:")
                for student in filter_students:
                    print(f"Student: {student}, Name: {filter_students[student]}")
            elif subchoice == "5":
                break
            else:
                print("Invalid input.")
    # Option 5: Update student info - find by document and replace name/phone/city
    elif choice == "5":
        document = input("Enter student document: ").capitalize()
        if document in students:
            name = input("Enter student name: ").capitalize()
            phone = input("Enter student phone number: ").capitalize()
            city = input("Enter student residency city: ").capitalize()
            students[document]["name"] = name
            students[document]["phone"] = phone
            students[document]["city"] = city
        else:
            print("The student is not registered on the database.")
    # Option 6: Show specific student - display full details for a given document
    elif choice == "6":
        document = input("Enter student document: ").capitalize()
        if document in students:
            print(f"Document: {document}, Name: {students[document]["name"]}, Phone: {students[document]["phone"]}, "
                  f"City: {students[document]["city"]}, Age: {students[document]["age"]}")
    # Option 7: Inscribe subjects - present subjects list, validate choice and append if not enrolled
    elif choice == "7":
        document = input("Enter student document: ").capitalize()
        if document in students:
            while True:
                print("Select which subject you want to inscribe")
                for i, subject in enumerate(subjects, start=1):
                    print(f"{i}. {subject}")
                subchoice = input("0. Exit\n")
                if subchoice == "0":
                    break
                try:
                    idx = int(subchoice)
                    # Note: validate numeric input and index bounds when selecting a subject
                    if not 0 <= idx < len(subjects):
                        raise ValueError
                    student_subjects = students[document]["subject"]
                    subject = subjects[idx - 1]
                    if subject in student_subjects:
                        print("Student already enrolled in that subject.")
                    else:
                        student_subjects.append(subject)
                        students[document]["subject"] =  student_subjects
                        print(f"Subject {subject} is now enrolled.")
                except ValueError:
                    print("Invalid input.")
        else:
            print("The student is not registered on the database.")
    # Option 8: Exit program - print farewell and break the loop
    elif choice == "8":
        print("Thank you for your time!")
        break
    # Invalid input: notify the user and continue loop
    else:
        print("Invalid input.")