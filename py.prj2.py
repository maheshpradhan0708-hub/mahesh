print("***...***...***...***...***...***...***...***...***...***...***...***...")


# Project: Logic Box - Pattern Generator and Number Analyzer

while True:  # Yeh loop tab tak chalega jab tak user exit na kare
    print("-" * 50)
    print("Welcome to the Pattern Generator and Number Analyzer!\n")

    print("Select an option:")
    print("1. Right-angled Triangle")
    print("2. Pyramid")
    print("3. Left-angled Triangle")
    print("4. Analyze a Range of Numbers")
    print("5. Exit")

    # choice ko string me rakhna better hai taaki alphabets daalne par crash na ho
    choice = input("Enter your choice: ").strip()

    if choice == "5":
        print("Goodbye!")
        break  # Program se baahar nikalne ke liye

    # --- PATTERN GENERATION (Options 1, 2, 3) ---
    elif choice in ["1", "2", "3"]:
        try:
            rows = int(input("Enter the number of rows for the pattern: "))
            if rows <= 0:
                print("Error: Row count must be a positive integer.")
                break  # Assignment Rule: 'break' to stop on invalid row count
        except ValueError:
            print("Error: Invalid input! Please enter a number.")
            continue

        print("\nPattern:")

        # 1. Right-angled Triangle (Using Nested Loops)
        if choice == "1":
            for i in range(1, rows + 1):
                for j in range(1, i + 1):  # Loop ke andar loop (Nested)
                    print("*", end="")
                print()  

        # 2. Pyramid (Using Nested Loops)
        elif choice == "2":
            for i in range(1, rows + 1):
                
                for j in range(rows - i):
                    print(" ", end="")
                # Stars ke liye loop
                for k in range(2 * i - 1):
                    print("*", end="")
                print()

        # 3. Left-angled Triangle (Using Nested Loops)
        elif choice == "3":
            for i in range(1, rows + 1):
                
                for j in range(rows - i):
                    print(" ", end="")
                # Stars ke liye loop
                for k in range(i):
                    print("*", end="")
                print()

    # --- NUMBER ANALYZER (Option 4) ---
    elif choice == "4":
        try:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))

            if end < start:
                print("Error: End of range must be greater than or equal to start.\n")
                continue  # Dobara menu par bhej dega
        except ValueError:
            print("Error: Please enter valid integers.\n")
            continue

        total = 0

        for i in range(start, end + 1):
            # Assignment Rule: Demonstrating 'pass' statement
            if i == -99999:
                pass  

            if i % 2 == 0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")

            total += i

        print(f"Sum of all numbers from {start} to {end} is: {total}")

    else:
        print("Invalid Choice! Please enter a number between 1 and 5.")
    
    print()  # Output ke beech me thoda gap rakhne ke liye   






















































