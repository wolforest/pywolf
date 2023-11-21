
from pywolf.io.fs import FileStructure

def test_fs_scan():
    print("************************************")

    path = "/Users/wingle/code/github/amq/broker/src/main/java/org/apache/rocketmq/broker/"
    fs: FileStructure  = FileStructure(path)
    fs.scan()

    
    print("************************************")
    # fs.root.get_info()
    # for dir in fs.root.dirChildren:
    #     dir.get_info()


    fs.traverse()
