"""A small command-line calculator."""


def add(left: float, right: float) -> float:
    return left + right


def subtract(left: float, right: float) -> float:
    return left - right


def multiply(left: float, right: float) -> float:
    return left * right


def divide(left: float, right: float) -> float:
    if right == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return left / right


def calculate(operation: str, left: float, right: float) -> float:
    """Apply one of the supported arithmetic operations."""
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    try:
        function = operations[operation]
    except KeyError as exc:
        raise ValueError(f"Unsupported operation: {operation}") from exc
    return function(left, right)


def read_number(prompt: str) -> float:
    """Read a number from the terminal, reporting invalid input clearly."""
    value = input(prompt)
    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"Please enter a valid number, got {value!r}.") from exc


def main() -> None:
    """Run the interactive calculator."""
    print("Python Calculator")
    print("Operations: +  -  *  / (enter q to quit)")

    while True:
        operation = input("\nOperation: ").strip()
        if operation.lower() == "q":
            print("Goodbye!")
            return

        try:
            left = read_number("First number: ")
            right = read_number("Second number: ")
            result = calculate(operation, left, right)
        except (ValueError, ZeroDivisionError) as exc:
            print(f"Error: {exc}")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    main()