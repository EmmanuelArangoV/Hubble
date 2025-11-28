from typing import Optional

# Color constants
COLOR_RESET = '\033[0m'
COLORS = {
    'info': '\033[38;5;153m',      # Pastel sky blue
    'success': '\033[38;5;151m',   # Pastel green
    'error': '\033[38;5;210m',     # Pastel salmon
    'warning': '\033[38;5;221m',   # Pastel yellow
    'prompt': '\033[38;5;216m'     # Pastel peach
}

def ctext(text: str, kind: str = 'info') -> str:
    return f"{COLORS.get(kind, '')}{text}{COLOR_RESET}" if COLORS.get(kind) else text

"""Validations for yes/no answers"""
def parse_answer(value) -> Optional[bool]:
    yes = ['yes', 'y', 'si', 'sí', 's']
    no = ['no', 'n']

    value = value.strip().lower()

    if value in yes:
        return True
    elif value in no:
        return False
    else:
        return None

"""Validations for strings"""
def non_empty_string(value: str) -> bool:
    return bool(value and value.strip())

def clear_string(value: str) -> str:
    return value.strip()

def only_letters_string(value: str) -> bool:
    return value.isalpha()

def valid_string(value) -> str:
    value = clear_string(value)
    if not non_empty_string(value):
        raise ValueError("Name cannot be empty")
    elif not only_letters_string(value):
        raise ValueError("Name should contain only letters")
    else:
        return value

"""Validations for positive integers and floats"""

def parse_positive_int(value: str) -> int:
    value = clear_string(value)
    try:
        n = int(value)
    except Exception:
        raise ValueError("Value should be an integer")

    if n <= 0:
        raise ValueError("Value should be greater than zero")

    return n

def parse_positive_float(value: str) -> float:
    value = clear_string(value)
    try:
        value = replace_float(value)
        f = float(value)
    except Exception:
        raise ValueError("Value should be a float number")
    if f <= 0:
        raise ValueError("Value should be greater than zero")

    return f

def replace_float(value: str) -> str:
    new_value = value.replace(',', '.')
    return new_value
