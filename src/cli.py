"""
Command Line Interface for Calculator
Example: python -m src.cli add 5 3
"""

import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root
# If cli.py is inside src/, you can also use:
# from .calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""
    try:
        # Normalize operation (optional, just in case user types uppercase)
        operation = operation.lower()

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
            click.echo("Unknown operation")
            sys.exit(1)  # Test expects exit code 1

        click.echo(result)
        sys.exit(0)  # Success

    except ZeroDivisionError:
        click.echo("Cannot divide by zero")
        sys.exit(1)

    except Exception as e:
        # Any other calculator-related error
        click.echo(str(e))
        sys.exit(1)


if __name__ == "__main__":
    calculate()
