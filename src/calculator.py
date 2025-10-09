"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""


def add(a, b):
    """Add two numbers together"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b


def multiply(a, b):
    """Multiply two numbers with input validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a, b):
    """Divide a by b with input validation and zero-division check."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


def power(a, b):
    """Raise a to the power of b"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a**b


def square_root(a):
    """Calculate square root of a"""
    if not isinstance(a, (int, float)):
        raise TypeError("Argument must be a number")
    if a < 0:
        raise ValueError("Cannotcalculate square root of negative")
    return a**0.5


if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"3 × 4 = {multiply(3, 4)}")
    print(f"10 ÷ 2 = {divide(10, 2)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    print(f"√16 = {square_root(16)}")
