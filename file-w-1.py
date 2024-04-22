from pathlib import Path

def write_file(filename, data):
    with open(file=filename, mode='w') as fp:
        fp.write(data)

def write_lines(filename, data: list[str]) -> None:
    with open(file=filename, mode='w') as fp:
        fp.writelines(data)

def main():
    filename = './files/4.txt'
    data = 'aijda ajdja aijda djadajd ajda djaod'
    data2 = ['this is 1st line.\n', 'this is 2nd line.\n']

    write_lines(filename=filename, data=data2)

if __name__ == '__main__':
    main()
