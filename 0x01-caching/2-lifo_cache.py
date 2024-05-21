#!/usr/bin/python3
"""Imported modules"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """the class definition"""
    def __init__(self):
        """the __init__ method"""
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """the put method
        Args:
            key: the first input
            item: the second input
        """
        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        """the get method
        Args:
            key: the input
        """
        with self.__rlock:
            return self.cache_data.get(key, None)

    def _balance(self, keyIn):
        """The method definition
        Args:
            keyIn: the input
        """
        keyOut = None
        with self.__rlock:
            keysLength = len(self.__keys)
            if keyIn not in self.__keys:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = self.__keys.pop(keysLength - 1)
                    self.cache_data.pop(keyOut)
            else:
                self.__keys.remove(keyIn)
            self.__keys.insert(keysLength, keyIn)
        return keyOut
