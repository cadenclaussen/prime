def isPrime(number):
    for primeNumber in [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37 ]:
        if number % primeNumber == 0:
            return False
    return True


def getPrimeFactors(number):
    for primeNumber in [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37 ]:
        if number % primeNumber == 0:
            return False
    return True
            

number = input("Type in a number: ")
number = int(number)
isPrime = isPrime(number)
if isPrime == False:
    print(number, "is not prime")
else:
    print(number, "is prime")