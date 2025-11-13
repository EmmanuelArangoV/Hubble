

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

def diagnostic(patients):

    diagnostics = {}

    for i in patients:
        patient_diagnostic = i.get("diagnostic")
        if  patient_diagnostic in diagnostics:
            diagnostics[patient_diagnostic] += 1
        else:
            diagnostics[patient_diagnostic] = 1
    for i in list(diagnostics.keys()):
        print("Diagnostic\n")
        print(f"Diagnostic: {i}, count: {diagnostics.get(i)}")

def total_patients(patients):
    print("Total patients is: ", len(patients))
