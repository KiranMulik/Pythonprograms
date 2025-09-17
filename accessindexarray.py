from array import array

arr = array('i', [10, 20, 30, 40, 50])
index = int(input("Enter index to access: "))
if 0 <= index < len(arr):
    print("Element at index", index, "is", arr[index])
else:
    print("Invalid index.")
