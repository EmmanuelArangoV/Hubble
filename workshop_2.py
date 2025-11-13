patients = [
    {
    "id": 1,
    "name" : "Juan",
    "age": 23,
    "gender": "Masculino",
    "record": ["test1","test2"]
    },
    {
    "id": 2,
    "name" : "Esteban" ,
    "age": 12,
    "gender": "Masculino",
    "record": ["test3", "test4"]
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
                    print(f"Patient {patient["name"]} was deleted")
                    break
                else: 
                    print("Deleting canceled")
                    break
        print(f"{"" if band else "not found"}")     
        print(patients)
delete_patient(patients)

def reports(patients):
    file_name = "reports.txt"

    with open(file_name, 'w') as file:    
        file.write(f"{'ID':<15}|{'Name':<15}|{'Age':<5}|{'Record':<20}\n")
        for patient in patients:
            file.write(f"{patient['id']:<15}|{patient['name']:<15}|{patient['age']:<5}|")
            for i, record in enumerate(patient['record']):
                if i == len(patient['record'])-1:
                    file.write(f"{record:>43}\n")
                else:
                    file.write(f"{record}\n")
                

reports(patients)