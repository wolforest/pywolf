from urllib.parse import urlparse, ParseResult


class Connection(ParseResult):
    database: str = None
    engine: str = None
    url: str = None

    def __init__(self, url: str):
        if not url:
            raise SyntaxError('connection url can not be blank')

        self.url = url
        result = urlparse(url)
        super().__init__(result.scheme)

        self.engine = result.scheme
        self.username = result.username
        self.password = result.password
        self.hostname = result.hostname
        self.port = result.port
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
