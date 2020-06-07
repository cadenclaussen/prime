def findPrimes(max):
    primes = [ 2 ]
    for n in range(3, max + 1):
        if (isPrime(n, primes)):
            primes.append(n)
    return primes



def isPrime(n, primes):
    for prime in primes:
        if n % prime == 0:
            return False
    return True
