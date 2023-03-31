from urllib.parse import urlparse


class ConnectionUrl(object):
    url: str = ''
    engine: str = ''
    username: str = ''
    password: str = ''
    hostname: str = ''
    port: int = None
    database: str = ''
    query: str = ''

    def __init__(self, url: str):
        if not url:
            raise SyntaxError('connection url can not be blank')

        self.url = url
        result = urlparse(url)

        if result.scheme:
            self.engine = result.scheme

        if result.username:
            self.username = result.username

        if result.password:
            self.password = result.password

        if result.hostname:
            self.hostname = result.hostname

        if result.port:
            self.port = result.port

        if result.query:
            self.query = result.query

        self.init_database(result.path)

    def init_database(self, path: str):
        if not path:
            return

        ps = path.split('/')
        if not ps or len(ps) != 2:
            return

        p = ps[1].strip()
        if not p:
            return

        self.database = p
