with open("file2.txt", "a") as f:
    line = input("Enter a line to append: ")
    f.write(line + "\n")

with open("file2.txt", "r") as f:
    print("All lines:")
    print(f.read())
