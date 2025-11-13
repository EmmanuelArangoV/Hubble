patients = []

def print_patient(patient):
    print(f"Id: {patient.get('id')}, Name: {patient.get('name')}, "
          f"Age: {patient.get('age')}, Diagnosis: {patient.get('diagnosis')}")

    print("Record of events:")
    for event in patient.get('record', []):
        print(" - ", event)
    print("\n")

def search_by_id(value):
    found = False
    for patient in patients:
        if patient.get('id') == value:
            found = True
            print_patient(patient)

    if not found:
        print("Patient not found")

def search_by_name(value):
    found = False
    for patient in patients:
        if value in patient.get('name'):
            found = True
            print_patient(patient)
    if not found:
        print("Patients not found")

def search_by_diagnosis(value):
    found = False
    for patient in patients:
       if value == patient.get('diagnosis'):
           found = True
           print_patient(patient)
    if not found:
        print("Patients not found")