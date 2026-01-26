def get_positive_number():

    while True:
        user_input = input("Please enter a positive number: ")
        try:
            number = float(user_input) 
            if number > 0:
                return number
            else:
                print("Error: The number must be greater than zero. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value. Please try again.")

if __name__ == "__main__":
    positive_num = get_positive_number()
    print(f"You entered a valid positive number: {positive_num}")