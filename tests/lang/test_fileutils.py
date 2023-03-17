from pywolf.lang import fileutils 


def test_write_contents():
    filename = '/tmp/py_file_write_unit_test.txt'
    contents = 'hello python'

    fileutils.write_contents(filename, contents)

    with open(filename, "r") as f:
        fileContents = f.read()

    print(fileContents)
    assert contents == fileContents


