def check_registration(registration: dict) -> str:
    """
    Check if a person is registered and eligible based on age.
    Returns a message string.
    """
    if registration.get("is_registered") and registration.get("age", 0) >= 20:
        return f'{registration.get("name")} is registered already'
    else:
        return f'{registration.get("name")} is not registered'


# Example usage
registration = {
    "name": "kcee",
    "lga": "umuahia",
    "age": 28,
    "is_registered": True
}

print(check_registration(registration))
