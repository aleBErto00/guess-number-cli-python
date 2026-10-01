import re # Regular expression module for input validation
import time # Time module for adding delays in the game


# Function to process the operation input by the user
def process_operation(current_number, operation):
    try:
        match = re.match(r"([+\-*/])\s*(-?\d+\.?\d*)", operation) # Validates the input with and without spaces
        if not match:
            print("Invalid input format. Use operation number.")
            return current_number

        op = match.group(1)
        num_str = match.group(2)
        num = float(num_str)
        match op:
            case '+':
                return current_number + num
            case '-':
                return current_number - num
            case '*':
                return current_number * num
            case '/':
                if num == 0:
                    print("Cannot divide by zero.")
                    return current_number
                return current_number / num
            case _:
                print("Invalid operation. Use +, -, *, or /.")
                return current_number
    except ValueError:
        print("Invalid input format. Use operation number.")
        return current_number

# Function to provide hints based on the difference between the guess and the target
def process_hint(guess, target, attempts):
    difference = abs(guess - target)
    print (f"Your actual number is {guess}...") # Log message to make easier to remember the current number
    match difference:
        case _ if difference == 0:
            print(f"Congratulations! You've guessed the number {target} in {attempts} attempts.")
            return 1
        case _ if difference <= 10:
            print("Blazing hot!")
        case _ if difference <= 50:
            print("Hot")
        case _ if difference <= 100:
            print("Warm")
        case _ if difference >= 400:
            print("Cold")
        case _ if difference >= 500:
            print("Icy")
        case _ if difference >= 600:
            print("Freezing!")
    return 0