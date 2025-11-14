def delete_patient(patients):
    band_patient_id = False
    while band_patient_id == False:
        band = False
        try:
            patient_id = input("Type a patient ID to delete: ")
            if patient_id == "":
                raise ValueError
        except ValueError:
            print("Type a valid ID")
        for i,patient in enumerate(patients):
            if  patient_id == patient.get("id") :
                band = True
                band_patient_id = True
                confirm = input(f"You will eliminate the patient {patient["name"]}. Are you sure? Yes/No: ").lower()
                if confirm == "yes":
                    patients.pop(i)
                    print(f"Patient {patient["name"]} was deleted")
                    break
                else:
                    print("Deleting canceled")
                    break
        print(f"{"" if band else "Not found"}")

