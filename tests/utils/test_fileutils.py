import pytest 

from pywolf.utils import fileutils 


def test_write_contents():
    filename = '/tmp/py_file_write_unit_test.txt'
    contents = 'hello python'

    fileutils.write_contents(filename, contents)

    with open(filename, "r") as f:
        file_contents = f.read()

    assert contents == file_contents


