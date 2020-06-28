import sys
import prime

def main():
    if (len(sys.argv) != 3):
        print('usage: gcfTest number1 number2')
        sys.exit(1)
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    gcf = prime.gcd(n1, n2)
    print(gcf)

main()