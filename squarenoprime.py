num = int(input("Enter a number: "))
sq = num ** 2

is_prime = True
if sq < 2:
    is_prime = False
else:
    for i in range(2, int(sq ** 0.5) + 1):
        if sq % i == 0:
            is_prime = False
            break

print(f"Square of {num} is {sq}")
if is_prime:
    print("It is prime")
else:
    print("It is not prime")
