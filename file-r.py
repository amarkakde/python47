# read a text file and show its content on console

import sys

def read_file(filename) -> None:
    fp = open(filename, 'r')
    data = fp.read()

    print(data)

def main():
    filename = sys.argv[1]
    read_file(filename) 

if __name__ == '__main__':
    main()