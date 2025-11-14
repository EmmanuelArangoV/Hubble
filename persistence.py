import json
from typing import List, Dict, Any

def save_patients(path: str, patients: List[Dict[str, Any]]) -> None:
    # Save the list of patients to a JSON file
    with open(path, mode='w', encoding="utf-8") as clinic:
        json.dump(patients, clinic, indent=4, ensure_ascii=False)

def load_patients (path: str) -> List[Dict[str, Any]]:
    try:
        with open(path, "r", encoding="utf-8") as clinic:
            patients = json.load(clinic)
            return patients if isinstance(patients, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Empty or invalid JSON file. Initializing with an empty list.")
        with open(path, "w") as clinic:
            json.dump([], clinic)
        return []
