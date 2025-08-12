n = int(input("Enter how many numbers: "))
count = 1
largest = float(input(f"Enter number {count}: "))

while count < n:
    num = float(input(f"Enter number {count+1}: "))
    if num > largest:
        largest = num
    count += 1

print("Largest number is:", largest)
