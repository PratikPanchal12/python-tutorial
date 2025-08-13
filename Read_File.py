# Read from a File Program

# Open file in read mode ("r")
file = open("myfile.txt", "r")

# Read entire content of the file
content = file.read()

# Close the file
file.close()

# Display content
print("File Content:\n")
print(content)
