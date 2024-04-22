# eXclusive mode
# in x mode file is first created then written 
# if file present it will throw an FileExist Error

def write_file(filename, data) -> None:
    with open(file=filename, mode='x') as fp:
        fp.write(data)

if __name__=='__main__':
    data= 'aidjaaoka a akdak akpda d'
    filename = './files/exclusive.txt'
    write_file(filename=filename, data=data)