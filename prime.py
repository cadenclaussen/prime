def main():
    primes = [ 2 ]
    for number in range(3, 500000):
        # if (number % 10000 == 0):
        #     print(number, len(primes)) 
        if (isPrime(number, primes)):
            primes.append(number)
    print()
    print(len(primes)) 

def isPrime(number, primes):
    for prime in primes:
        if number % prime == 0:
            return False
    return True

main()