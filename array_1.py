from array import array

nums = list(map(int, input("Enter integers separated by space: ").split()))
arr = array('i', nums)
print("Array:", arr.tolist())
