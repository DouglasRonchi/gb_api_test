"""
A Database Interface
Uses to force the implementation of the methods that a database class should to have.
"""
from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        """To be implemented with a connect method"""
        raise NotImplementedError

    @abstractmethod
    def check_connection(self):
        """To be implemented with a check connection method"""
        raise NotImplementedError
