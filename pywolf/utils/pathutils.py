import os
import pathlib

'''
all path returned will have '/' or '\\' suffix
'''


def dirname(file):
    return os.path.dirname(os.path.abspath(file)) + os.sep

def extension(fileName: str, withoutDot=False, toLower=False):
    s = pathlib.Path(fileName).suffix
    if not s:
        return None

    if toLower:
        s = s.lower()

    if withoutDot:
        return s.lstrip(".")
    
    return s


if __name__ == '__main__':
    print("txt :", extension("my_file.txt", True))
    print(".txt :", extension("/Users/pankaj/abc.txt"))
    print("None :", extension("/Users/pankaj/.bashrc", True))
    print("jpg :", extension("/Users/pankaj/a.b/abc.jpg", True))
