import random

# Function to generate a password
def find_password(letters_small, letters_capital, numbers, symbols):
    # Combine lowercase and uppercase letters
    letter_combined = letters_small + letters_capital
    
    # Input validation for the number of letters in the password
    while True:
        try:
            number_letter = int(input("How many letters do you want in your password? : "))
            break
        except ValueError:
            print("Error: Please enter a number!")
            continue
    
    # Randomly select letters from the combined list
    random_letter = random.sample(letter_combined, number_letter)
    
    # Input validation for the number of numbers in the password
    while True:
        try:
            password_num = int(input("How many numbers do you want in your password? : "))
            break
        except ValueError:
            print("Error: Please enter a number!")
            continue
    
    # Randomly select numbers
    random_number = random.sample(numbers, password_num)
    
    # Input validation for the number of symbols in the password
    while True:
        try:
            symbol_num = int(input("How many symbols do you want in your password? : "))
            break
        except ValueError:
            print("Error: Please enter a number!")
            continue
    
    # Randomly select symbols
    random_symbol = random.sample(symbols, symbol_num)
    
    # Combine all elements to form the final list
    final_list = random_letter + random_number + random_symbol
    
    # Shuffle the final list to ensure randomness
    random.shuffle(final_list)
    
    # Convert the list elements to strings and join them to form the password
    password = "".join(str(i) for i in final_list)
    
    # Print the generated password
    print(f"Your password is: {password}")

# Lists of characters to choose from
letters_small = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                 "j", "k", "l", "m", "n", "o", "p", "q", "r",
                 "s", "t", "u", "v", "w", "x", "y", "z"]

letters_capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                   "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                   "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ["@", "#", "$", "%", "^", "&", "=", ":", "?", ".", "/",
            "|", "~", ">", "*", "(", ")", "<"]

# Generate the first password
find_password(letters_small, letters_capital, numbers, symbols)

# Allow the user to generate more passwords if desired
while True:
    try_again = input("Want another one? (yes/no): ")
    if try_again.lower() == "yes":
        find_password(letters_small, letters_capital, numbers, symbols)
        continue
    elif try_again.lower() == "no":
        print("Goodbye!")
        break
    else:
        print("Error: Please enter 'yes' or 'no'!")
        continue
