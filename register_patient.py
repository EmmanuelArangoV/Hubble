patients = []
def register_patients():
    while True:

        print("... CLINIC MANAGER ...")
        patient_id = input("\nEnter the patient ID -> ")

        flag = patient_exists(patient_id)
        if not flag:
            name = input("Enter your name -> ").capitalize()
            age = age_correct()
            gender = patient_gender()
            diagnostic = diagnostics()
            record = record_events()

            patient = { "id": patient_id, "name": name, "age": age,
                "gender": gender, "diagnostic": diagnostic, "record": record }
            patients.append(patient)
        else:
            print("\nThat  patient already exists")

        continue_registration = input("\nDo you wish to register another patient? 'Y' to continue -> ").capitalize()

        if continue_registration != "Y":
            break


def patient_exists(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            print("The user with that ID already exists")
            return True
    return False


def age_correct():
    while True:
        try:
            age = int(input("Enter your age -> "))
            if age <= 0:
                raise ValueError
            return age
        except ValueError:
            print("\ninvalid age")


def patient_gender():
    gender = input("\nEnter your gender\n1) Male\n2) Female\n3) No binary\n-> ")

    while True:
        if gender == "1":
            return "Male"
        elif gender == "2":
            return "Female"
        elif gender == "3":
            return "No binary"
        else:
            print("\nInvalid gender")
            gender = input("Enter your gender\n1) Male\n2) Female\n3) No binary")


def record_events():
    record = []
    while True:
        event = input("Enter an event -> ")
        record.append(event)

        choice = input("\nDo you want to add another event. Press 'Y' to continue-> ").capitalize()

        if choice != "Y":
            break
    return record

def diagnostics():
    menu = "\nEnter your diagnostic\n1) Hypertension\n2) Diabetes Mellitus\n3) Upper Respiratory Infection\n4) Urinary Tract Infection\n5) Allergic Rhinitis\n-> "
    diagnostic = input(menu)

    while True:
        if diagnostic == "1":
            return "Hypertension"
        elif diagnostic == "2":
            return "Diabetes Mellitus"
        elif diagnostic == "3":
            return "Upper Respiratory Infection"
        elif diagnostic == "4":
            return "Urinary Tract Infection"
        elif diagnostic == "5":
            return "Allergic Rhinitis"
        else:
            print("\nInvalid diagnostic")
            diagnostic = input(menu)


register_patients()


