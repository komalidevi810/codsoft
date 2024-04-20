# Password Generator

The Password Generator is a command-line tool built using Python that generates strong and random passwords for users. It allows users to specify the desired length and complexity of the password by including various character types such as lowercase letters, uppercase letters, digits, and symbols.

## Features

- Generate passwords with a specified length (minimum 6 characters)
- Include lowercase letters (a-z)
- Include uppercase letters (A-Z)
- Include digits (0-9)
- Include symbols (e.g., !, @, #, $, %, etc.)
- User-friendly interface with prompts for password customization
- Error handling for invalid inputs

## Prerequisites

- Python 3.x installed on your system

## Usage

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to start the Password Generator:
4. Follow the prompts to specify the desired length and character types for the password:
   - Enter the desired length of the password (minimum 6).
   - Choose whether to include lowercase letters (y/n).
   - Choose whether to include uppercase letters (y/n).
   - Choose whether to include digits (y/n).
   - Choose whether to include symbols (y/n).

5. The generated password will be displayed.
6. You will be asked if you want to generate another password. Enter 'y' to continue or 'n' to exit the program.

## Error Handling

- If the entered password length is less than 6, a warning will be displayed, and you will be prompted to enter a length of at least 6 characters.
- If none of the character types (lowercase, uppercase, digits, symbols) are selected, an error message will be displayed, and you will be prompted to select at least one character type.
- If an invalid input is entered for the password length or character type choices, an error message will be displayed, and you will be prompted to enter a valid input.
