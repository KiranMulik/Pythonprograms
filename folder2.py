import os

path = input("Enter folder path (or . for current): ")
if os.path.exists(path):
    print("Files and folders in", path)
    print(os.listdir(path))
else:
    print("Path doesn't exist.")
