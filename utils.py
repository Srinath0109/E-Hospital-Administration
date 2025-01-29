def validate_patient_data(data):
    """Validates patient registration data."""
    required_fields = ["name", "age", "disease"]
    for field in required_fields:
        if field not in data:
            return False
    return True
