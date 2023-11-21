import os
import pathlib

import pywolf.utils.fileutils as f;
import pywolf.utils.strutils as s;

'''
all path returned will have '/' or '\\' suffix
'''

'''
normalize path items:
remove the first os.sep, if removeFirst is True
add os.sep, if the last is not os.sep
'''
def normalize(path: str, removeFirst=True, strip=False) -> str:
    if not path:
        return ""
    
    if strip:
        path = path.strip()

    if removeFirst and path.startswith(os.sep):
        path = path[1:]

    if not path.endswith(os.sep):
        path += os.sep
   
    return path

def strip(path: str) -> str:
    if not path:
        return path
    

    return path.strip(" "+os.sep)

def getLevel(path) -> int:
    if not path:
        return 1
    
    path = strip(path)
    arr = path.split(os.sep)

    return len(arr) + 1

'''
join path items array to path
'''
def join(*pathes: str) -> str:
    if not pathes:
        return ""
    
    result: str = None
    for path in pathes:
        if not path:
            raise SyntaxError("path can't be None")

        if result is None:
            result = normalize(path, False)
            continue

        result += normalize(path)
    
    return result
    


def dirname(file) -> str:
    return os.path.dirname(os.path.abspath(file)) + os.sep

def extension(fileName: str, withoutDot=False, toLower=False) -> str:
    s = pathlib.Path(fileName).suffix
    if not s:
        return None

    if toLower:
        s = s.lower()

    if withoutDot:
        return s.lstrip(".")
    
    return s


def isdir(fileName: str) -> bool:
    return os.path.isdir(fileName)

def isfile(fileName: str) -> bool:
    return os.path.isfile(fileName)

# if __name__ == '__main__':
#     print("txt :", extension("my_file.txt", True))
#     print(".txt :", extension("/Users/pankaj/abc.txt"))
#     print("None :", extension("/Users/pankaj/.bashrc", True))
#     print("jpg :", extension("/Users/pankaj/a.b/abc.jpg", True))
