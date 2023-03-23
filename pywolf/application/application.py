import asyncio

from pywolf.application.bootstrap import Bootstrap
from pywolf.application.context import context

class Application(object):

    def bootstrap(self, path):
        context.set_application(self)
        context.set_root_path(path)

        Bootstrap().boot(context)

        return self

    def run(main, args, debug=None):
        if not main:
            return

        asyncio.run(main, args, debug)



# if __name__=='__main__':
#     Application().bootstrap('./').run(None)