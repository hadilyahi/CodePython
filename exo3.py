def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a // gcd(a, b)) * b


A = int(input("Enter Number 1: "))
B = int(input("Enter Number 2: "))


result = lcm(A, B)


print(f"Lcm {A} and {B} is {result}")
