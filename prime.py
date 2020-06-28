def generatePrimes(max):
    primes = [ 2 ]
    for n in range(3, max + 1):
        if (__isPrime(n, primes)):
            primes.append(n)
    return primes


def getPrimeFactors(n):
    primeFactors = []
    print()
    print("  ", n)
    spaces = 1
    for prime in generatePrimes(n):
        while n % prime == 0:
            n = n // prime
            primeFactors.append(prime)
            if (n != 1):
                print(" " * (spaces + 1), "/ ", "\\")
                print(" " * spaces, prime, "  ", n)
                spaces += len(str(prime)) + 2
    print()
    return primeFactors


def isPrime(n):
    primes = generatePrimes(n - 1);
    if (__isPrime(n, primes)):
        return True
    return False


def lcm(n1, n2):
    pass


def gcd(n1, n2):
    primeFactors1 = getPrimeFactors(n1)
    primeFactors2 = getPrimeFactors(n2)

    commonPrimeFactors = []
    for primeFactor1 in primeFactors1:
        for primeFactor2 in primeFactors2:
            if primeFactor2 == primeFactor1:
                commonPrimeFactors.append(primeFactor1)
                primeFactors2.remove(primeFactor2)
                break

    gcf = 1
    for commonPrimeFactor in commonPrimeFactors:
        gcf = gcf * commonPrimeFactor
        
    return gcf


def __isPrime(n, primes):
    for prime in primes:
        if n % prime == 0:
            return False
    return True
