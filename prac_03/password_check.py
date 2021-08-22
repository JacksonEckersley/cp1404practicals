
def main():
    char_length = 10
    while True:
        password = get_password(char_length)
        if len(password) < char_length:
            continue
        else:
            print_star(password)
            break


def get_password(char_length):
    password = input("Enter a password at least {} characters long: ".format(char_length))
    return password


def print_star(password):
    for i in range(0, len(password)):
        print("*", end="")


main()
