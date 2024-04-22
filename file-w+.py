# write + 
# first write then read


def write_file(filename, data) -> None:
    with open(file=filename, mode='w+') as fp:
        fp.write(data)
        # after writing the data into file the file pointer will be at the end
        # we can file the position of the pointer using tell
        print('file pointer at : {}'.format(fp.tell()))
        # we can change this pointer position to any point using seek
        fp.seek(0)
        print(fp.read())


def main():
    data = 'sample data'
    filename = './files/writeandread.txt'

    write_file(filename=filename, data=data)

if __name__ == '__main__':
    main()