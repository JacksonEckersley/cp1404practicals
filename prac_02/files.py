# Get the user's name and write it to a file
NAME_FILE = "user_name.txt"
name_write = input("Enter your name: ")
out_file = open(NAME_FILE, 'w')
print(f"{name_write}", file=out_file)
out_file.close()

# Read the user's name from a file and print it
in_file = open(NAME_FILE, 'r')
name_read = in_file.read()
print(f"Your name is {name_read}")
out_file.close()

# Read the first two numbers from 'numbers.txt' and add them
in_file = open("numbers.txt", 'r')
number_one = int(in_file.readline())
number_two = int(in_file.readline())
number_sum = number_one + number_two
print(number_sum)
in_file.close()
# Read all numbers from the file 'numbers.txt' and print the sum
in_file = open("numbers.txt", 'r')

number_one = int(in_file.readline())
number_two = int(in_file.readline())
number_sum = number_one + number_two
print(number_sum)
in_file.close()
