import math

def prime_number(N):
    is_prime = True
    if N <= 1:
        is_prime = False
    else:
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                is_prime = False
                break
    
    if is_prime:
        print(f"{N} is a prime number")
    else:
        print(f"{N} is not a prime number")

N = int(input("Enter an integer number: "))

if 1 < N < 1000000:
    prime_number(N)
else:
    print(f"{N} is not a correct number")
