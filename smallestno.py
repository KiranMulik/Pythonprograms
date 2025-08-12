n = int(input("Enter how many numbers: "))
count = 1
smallest = float(input(f"Enter number {count}: "))

while count < n:
    num = float(input(f"Enter number {count+1}: "))
    if num < smallest:
        smallest = num
    count += 1

print("Smallest number is:", smallest)
