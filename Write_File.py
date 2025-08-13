# Write to a File Program

# Open file in write mode ("w" creates the file if it doesn't exist)
file = open("myfile.txt", "w")

# Content to write
content = "Hello! Updated This is a sample text written to a file.\nPython file handling is easy!"

# Writing content to file
file.write(content)

# Closing the file
file.close()

print("File created and content written successfully!")
