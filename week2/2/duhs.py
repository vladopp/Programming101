import sys
import os


def main():
    script, path = sys.argv
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    print(total_size/10**3)

if __name__ == '__main__':
    main()
