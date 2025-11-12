patients = [
    {
    "id": 1,
    "name" : "Juan" 
    },
    {
    "id": 2,
    "name" : "Esteban" 
    },

]

def delete_patient(patients):
    try:
        patient_id = int(input("Type a patient ID to delete: "))
    except ValueError:
        print("Type a valid ID")

    for i,patient in enumerate(patients):
        if patient.get("id", "This patient does not exist") == patient_id:
            print(patient , i)
            print(f"Patient {patient["name"]} deleted")

delete_patient(patients)