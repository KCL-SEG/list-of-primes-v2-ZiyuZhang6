"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError(f"number_of_primes={number_of_primes} should have been a positive number.")
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    count = 0
    number = 2
    while count < number_of_primes:
        if is_prime(number):
            list.append(number)
            count += 1
        number += 1
    return list
