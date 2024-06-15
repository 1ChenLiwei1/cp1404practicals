MINIMUM_LENGTH = 8


def main():
    password = get_password()
    password_length = len(password)
    while password_length < MINIMUM_LENGTH:
        password = get_password()
        password_length = len(password)
    print_password(password_length)


def print_password(password_length):
    print('*' * password_length)


def get_password():
    password = input('Enter your password: ')
    return password


main()

