from register_patient import register_patients
from update_patient import update_patient
from delete_patient import delete_patient
from search_patients import search_by_id, search_by_name, search_by_diagnosis
from reports import reports, all_patient, older_sixty, diagnosis, total_patients
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
                "8. Exit\n")

report_options = (""
                  "1. List all patients\n"
                  "2. List patients older than sixty\n"
                  "3. Count by diagnosis\n"
                  "4. Total number of patients\n"
                  "5. Import in txt file\n"
                  "6. Back to main menu\n")



if __name__ == "__main__":
    while True:
        print("Welcome to the Clinic Management System")
        choice = input(menu_options)
        if choice == '1':
            register_patients()

