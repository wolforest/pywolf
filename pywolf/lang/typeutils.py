import boltons.typeutils as butils


def make_sentinel(name='_MISSING', var_name=None):
    return butils.make_sentinel(name, var_name)


def issubclass(subclass, baseclass):
    return butils.issubclass(subclass, baseclass)


def get_all_subclasses(cls):
    return butils.get_all_subclasses(cls)


class classproperty(object):
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, cls):
        return self.fn(cls)
