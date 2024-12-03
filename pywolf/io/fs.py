import os

import pywolf.utils.fileutils as f
import pywolf.utils.pathutils as p

class DirNode:
    def __init__(self, parent: str, level: int, name: str=None) -> None:
        self.parent = p.normalize(parent, removeFirst=False, strip=True)
        self.level = level

        if name is None:
            self.name = "root"
            self.path = self.parent
        else:
            self.name = name
            self.path = p.join(self.parent, name)
        
        self.fileChildren = set()
        self.dirChildren = set()


    def get_info(self) -> str:
        #print("dir: level= ", self.level, "; name= ", self.name, "; dirs: ", len(self.dirChildren), "; files: ", len(self.fileChildren))
        print("  " * (self.level - 1) + "|--" + self.name + " [subDirs: ", len(self.dirChildren),  "; files: " , len(self.fileChildren), "]")
        pass

    def add_file(self, file) -> None:
        self.fileChildren.add(file)
    
    def add_dir(self, dir) -> None:
        self.dirChildren.add(dir)


class FileNode:
    fileCount: int = 0

    def __init__(self, parent:DirNode, name: str) -> None:
        if not name:
            raise SyntaxError("File name can't be None")

        self.name = name
        self.parent = parent
        self.lineNumber = 0
        self.path = os.path.join(parent.path, self.name)
    
    def get_info(self) -> str:
        #print("file: ", self.name)
        num = self.parent.level
        lines =  self.count_lines()

        if lines < 300:
            return

        FileNode.fileCount += 1
        print(self.fileCount, "|" +"----" * num + self.name + " lines: ", lines)

    def count_lines(self) -> int:
        if self.lineNumber > 0:
            return self.lineNumber
        
        for line in open(self.path):
            self.lineNumber += 1
        
        return self.lineNumber

    def count(self, countRowNumber=False, countLineLength=False) -> None:
        pass

  
class FileStructure:
    def __init__(self, path: str) -> None:
        if not path:
            raise SyntaxError("Directory name can't be None")
        
        if not f.exists(path):
            raise SystemError("Directory: " + path + " doesn't exists")
        
        self.root = DirNode(path, 1, None)

    def scan(self, node: DirNode=None) -> None:
        if node is None:
            node = self.root

        for file in os.listdir(node.path):
            self.__parse_file(node, file)

    def traverse(self, node: DirNode=None):
        if node is None:
            node = self.root
            node.get_info()

        #for file in node.fileChildren:
            #file.get_info()

        for dir in node.dirChildren:
            dir.get_info()
            self.traverse(dir)

    def __parse_file(self, node: DirNode, file: str) -> None:
        path = p.join(node.path, file)
        if p.isdir(path):
            dir = self.__add_dir(node, file)
            self.scan(dir)
        else:
            self.__add_file(node, file)


    def __add_dir(self, parent: DirNode, file: str) -> DirNode:
        child = DirNode(parent.path, parent.level + 1, file)
        parent.add_dir(child)

        return child

    def __add_file(self, parent: DirNode, file: str) -> FileNode:
        child = FileNode(parent, file)
        parent.add_file(child)

        return child
        
    


    