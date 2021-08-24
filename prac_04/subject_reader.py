"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_data()


def print_data():
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        print("{} is taught by {} and has {} students.".format(parts[0], parts[1], parts[2]))

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()         # Remove the \n
        parts = line.split(',')     # Separate the data into its parts
        parts[2] = int(parts[2])    # Make the number an integer (ignore PyCharm's warning)
        print(parts)                # See if that worked
    input_file.close()


main()
