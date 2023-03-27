import os
import pytest

import boltons.fileutils as butils


def write_contents(file: str, contents):
    if isinstance(contents, str):
        return write_string(file, contents)
    elif isinstance(contents, bytes):
        return write_bytes(file, contents)

    raise SyntaxError("Can not write contents other than str or bytes")


def write_string(file: str, contents):
    with open(file, "w+") as f:
        f.write(contents)


def write_bytes(file: str, contents: bytes):
    with open(file, "wb+") as f:
        f.write(contents)


def append_contents(file: str, contents: str):
    with open(file, "a+") as f:
        f.write(contents)


def read_contents(file: str) -> str:
    if not exists(file):
        raise FileExistsError(file + " not exists")

    with open(file, "r") as f:
        # max file length = 10M
        return f.read(10 * 1024 * 1024)


def read_lines(file: str) -> list:
    if not exists(file):
        raise FileExistsError(file + " not exists")

    with open(file, "r") as f:
        return f.readlines()


def exists(file: str) -> bool:
    if not file:
        return False

    if not os.path.exists(file):
        return False

    return os.path.isfile(file)
