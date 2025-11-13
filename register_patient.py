patients = []
def register_patients():
    while True:

        patient_id = input("Enter the patient ID -> ")

        flag = patient_exists(patient_id)
        if not flag:
            name = input("Enter your name -> ").capitalize()
            age = age_correct()
            gender = patient_gender()
            diagnostic = input("Enter your diagnostic -> ")
            record = record_events()

            patient = { "id": patient_id, "name": name, "age": age,
                "gender": gender, "diagnostic": diagnostic, "record": record }
            patients.append(patient)
        else:
            print("That  patient already exists")

        continue_registration = input("Do you wish to register another patient? 'Y' to continue -> ").capitalize()

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
            print("invalid age")


def patient_gender():
    gender = input("Enter your gender\n1) Male\n2) Female\n3) No binary\n-> ")

    while True:
        if gender == "1":
            return "Male"
        elif gender == "2":
            return "Female"
        elif gender == "3":
            return "No binary"
        else:
            print("Invalid gender")
            gender = input("Enter your gender\n1) Male\n2) Female\n3) No binary")


def record_events():
    record = []
    while True:
        event = input("Enter an event -> ")
        record.append(event)

        choice = input("Do you want to add another event. Press 'Y' to continue-> ").capitalize()

        if choice != "Y":
            break
    return record


register_patients()


