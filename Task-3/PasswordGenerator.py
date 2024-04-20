import random
import string

def generate_password(length, include_lowercase=True, include_uppercase=True, include_digits=True, include_symbols=True):

    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = "".join(random.sample(characters, length))
    return password

def get_password_length():
    while True:
        length = input("Enter the desired length of the password (minimum 6): ")
        if length.isdigit():
            length = int(length)
            if length < 6:
                print("Warning: Password length should be at least 6 characters for better security.")
                continue
            return length
        print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Password Generator!")

    while True:
        length = get_password_length()

        include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
        include_digits = input("Include digits? (y/n): ").lower() == "y"
        include_symbols = input("Include symbols? (y/n): ").lower() == "y"

        try:
            password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols)
            print(f"\nThe generated password is: {password}")
        except ValueError as e:
            print(f"Error: {e}")

        choice = input("\nDo you want to generate another password? (y/n): ").lower()
        if choice != "y":
            break

    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()