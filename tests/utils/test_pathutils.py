import pytest

from pywolf.utils import pathutils

def test_extension():
    assert "txt" == pathutils.extension("my_file.txt", True)
    assert ".txt" == pathutils.extension("/Users/pankaj/abc.txt")
    assert None == pathutils.extension("/Users/pankaj/.bashrc", True)
    assert "jpg" == pathutils.extension("/Users/pankaj/a.b/abc.jpg", True)

    assert "JPG" == pathutils.extension("/Users/pankaj/a.b/abc.JPG", True)
    assert "jpg" == pathutils.extension("/Users/pankaj/a.b/abc.JPG", True, True)

def test_strip():
    assert "" == pathutils.strip("") 
    assert "abc" == pathutils.strip("abc") 
    assert "abc" == pathutils.strip(" abc") 
    assert "abc" == pathutils.strip("abc ") 
    assert "abc" == pathutils.strip(" abc ") 

    assert "abc" == pathutils.strip("/abc") 
    assert "abc" == pathutils.strip("/abc/") 
    assert "abc" == pathutils.strip("abc/")

    assert "abc" == pathutils.strip(" /abc ") 
    assert "abc" == pathutils.strip(" /abc/ ") 
    assert "abc" == pathutils.strip(" abc/ ")  

def test_getLevel():
    p1 = None
    assert 1 == pathutils.getLevel(p1)

    p2 = ""
    assert 1 == pathutils.getLevel(p2)

    p3 = "abc"
    assert 2 == pathutils.getLevel(p3)

    p4 = "abc/def"
    assert 3 == pathutils.getLevel(p4)

    p5 = "abc/def/hij"
    assert 4 == pathutils.getLevel(p5)

    p3 = " abc "
    assert 2 == pathutils.getLevel(p3)

    p4 = " abc/def"
    assert 3 == pathutils.getLevel(p4)

    p5 = "abc/def/hij "
    assert 4 == pathutils.getLevel(p5)