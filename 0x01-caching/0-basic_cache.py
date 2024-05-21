#!/usr/bin/env python3
"""Imported modules"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class definition"""
    def put(self, key, item):
        """The method definition
        Args:
            key: the first input
            item: the second input
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """the method definition
        Args:
            key: the input
        """
        return self.cache_data.get(key, None)
