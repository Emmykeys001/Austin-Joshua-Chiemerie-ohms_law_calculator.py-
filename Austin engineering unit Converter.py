
# OHM'S LAW AND POWER CALCULATOR
# CTE123 Python Mini Project

calculation_history = []


# Function to collect valid numbers.
def get_number(message, allow_zero=True):
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Negative values are not allowed.")
            elif not allow_zero and value == 0:
                print("Value cannot be zero.")
            else:
                return value

        except ValueError:
            print("Invalid input. Enter a number.")


# Function to display the menu.
def show_menu():
    print("\n===== OHM'S LAW CALCULATOR =====")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")
    print("5. View Calculation History")
    print("0. Exit")


# Function to perform calculations.
def calculate(choice):

    if choice == 1:
        current = get_number("Enter current (A): ")
        resistance = get_number("Enter resistance (Ohms): ", False)

        voltage = current * resistance
        power = voltage * current

    elif choice == 2:
        voltage = get_number("Enter voltage (V): ")
        resistance = get_number("Enter resistance (Ohms): ", False)

        current = voltage / resistance
        power = voltage * current

    elif choice == 3:
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ", False)

        resistance = voltage / current
        power = voltage * current

    elif choice == 4:
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ")

        power = voltage * current

        if current == 0:
            resistance = None
        else:
            resistance = voltage / current

    # Display the calculated result.
    print("\n===== CALCULATION RESULT =====")

    if choice == 1:
        print(f"Voltage = {voltage:.2f} V")
    elif choice == 2:
        print(f"Current = {current:.2f} A")
    elif choice == 3:
        print(f"Resistance = {resistance:.2f} Ohms")
    elif choice == 4:
        print(f"Power = {power:.2f} W")

    # Feature 1: Power status classification.
    print("\nEnter the maximum power limit for your circuit.")
    power_limit = get_number("Power limit (W): ", False)

    if power > power_limit:
        status = "HIGH POWER - WARNING"
    elif power >= power_limit * 0.5:
        status = "MODERATE POWER"
    else:
        status = "LOW POWER"

    print("Power Status:", status)

    # Feature 2: Save calculation history.
    record = (
        f"Voltage: {voltage:.2f}V | "
        f"Current: {current:.2f}A | "
        f"Power: {power:.2f}W | "
        f"Status: {status}"
    )

    calculation_history.append(record)


# Main program.
def main():

    while True:
        show_menu()

        try:
            choice = int(input("Choose an option: "))

            if choice == 0:
                print("Thank you for using the calculator.")
                break

            elif choice in [1, 2, 3, 4]:
                calculate(choice)

            elif choice == 5:
                print("\n===== CALCULATION HISTORY =====")

                if not calculation_history:
                    print("No calculations available.")
                else:
                    for record in calculation_history:
                        print(record)

            else:
                print("Invalid option. Choose between 0 and 5.")

        except ValueError:
            print("Please enter a valid menu number.")


if __name__ == "__main__":
    main()
  
