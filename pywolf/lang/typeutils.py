
import boltons.typeutils as butils




def make_sentinel(name='_MISSING', var_name=None):
    """
    Creates and returns a new **instance** of a new class, suitable for
    usage as a "sentinel", a kind of singleton often used to indicate
    a value is missing when ``None`` is a valid input.

    Args:
        name (str): Name of the Sentinel
        var_name (str): Set this name to the name of the variable in
            its respective module enable pickleability. Note:
            pickleable sentinels should be global constants at the top
            level of their module.

    >>> make_sentinel(var_name='_MISSING')
    _MISSING

    The most common use cases here in boltons are as default values
    for optional function arguments, partly because of its
    less-confusing appearance in automatically generated
    documentation. Sentinels also function well as placeholders in queues
    and linked lists.

    .. note::

      By design, additional calls to ``make_sentinel`` with the same
      values will not produce equivalent objects.

      >>> make_sentinel('TEST') == make_sentinel('TEST')
      False
      >>> type(make_sentinel('TEST')) == type(make_sentinel('TEST'))
      False

    """
    return butils.make_sentinel(name, var_name)


def issubclass(subclass, baseclass):
    """
    Just like the built-in :func:`issubclass`, this function checks
    whether *subclass* is inherited from *baseclass*. Unlike the
    built-in function, this ``issubclass`` will simply return
    ``False`` if either argument is not suitable (e.g., if *subclass*
    is not an instance of :class:`type`), instead of raising
    :exc:`TypeError`.

    Args:
        subclass (type): The target class to check.
        baseclass (type): The base class *subclass* will be checked against.

    >>> class MyObject(object): pass
    ...
    >>> issubclass(MyObject, object)  # always a fun fact
    True
    >>> issubclass('hi', 'friend')
    False
    """
    return butils.issubclass(subclass, baseclass)

def get_all_subclasses(cls):
    """Recursively finds and returns a :class:`list` of all types
    inherited from *cls*.

    >>> class A(object):
    ...     pass
    ...
    >>> class B(A):
    ...     pass
    ...
    >>> class C(B):
    ...     pass
    ...
    >>> class D(A):
    ...     pass
    ...
    >>> [t.__name__ for t in get_all_subclasses(A)]
    ['B', 'D', 'C']
    >>> [t.__name__ for t in get_all_subclasses(B)]
    ['C']

    """
    return butils.get_all_subclasses(cls)

class classproperty(object):
    """Much like a :class:`property`, but the wrapped get function is a
    class method.  For simplicity, only read-only properties are
    implemented.
    """

    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, cls):
        return self.fn(cls)