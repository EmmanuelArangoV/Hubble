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
    band_patient_id = False
    while band_patient_id == False:
        band = False
        try:
            patient_id = int(input("Type a patient ID to delete: "))
        except ValueError:
            print("Type a valid ID")

        for i,patient in enumerate(patients):
            if  patient_id == patient.get("id") :
                band = True
                band_patient_id = True
                confirm = input(f"You will eliminate the patient {patient["name"]}. Are you sure? Yes/No: ").lower()
                if confirm == "yes":
                    patients.pop(1)
                    print(f"Patient {patient["name"]} deleted")
                    break
                else: 
                    print("Deleting canceled")
                    break

        print(f"{"" if band else "not found"}")     
        print(patients)

delete_patient(patients)