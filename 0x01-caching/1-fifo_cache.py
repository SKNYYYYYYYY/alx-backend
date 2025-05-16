#!/usr/bin/python3
"""FIFO caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system
    """

    def __init__(self):
        """ Constructor"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in  the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            print(f"DISCARD: {keys[0]}")
            first_key = keys[0]
            del self.cache_data[first_key]
