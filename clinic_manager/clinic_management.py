from register_patient import register_patients
from update_patient import update_patient
from delete_patient import delete_patient
from search_patients import search_by_id, search_by_name, search_by_diagnosis, filter
from reports import reports, all_patient, older_sixty, diagnosis, total_patients, single_diagnosis
from persistence import save_patients, load_patients
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
json_path = BASE_DIR / 'patients.json'
txt_path = BASE_DIR / 'reports.txt'

patients = load_patients(json_path)

menu_options = (""
                "1. Register Patient\n"
                "2. Update Patient\n"
                "3. Delete Patient\n"
                "4. Search patient by ID\n"
                "5. Search patient by Name\n"
                "6. Search patient by Diagnosis\n"
                "7. Generate Reports\n"
                "8. Filter Patients by Gender\n"
                "9. Exit\n")

report_options = (""
                  "1. List all patients\n"
                  "2. List patients older than sixty\n"
                  "3. Count by diagnosis\n"
                  "4. Total number of patients\n"
                  "5. Import in txt file\n"
                  "6. Single Diagnosis\n"
                  "7. Back to main menu\n")



if __name__ == "__main__":
    while True:
        print("Welcome to the Clinic Management System")
        choice = input(menu_options)
        if choice == '1':
            register_patients(patients)
            save_patients(json_path, patients)
        elif choice == '2':
            update_patient(patients)
            save_patients(json_path, patients)
        elif choice == '3':
            delete_patient(patients)
            save_patients(json_path, patients)
        elif choice == '4':
            patient_id = input("Enter patient ID to search: ")
            search_by_id(patients, patient_id)
        elif choice == '5':
            name = input("Enter patient Name to search or part of it: ")
            search_by_name(patients, name)
        elif choice == '6':
            diagnosis = input("Enter Diagnosis to search: ")
            search_by_diagnosis(patients, diagnosis)
        elif choice == '7':
            while True:
                print("What report do you want to generate?")
                subchoice = input(report_options)
                if subchoice == '1':
                    all_patient(patients)
                elif subchoice == '2':
                    older_sixty(patients)
                elif subchoice == '3':
                    diagnosis(patients)
                elif subchoice == '4':
                    total_patients(patients)
                elif subchoice == '5':
                    reports(patients, txt_path)
                    print(f"Report saved to {txt_path}")
                elif subchoice == '6':
                    single_diagnosis(patients)
                elif subchoice == '7':
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == '8':
                filter(patients)
        elif choice == '9':
            print("Exiting the Clinic Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")