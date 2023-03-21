import os

def current():
    return os.getcwd() + os.sep


if __name__=='__main__':
    print(current())
    print(os.sep)