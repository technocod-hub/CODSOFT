# Task 3 - Password Generator
# CodSoft Python Internship - Azhaan Azam

import random
import string

def generate_password(length, use_uppercase, use_digits, use_symbols):
    characters = string.ascii_lowercase  # always include lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("===== Password Generator =====")

while True:
    print("\n1. Generate Password")
    print("2. Exit")

    choice = input("\nEnter your choice (1-2): ")

    if choice == '2':
        print("Goodbye!")
        break

    elif choice == '1':
        # Get password length
        while True:
            try:
                length = int(input("Enter password length (6-32): "))
                if 6 <= length <= 32:
                    break
                else:
                    print("Please enter a length between 6 and 32!")
            except ValueError:
                print("Please enter a valid number!")

        # Get complexity options
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_uppercase, use_digits, use_symbols)

        print(f"\n✅ Your Generated Password: {password}")
        print(f"   Password Length: {len(password)}")

    else:
        print("Invalid choice! Please enter 1 or 2.")