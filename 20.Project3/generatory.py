import string
import secrets

def get_password_parameters():
    while True:
        try:
            length = int(input("Password Length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer.")

    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

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
        print("You must select at least one character type.")
        return get_password_parameters()

    return length, char_pool

def generate_password(length, char_pool):
    return ''.join(secrets.choice(char_pool) for _ in range(length))

def main():
    print("\n--- Password Generator ---\n")
    length, char_pool = get_password_parameters()
    password = generate_password(length, char_pool)
    print("\nNew Password: ", password, "\n")

if __name__ == "__main__":
    main()
