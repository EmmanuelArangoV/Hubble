def print_patient(patient):
    print(f"Id: {patient.get('id')}, Name: {patient.get('name')}, "
          f"Age: {patient.get('age')}, Diagnosis: {patient.get('diagnosis')}")

    print("Record of events:")
    for event in patient.get('record', []):
        print(" - ", event)
    print("\n")

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
    new_diagnosis = input("You chose to modify diagnosis, enter the diagnosis to update: ")
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
        option = -99
        id = int(input("Enter the ID to modify the patient: "))
        if id == -1:
            print("Ending the program")
            break
        while option != 0:
            for i in patients:
                if id == i.get("id"):
                    print("You have found the patient, what would you like to modify?")
                    print("==> 1. Age")
                    print("==> 2. Diagnosis")
                    print("==> 3. Record")
                    print("==> 0. Exit")
                    option = int(input("Choose an option: "))
                    if option != 0:
                        if option == 1:
                            update_age(i)
                        elif option == 2:
                            update_diagnosis(i)
                        elif option == 3:
                            update_record(i)
                        else:
                            print(f"The option {option} does not exist")
                    else:
                        break