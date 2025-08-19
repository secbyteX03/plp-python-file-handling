# A simple program demonstrating file reading, writing, and error handling
# -------------------------------
# Challenge 1: File Read & Write
# -------------------------------
print("Challenge 1: File Read & Write")

# Create a simple text file with some content
with open("sample.txt", "w") as file:
    file.write("--------------------------------------------\n")
    file.write("Hello Python!\n")
    file.write("This is line 2\n")
    file.write("Learning file handling in PLP is fun!\n")
    file.write("We can read and write files easily.\n")
    file.write("End of sample content.Bye!\n")
    file.write("--------------------------------------------\n")
print("Created sample.txt")

# Read the file and modify it
with open("sample.txt", "r") as file:
    content = file.read()
    print("Original content:")
    print(content)

# Make it uppercase and save to new file
modified_content = content.upper()

with open("modified.txt", "w") as file:
    file.write(modified_content)

print("Created modified.txt with uppercase text")


# -----------------------------
# Challenge 2: Error Handling
# -----------------------------
print("\nChallenge 2: Error Handling")

# Ask the user for a filename
filename = input("Enter a filename to read: ")

try:
    # Try to read the file
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print("Error: File not found!")

except Exception as e:
    print(f"Error: {e}")

print("Program finished!")
