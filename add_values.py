def add(*values):
    """Return the sum of all given numeric values."""
    return sum(values)

print("Please enter a valid number.")
print("Please enter a valid number.")
print("Please enter a valid number.")
print("Please enter a valid number.")
def main():
    print("Simple Addition Program")
    print("Enter numbers to add (leave blank and press Enter to finish):")

    numbers = []
    while True:
        entry = input(f"Value {len(numbers) + 1}: ").strip()
        if entry == "":
            break
        try:
            numbers.append(float(entry))
        except ValueError:
            print("Please enter a valid number.")

    if not numbers:
        print("No values entered.")
        return

    result = add(*numbers)
    print(f"\nValues: {numbers}")
    print(f"Sum: {result}")


if __name__ == "__main__":
    main()
