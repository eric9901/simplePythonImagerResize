import sys
import resizer
from os import listdir
from os.path import isfile, join,isdir
if __name__ == '__main__':
    path=sys.argv[1]
    try:
        if isdir(path):
            for f in listdir(path):
                if isfile(join(path, f)):
                    resizer.resize('tg',join(path, f))
        elif isfile(path):
            resizer.resize('tg',path)
        else:
            print("please input correct folder or file path")
    except IOError:
        print("file not found")