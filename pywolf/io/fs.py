import os

import pywolf.utils.fileutils as f
import pywolf.utils.pathutils as p

class FileNode:
    dir : str = ""
    path: str = None
    name: str = None
    size: int = 0
    rows: int = 0
    level: int = -1

    def __init__(self, name: str, level: int=1, dir: str=None, ) -> None:
        if not name:
            raise SyntaxError("File name can't be None")
        
        self.level = level
        self.name = name
        self.__init_path()
    
    def count(self, countRowNumber=False, countLineLength=False) -> None:
        pass

    
    def __init_path(self, dir: str) -> None:

        if not dir:
            self.path = self.name
        else:
            self.dir = dir
            self.path = p.join(dir, self.name)
    
        

class FileStructure:
    baseDir: str = None
    nodeList: list = []


    def __init__(self, dir: str) -> None:
        if not dir:
            raise SyntaxError("Directory name can't be None")
        
        if not f.exists(dir):
            raise SystemError("Directory: " + dir + " doesn't exists")
        
        self.baseDir = dir

    def scan(self, **args) -> list:
        baseDirLen = len(self.baseDir)

        for root, ds, fs in os.walk(self.baseDir):
            for f in fs:
                print("file: " , self.getLevel(root[baseDirLen:]) , " : " +  f)
            
            for d in ds: 
                print("dir: " , self.getLevel(root[baseDirLen:]) , " : " + d)

    def getLevel(self, path) -> int:
        if not path:
            return 1
        
        path = p.strip(path)
        arr = path.split(os.sep)

        return len(arr) + 1


    