from sys import argv


def cat(filename):
    f = open(filename, "r")
    content = f.read()
    print(content)
    f.close()


def main():
    for i in range(1, len(argv)):
        cat(argv[i])


if __name__ == '__main__':
    main()
