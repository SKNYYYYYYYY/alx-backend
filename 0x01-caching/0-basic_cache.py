#!/usr/bin/python3
""" basic caching implementation
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """   a basic caching system
    """

    def put(self, key, item):
        """ add item to cache
        """
        if key or item is not None:
            self.cache_data.update({key: item})
        else:
            pass

    def get(self, key):
        """ retunr the value of the key
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
