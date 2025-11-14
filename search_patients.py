def print_patient(patient):
    print(f"Id: {patient.get('id')}, Name: {patient.get('name')}, "
          f"Age: {patient.get('age')}, Diagnosis: {patient.get('diagnosis')}")

    print("Record of events:")
    for event in patient.get('record', []):
        print(" - ", event)
    print("")

def search_by_id(patients, value):
    found = False
    for patient in patients:
        if patient.get('id') == value:
            found = True
            print_patient(patient)

    if not found:
        print("Patient not found")

def search_by_name(patients, value):
    found = False
    for patient in patients:
        if value in patient.get('name'):
            found = True
            print_patient(patient)
    if not found:
        print("Patients not found")

def search_by_diagnosis(patients, value):
    found = False
    for patient in patients:
       if value == patient.get('diagnosis'):
           found = True
           print_patient(patient)
    if not found:
        print("Patients not found")

def filter(patients):

    filter_gender = input("filter by gender -> ").capitalize()

    filter_patients = []
    if filter_gender == "Male":

        for patient in patients:
            if patient["gender"] == filter_gender:
                filter_patients.append(patient)
        if len(filter_patients) == 0:
            print("no male patients")
        else:
            print("Male patients")
            for patient in filter_patients:
                print(f"name: {patient['name']}, age: {patient['age']}, diagnosis: {patient['diagnosis']}")
            print("")
    elif filter_gender == "Female":

        for patient in patients:
            if patient["gender"] == filter_gender:
                filter_patients.append(patient)
        if len(filter_patients) == 0:
            print("no female patients")
        else:
            print("Female patients")
            for patient in filter_patients:
                print(f"name: {patient['name']}, age: {patient['age']}, diagnosis: {patient['diagnosis']}")
            print("")
    elif filter_gender == "No binary":

        for patient in patients:
            if patient["gender"] == filter_gender:
                filter_patients.append(patient)
        if len(filter_patients) == 0:
            print("no no binary patients")
        else:
            print("No binary patients")
            for patient in filter_patients:
                print(f"name: {patient['name']}, age: {patient['age']}, diagnosis: {patient['diagnosis']}")
            print("")
    else:
        print("Invalid gender")