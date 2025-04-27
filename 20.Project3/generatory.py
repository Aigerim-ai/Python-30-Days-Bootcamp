import string
import secrets

def yes_or_no(prompt):
    return input(prompt).strip().lower() == 'y'

def get_password_parameters():
    while True:
        length_input = input("Password Length: ")
        if length_input.isdigit() and int(length_input) > 0:
            length = int(length_input)
            break
        else:
            print("Please enter a positive integer.")

    include_upper = yes_or_no("Include uppercase letters? (y/n): ")
    include_lower = yes_or_no("Include lowercase letters? (y/n): ")
    include_numbers = yes_or_no("Include numbers? (y/n): ")
    include_symbols = yes_or_no("Include symbols? (y/n): ")

    char_pool = ""
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_numbers:
        char_pool += string.digits
    if include_symbols:
        char_pool += "`~!@#:;,./|$%^&*)(_-=+"

    if not char_pool:
        print("You must select at least one character type.\n")
        return get_password_parameters()

    return length, char_pool

def generate_password(length, char_pool):
    password = ""
    for _ in range(length):
        password += secrets.choice(char_pool)
    return password
def main():
    print("\n--- Password Generator ---\n")
    length, char_pool = get_password_parameters()
    password = generate_password(length, char_pool)
    print("\nNew Password: ", password, "\n")

if __name__ == "__main__":
    main()
