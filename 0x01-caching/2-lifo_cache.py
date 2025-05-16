#!/usr/bin/python3
"""LIFO caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Lifo caching"""

    def __init__(self):
        super().__init__()
        self.ky = []

    def put(self, key, item):
        """inserts the data to the dict while discarding the recently inserted"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.ky.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.ky[len(self.ky) - 2]
            # last_key = keys[len(keys) - 2]
            print("DISCARD: {}".format(last_key))
            del self.cache_data[last_key]

    def get(self, key):
        """returns the key's item"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
