try:
    filename = input("Enter filename to open: ")
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
