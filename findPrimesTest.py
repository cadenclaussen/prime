import sys
import findPrimes

max = int(sys.argv[1])
primeNumbers = findPrimes.findPrimes(max)
print(len(primeNumbers))
