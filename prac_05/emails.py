
def main():
    email_list = {}
    email_in = input("Email: ")

    while email_in != "":
        name = get_name(email_in)
        confirmation = input("Is your name {}? (Y/n) ".format(name))

        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_list[email_in] = name

        email_in = input("Email: ")

    for email_in, name in email_list.items():
        print("{} ({})".format(name, email_in))


def get_name(email_in):
    name_1 = email_in.split('@')[0]
    name_2 = name_1.split('.')
    name = " ".join(name_2).title()
    return name


main()

