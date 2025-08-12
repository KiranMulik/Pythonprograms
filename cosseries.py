x = float(input("Enter x in radians: "))
n = int(input("Enter the maximum power (even number): "))

sum_cos = 1
sign = -1
fact = 1

for i in range(2, n+1, 2):
    fact *= i * (i - 1)   # factorial update for even terms
    sum_cos += sign * (x ** i) / fact
    sign *= -1

print("cos(x) =", sum_cos)
