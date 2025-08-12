n = int(input("Enter number of terms: "))
a, b = 0, 1
i = 0

while i <= n:
    print(a)
    a, b = b, a + b
    i += 1
