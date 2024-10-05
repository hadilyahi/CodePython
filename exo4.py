def sieve_of_eratosthenes(N):
    primes = [True] * (N + 1) 
    primes[0], primes[1] = False, False  

    for i in range(2, int(N**0.5) + 1):
        if primes[i]:
            for j in range(i * i, N + 1, i):
                primes[j] = False


    return [i for i in range(2, N + 1) if primes[i]]

N = int(input("Enter the value of N: "))


if 1 <= N <= 10**6:
    prime_numbers = sieve_of_eratosthenes(N)
    print(f"Prime numbers less than or equal to {N}:")
    print(prime_numbers)
else:
    print("Please enter a number between 1 and 10^6.")
