"""
Command Line Interface for Calculator
Example: python -m src.cli add 5 3
"""

import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root

def format_result(value):
    """Convert floats like 8.0 to 8 for cleaner CLI output."""
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation in ("square_root", "sqrt"):
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        result = format_result(result)
        click.echo(result)

    except Exception as e:
        click.echo(str(e))
        sys.exit(1)

if __name__ == "__main__":
    calculate()
