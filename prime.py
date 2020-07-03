def generatePrimes(max):
    primes = [2]
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
    primes = generatePrimes(n - 1)
    return __isPrime(n, primes)

def lcm(n1, n2):
    primeFactors1 = getPrimeFactors(n1)
    primeFactors2 = getPrimeFactors(n2)

    lcmPrimeFactors = []

    for primeFactor1 in primeFactors1:
        found = False
        for primeFactor2 in primeFactors2:
            if primeFactor2 == primeFactor1:
                lcmPrimeFactors.append(primeFactor1)
                primeFactors2.remove(primeFactor2)
                found = True
                break
        if found == False:
            lcmPrimeFactors.append(primeFactor1)

    print(lcmPrimeFactors, primeFactors1, primeFactors2)       
    lcmPrimeFactors.extend(primeFactors2)



    lcm = 1
    for lcmPrimeFactor in lcmPrimeFactors:
        lcm *= lcmPrimeFactor
        
    return lcm




def __isPrime(n, primes):
    return all(n % prime for prime in primes)
