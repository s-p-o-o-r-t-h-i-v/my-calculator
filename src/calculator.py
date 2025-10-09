"""
Calculator Module - Basic arithmetic operations
Extended with power and square-root functionality
"""

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b

def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")  # Matches integration test
    return a / b

def power(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a**b

def square_root(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Argument must be a number")
    if a < 0:
        raise ValueError("Cannot calculate square root of negative")
    return a**0.5

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"3 × 4 = {multiply(3, 4)}")
    print(f"10 ÷ 2 = {divide(10, 2)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    print(f"√16 = {square_root(16)}")
