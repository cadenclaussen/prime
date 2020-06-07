import sys
import prime


# Get the number to test
n = int(sys.argv[1])


# Get prime numbers up to the number
primes = prime.generatePrimes(n)
print(primes)
print(len(primes))
print()


# Determine whether the number is prime
isPrime = prime.isPrime(n)
print(n, " isPrime: ", isPrime)
print()


# Get the number's prime factors
primeFactors = prime.getPrimeFactors(n)
print("Prime factors:", primeFactors)
