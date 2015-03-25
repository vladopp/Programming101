from sys import argv


def main():
    scrypt, filename = argv
    f = open(filename)
    content = f.read()
    print(sum([int(x) for x in content.split(" ") if x != '\n']))


if __name__ == '__main__':
    main()
