import pytest

from pywolf.utils import pathutils

def test_extension():
    assert "txt" == pathutils.extension("my_file.txt", True)
    assert ".txt" == pathutils.extension("/Users/pankaj/abc.txt")
    assert None == pathutils.extension("/Users/pankaj/.bashrc", True)
    assert "jpg" == pathutils.extension("/Users/pankaj/a.b/abc.jpg", True)

    assert "JPG" == pathutils.extension("/Users/pankaj/a.b/abc.JPG", True)
    assert "jpg" == pathutils.extension("/Users/pankaj/a.b/abc.JPG", True, True)
