def all_patient(patients):
    print("List of patients")
    flag = False
    for i in patients:
        print(f"ID: {i.get("id")}, name: {i.get("name")}, age: {i.get("age")}")
        flag = True
    if not flag:
        print("There are no users")

def older_sixty(patients):
    print("list of patients older than sixty")

    flag = False
    for i in patients:
        if i.get('age') > 60:
            print(f"ID: {i.get("id")}, name: {i.get("name")}, age: {i.get("age")}")
            flag = True
    if not flag:
        print("There are no users older than sixty")

def diagnosis(patients):

    diagnosis = {}

    for i in patients:
        patient_diagnosis = i.get("diagnosis")
        if  patient_diagnosis in diagnosis:
            diagnosis[patient_diagnosis] += 1
        else:
            diagnosis[patient_diagnosis] = 1
    for i in list(diagnosis.keys()):
        print(f"Diagnosis: {i}, count: {diagnosis.get(i)}")

def total_patients(patients):
    print("Total patients is: ", len(patients))


def reports(patients, path):
    with open(path, 'w') as file:
        file.write(f"{'ID':<15}{'|Name':<25}{'|Age':<5}{'|Diagnosis':<50}{'|Record':<20}\n")
        for patient in patients:
            file.write("_____________________________________________________________________________________________________________________________________________________________\n")
            file.write(f"{patient['id']:<15}|{patient['name']:<25}|{patient['age']:<5}|{patient['diagnosis']:<50}|")
            for i, record in enumerate(patient['record']):
                if i == len(patient['record'])-1:
                    file.write(f"{record:>103}\n")
                else:
                    file.write(f"{record}\n")

