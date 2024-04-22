# read+ 
# first read then write


def read_file(filename, data) -> None:
    with open(file=filename, mode='r+') as fp:
        print(fp.read())

        fp.write(data)

def main():
    data = 'sample data'
    filename = './files/readandwrite.txt'

    read_file(filename=filename, data=data)

if __name__ == '__main__':
    main()