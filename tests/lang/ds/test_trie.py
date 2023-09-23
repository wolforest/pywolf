import pytest

from pywolf.lang.ds.trie import Trie

def test_trie_insert():
    t = Trie()

    t.insert('a')
    assert 1 == t.root.counter

    t.insert('b')
    assert 2 == t.root.counter

def test_trie_exists():
    t = Trie()

    t.insert('abc')
    t.insert('bcd')

    assert True == t.exists('abc')
    assert True == t.exists('bcd')
    assert False == t.exists('bed')

def test_trie_search():
    t = Trie()
    t.insert("abc")
    t.insert("abcd")
    t.insert("abcde")
    t.insert("abcdef")
    t.insert("abcdefg")
    t.insert("abcdefgi")

    result: list = t.search('abcd')
    assert 5 == len(result)
