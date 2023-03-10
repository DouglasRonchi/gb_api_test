"""
A singleton metaclass
"""
import threading

lock = threading.Lock()


class Singleton(type):
    """
    Thread Safe Singleton
     See at https://stackoverflow.com/questions/50566934/why-is-this-singleton-implementation-not-thread-safe
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
