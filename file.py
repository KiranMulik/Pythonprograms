text = input("Enter text to write to file: ")

with open("file1.txt", "w") as f:
    f.write(text)

with open("file1.txt", "r") as f:
    print("File contains:", f.read())
