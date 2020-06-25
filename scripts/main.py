import os, sys

def main():
    f = open('text.txt', 'w')

    for param in sys.argv:
        f.write(param)

    f.close()

if __name__ == "__main__":
    main()