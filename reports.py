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
        print("Diagnosis\n")
        print(f"Diagnosis: {i}, count: {diagnosis.get(i)}")

def total_patients(patients):
    print("Total patients is: ", len(patients))
