def write_file(filename, data) -> None:
    fp = open(file=filename, mode='w')
    fp.write(data)

def main() -> None:
    data = '1st line to write to file'
    filename = './files/2.txt'

    write_file(filename, data)

if __name__ == '__main__':
    main()