import sys
import primeFactors

# Get the number to test
number = int(sys.argv[1])

# Get the number's prime factors
primeFactors = primeFactors.getPrimeFactors(number)
print("Prime factors:", primeFactors)
