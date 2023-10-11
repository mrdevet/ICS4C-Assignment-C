# Programmer: 
# Description: 

# Ask the user for the file name and open that file
ranges_file_name = input("What file contains the ranges? ")
print()
ranges_file = open(ranges_file_name, "r")

# Read each line from the file and pick a random value in the given range
for line in ranges_file:
    pass  # Replace "pass" with your code

# Close the file
ranges_file.close()
