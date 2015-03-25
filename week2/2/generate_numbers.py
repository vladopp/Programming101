from sys import argv
from random import randint


def main():
    script, filename, n = argv
    f = open(filename, 'w')
    n = int(n)
    while n:
        f.write(str(randint(0, 999)))
        f.write(" ")
        n -= 1


if __name__ == '__main__':
    main()
