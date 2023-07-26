import os

'''
all path returned will have '/' or '\\' suffix
'''


def dirname(file):
    return os.path.dirname(os.path.abspath(file)) + os.sep


# if __name__ == '__main__':
#     pass
