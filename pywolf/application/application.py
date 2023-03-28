import asyncio

from pywolf.application.bootstrap import Bootstrap
from pywolf.application.context import context


class Application(object):
    def __init__(self, path):
        context.set_application(self)
        Bootstrap().boot(path)

    def run(self, main, args, debug=None):
        if not main:
            return

        asyncio.run(main)

# if __name__=='__main__':
#     Application().bootstrap('./').run(None)
