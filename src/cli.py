import sys
try:
    from .calculator import add, subtract, multiply, divide, power, square_root
except ImportError:
    # fallback if running directly
    from src.calculator import add, subtract, multiply, divide, power, square_root

def main():
    if len(sys.argv) < 3:
        print("Usage: python -m src.cli <operation> <num1> [<num2>]")
        sys.exit(1)

    operation = sys.argv[1]

    try:
        if operation in ["add", "subtract", "multiply", "divide", "power"]:
            a = float(sys.argv[2])
            b = float(sys.argv[3])
            if operation == "add":
                result = add(a, b)
            elif operation == "subtract":
                result = subtract(a, b)
            elif operation == "multiply":
                result = multiply(a, b)
            elif operation == "divide":
                result = divide(a, b)
            elif operation == "power":
                result = power(a, b)

        elif operation == "sqrt":
            a = float(sys.argv[2])
            result = square_root(a)

        else:
            print("Unknown operation")
            sys.exit(1)

        # Print result as integer if it's whole, else float
        if result == int(result):
            print(int(result))
        else:
            print(result)

        sys.exit(0)

    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
