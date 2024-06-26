#!/usr/bin/python3
"""
task-1: FIFO caching
"""

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Inherits from BaseCaching and is
    a caching system
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the
        item value for the key key
        """
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            my_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {my_key}")
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data
        linked to key
        """
        return self.cache_data.get(key, None)
