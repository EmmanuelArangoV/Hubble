def print_patient(patient):
    print(f"Id: {patient.get('id')}, Name: {patient.get('name')}, "
          f"Age: {patient.get('age')}, Diagnosis: {patient.get('diagnosis')}")

    print("Record of events:")
    for event in patient.get('record', []):
        print(" - ", event)
    print("")

def update_age(i):
    print_patient(i)
    new_age = int(input("You chose to modify age, enter the age to update: "))
    confirm_age = input("You are about to modify the age, are you sure? yes/no: ").lower()
    if confirm_age == "yes":
        print("The age was successfully updated, here is the information \n")
        i.update({"age" : new_age})
        print_patient(i)
    else:
        print("You did not modify the age")

def update_diagnosis(i):
    print_patient(i)
    menu = ("Enter your new diagnostic\n1) Hypertension\n2) Diabetes Mellitus\n3) Upper Respiratory Infection\n"
            "4) Urinary Tract Infection\n5) Allergic Rhinitis\n-> ")
    option = input(menu)
    if option == "1":
        new_diagnosis = "Hypertension"
    elif option == "2":
        new_diagnosis = "Diabetes Mellitus"
    elif option == "3":
        new_diagnosis = "Upper Respiratory Infection"
    elif option == "4":
        new_diagnosis = "Urinary Tract Infection"
    elif option == "5":
        new_diagnosis = "Allergic Rhinitis"
    else:
        print("The option does not exist, the diagnosis will not be changed")
        return

    confirm_diagnosis = input("You are about to modify the diagnosis, are you sure? yes/no: ").lower()
    if confirm_diagnosis == "yes":
        print("The diagnosis was successfully updated, here is the information \n")
        i.update({"diagnosis" : new_diagnosis})
        print_patient(i)
    else:
        print("You did not modify the diagnosis")

def update_record(i):
    print_patient(i)
    add_record = input("You chose to modify record, enter the record to update: ")
    confirm_add_record = input("You are about to modify the record, are you sure? yes/no: ").lower()
    if confirm_add_record == "yes":
        print("The record was successfully added, here is the information \n")
        i["record"].append(add_record)
        print_patient(i)

def update_patient(patients):
    while True:
        found = False
        print("You have found the patient, what would you like to modify?")
        print("==> 1. Age")
        print("==> 2. Diagnosis")
        print("==> 3. Record")
        print("==> 0. Exit")
        option = input("Choose an option: ")
        if option == "0":
            break
        if option not in ["1", "2", "3"]:
            print(f"The option {option} does not exist")
        else:
            id = input("Enter the ID to modify the patient: ")
            for i in patients:
                if id == i.get("id"):
                    found = True
                    if option == "1":
                        update_age(i)
                    elif option == "2":
                        update_diagnosis(i)
                    elif option == "3":
                        update_record(i)
            if not found:
                print("The ID does not exist")