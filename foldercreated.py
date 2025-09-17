import os

folder_name = input("Enter new folder name: ")
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created.")
else:
    print("Folder already exists.")
