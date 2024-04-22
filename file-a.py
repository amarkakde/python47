# append mode


def append_data(filename, data)-> None:
    with open(file=filename, mode='a') as fp:
        fp.write(data)

def read_file(filename) -> None:
    with open(file=filename) as fp:
        print('read:',fp.read())

def main() -> None:
    data1 = 'this is 1st line.\n'
    data2 = 'this is 2nd line.\n'
    data3 = 'this is 3rd line.\n'
    data4 = 'this is 4th line.\n'
    data5 = 'this is 5th line.\n'

    filename = './files/append.txt'

    append_data(filename=filename, data=data1)
    read_file(filename=filename)
    append_data(filename=filename, data=data2)
    read_file(filename=filename)
    append_data(filename=filename, data=data3)
    read_file(filename=filename)
    append_data(filename=filename, data=data4)
    read_file(filename=filename)
    append_data(filename=filename, data=data5)
    read_file(filename=filename)

if __name__ == '__main__':
    main()