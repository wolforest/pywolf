from pywolf.net.connection import ConnectionUrl


def test_url_parse_work_1():
    url = 'engine://username:password@localhost:123/database'
    conf = ConnectionUrl(url)

    assert 'engine' == conf.engine
    assert 'username' == conf.username
    assert 'password' == conf.password
    assert 'localhost' == conf.hostname
    assert 123 == conf.port
    assert 'database' == conf.database


def test_url_parse_work_2():
    url = 'engine://:password@localhost:123/database'
    conf = ConnectionUrl(url)

    assert 'engine' == conf.engine
    assert conf.username == ''
    assert 'password' == conf.password
    assert 'localhost' == conf.hostname
    assert 123 == conf.port
    assert 'database' == conf.database


def test_url_parse_work_3():
    url = 'engine://@localhost:123/database'
    conf = ConnectionUrl(url)

    assert 'engine' == conf.engine
    assert conf.username == ''
    assert conf.password == ''
    assert 'localhost' == conf.hostname
    assert 123 == conf.port
    assert 'database' == conf.database


def test_url_parse_work_4():
    url = 'engine://username:password@localhost/database'
    conf = ConnectionUrl(url)

    assert 'engine' == conf.engine
    assert 'username' == conf.username
    assert 'password' == conf.password
    assert 'localhost' == conf.hostname
    assert conf.port is None
    assert 'database' == conf.database
