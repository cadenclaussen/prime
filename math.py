# round(3.8) returns 4
# round(3.3) return 3
def round(n):
    roundn = n // 1 + 1
    if n > n // 1 and n + 0.5 < n // 1 + 1:
        roundn = n // 1
    return roundn

# floor(3.4) returns 3
def floor(n):
    floorn = n // 1
    return floorn


# ceiling(3.4) returns 4
def ceiling(n):
    floorn = n // 1 + 1
    return floorn


# modulus(10, 3) returns 1
# modulus(10, 2) returns 0
def modulus(n, x):
    floor = n // x 
    x = floor * x
    modulus = n - x
    return modulus



# factorial(5) returns 5 * 4 * 3 * 2 * 1 or 120
def factorial(n):
    i = n
    for _ in range(n):
        n = n * i
        i = i - 1
    nfactorial = n
    return nfactorial

factoraln = factorial(5)
print(factoraln)