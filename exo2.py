def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("Enter Number 1 :  "))
num2 = int(input("Enter Number 2 :  "))


result = gcd(num1, num2)

print(f"PGCd {num1} and {num2} is {result}")
