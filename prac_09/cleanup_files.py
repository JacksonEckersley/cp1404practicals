import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        print(f"Directory {directory_name} contains subdirectories {subdirectories} and files {filenames}")

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))
            print(f"renaming {filename} to {new_name}")


def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    temp_name = []

    # Add underscores before capital letters
    for index, char in enumerate(new_name):
        # If a char other than the first in the filename is uppercase:
        if char.isupper() and index != 0:
            # If the char preceding and uppercase letter is not an underscore:
            if new_name[index - 1] != "_":
                temp_name.append("_")
                temp_name.append(char)
            # Otherwise just append the next char:
            else:
                temp_name.append(char)

        # Else if there is an opening bracket before the current char:
        elif new_name[index - 1] == "(":
            # Capitalize the current char
            temp_name.append(char.upper())

        # Else if there is no underscore in front of an open bracket:
        elif new_name[index] == "(":
            if new_name[index - 1] != "_":
                temp_name.append("_")
                temp_name.append(char)
            else:
                temp_name.append(char)

        # Otherwise just append the next char
        else:
            temp_name.append(char)

    # Return the fixed name
    return "".join(temp_name)


main()
