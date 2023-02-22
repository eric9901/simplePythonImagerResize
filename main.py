import resizer
from os import listdir
from os.path import isfile, join,isdir
if __name__ == '__main__':
    path="Input"
    try:
        for f in listdir(path):
            print(f)
            if isfile(join(path, f)):
                print(join(path, f))
                resizer.resize('tg',join(path, f))
    except IOError:
        print("file not found")
    print("Finish") 
    