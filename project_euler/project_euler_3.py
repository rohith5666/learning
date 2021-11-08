# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# This function computes the prime factor's of input number
import math
n= int(input("Enter Number:"))
def Largest_Prime_Factor(n):
    prime_factor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1

    if prime_factor < n:
        prime_factor = n

    return prime_factor

# Printing the largest prime factor of input number
print ("Largest prime factor of",n, "is", Largest_Prime_Factor(n))