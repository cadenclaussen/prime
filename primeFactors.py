import findPrimes


def getPrimeFactors(number):
    primeFactors = []
    print()
    print("  ", number)
    spaces = 1
    for primeNumber in findPrimes.findPrimes(number):
        while number % primeNumber == 0:
            number = number // primeNumber
            primeFactors.append(primeNumber)
            if (number != 1):
                print(" " * (spaces + 1), "/ ", "\\")
                print(" " * spaces, primeNumber, "  ", number)
                spaces += len(str(primeNumber)) + 2
    print()
    return primeFactors
