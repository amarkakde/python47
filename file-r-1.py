import sys

def read_file(filename):
    with open(file=filename) as fp:
        data = fp.read()
    print(data)

def read_line(filename):
    with open(file=filename) as fp:
        data = fp.readline()
        data = fp.readline()
    print(data)

def read_lines(filename):
    with open(filename) as fp:
        data = fp.readlines()
        print(type(data))
        print(data)

def main():
    filename = sys.argv[1]
    with open(file=filename) as fp:
        print(fp.readable())

    read_lines(filename)

if __name__=='__main__':
    main()