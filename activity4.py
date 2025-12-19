# Custom Exception
class EmptyListError(Exception):
    pass


# Function to display the list
def display_list(numbers):
    print("\n----------------------------------------")
    print("Number List:")
    print(numbers)
    print("----------------------------------------")


# Input number of elements
while True:
    try:
        n = int(input("Enter number of elements: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input! Please enter a positive integer.")

# Store numbers
numbers = []
i = 1
while i <= n:
    try:
        value = float(input(f"Enter number {i}: "))
        numbers.append(value)
        i += 1
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Main program loop
while True:
    try:
        if len(numbers) == 0:
            raise EmptyListError("Error: The list is empty!")

        display_list(numbers)

        print("Choose an action:")
        print("1 - Calculate sum and average")
        print("2 - Divide two numbers")
        print("3 - Access element by index")
        print("4 - Add a new number")

        choice = int(input("Enter your choice: "))

        # Option 1: Sum and Average
        if choice == 1:
            total = sum(numbers)
            avg = total / len(numbers)
            print(f"Sum: {total}")
            print(f"Average: {avg}")

        # Option 2: Division using indices
        elif choice == 2:
            num_index = int(input("Enter index of numerator: "))
            den_index = int(input("Enter index of denominator: "))
            result = numbers[num_index] / numbers[den_index]
            print("Result:", result)

        # Option 3: Access element
        elif choice == 3:
            index = int(input("Enter index to access: "))
            print("Value:", numbers[index])

        # Option 4: Add new number
        elif choice == 4:
            new_num = float(input("Enter new number: "))
            numbers.append(new_num)
            print("Number added successfully!")

        else:
            print("Invalid menu choice!")

    except ValueError:
        print("Error: Invalid input!")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except IndexError:
        print("Error: Index out of range!")
    except EmptyListError as e:
        print(e)
    finally:
        print("\n----------------------------------------")
        cont = input("Do you want to continue? (yes/no): ").lower()
        if cont != "yes":
            print("\nProgram terminated!")
            break
