import re

def validate_string(value, field_name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string.")
    return value.strip()

def validate_integer(value, field_name):
    try:
        return int(value)
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be an integer.")

def validate_float(value, field_name):
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a number.")

