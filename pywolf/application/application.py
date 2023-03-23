import asyncio

from pywolf.application.bootstrap import Bootstrap
from pywolf.application.context import context


class Application(object):

    def bootstrap(self, path):
        context.set_application(self)
        Bootstrap().boot(path)

        return self

    def run(main, args, debug=None):
        if not main:
            return

        asyncio.run(main)



# if __name__=='__main__':
#     Application().bootstrap('./').run(None)