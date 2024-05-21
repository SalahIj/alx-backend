#!/usr/bin/env python3
"""Imported modules"""


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """The class definition"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """the metod definition
        Args:
            key: the first input
            item: the second input
        """
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")
        self.cache_data[key] = item

    def get(self, key):
        """the get method
        Args:
            key: the input
        """
        return self.cache_data.get(key, None)
