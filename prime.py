def isPrime(number):
    for primeNumber in [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37 ]:
        if primeNumber == number:
            return True
        if number % primeNumber == 0:
            return False
    return True


def getPrimeFactors(number):
    primeFactors = []
    for primeNumber in [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        while number % primeNumber == 0:
            number = number / primeNumber
            primeFactors.append(primeNumber)
    return primeFactors


number = input("Type in a number: ")
number = int(number)
isPrime = isPrime(number)
if isPrime == False:
    print(number, "is not prime")
else:
    print(number, "is prime")
factors = getPrimeFactors(number)
print(factors)
