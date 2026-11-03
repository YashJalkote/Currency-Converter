
def currency_converter():

    print("\n================================")
    print("       CURRENCY CONVERTER")
    print("================================")

    print("1. INR to USD")
    print("2. USD to INR")
    print("3. INR to EUR")
    print("4. EUR to INR")
    print("5. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 5:
                print("Thank you for using Currency Converter!")
                break

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice! Please select 1 to 5.")
                continue

            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Please enter an amount greater than zero.")
                continue

            if choice == 1:
                result = amount / 88
                print(f"Converted Amount: {result:.2f} USD")

            elif choice == 2:
                result = amount * 88
                print(f"Converted Amount: {result:.2f} INR")

            elif choice == 3:
                result = amount / 102
                print(f"Converted Amount: {result:.2f} EUR")

            elif choice == 4:
                result = amount * 102
                print(f"Converted Amount: {result:.2f} INR")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


currency_converter()
