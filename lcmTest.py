import sys
import prime

def main():
    if (len(sys.argv) != 3):
        print('usage: lcmTest number1 number2>')
        sys.exit(1)
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    lcm = prime.lcm(n1, n2)
    print(lcm)

main()