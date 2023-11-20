
from pywolf.io.fs import FileStructure


def test_fs_scan():
    path = "/Users/wingle/code/github/amq/broker/src/main/java/org/apache/rocketmq/broker/"
    fs: FileStructure  = FileStructure(path)
    fs.scan()


def test_fs_getLevel():
    fs = FileStructure("./")

    p1 = None
    assert 1 == fs.getLevel(p1)

    p2 = ""
    assert 1 == fs.getLevel(p2)

    p3 = "abc"
    assert 2 == fs.getLevel(p3)

    p4 = "abc/def"
    assert 3 == fs.getLevel(p4)

    p5 = "abc/def/hij"
    assert 4 == fs.getLevel(p5)

    p3 = " abc "
    assert 2 == fs.getLevel(p3)

    p4 = " abc/def"
    assert 3 == fs.getLevel(p4)

    p5 = "abc/def/hij "
    assert 4 == fs.getLevel(p5)