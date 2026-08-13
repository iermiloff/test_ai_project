def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return round(a / b, 2)
