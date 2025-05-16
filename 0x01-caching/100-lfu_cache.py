#!/usr/bin/python3
"""LRU caching system"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    implements LRU cache policy
    """
    counter = 0

    def __init__(self):
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """inserts a key-item pair to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

            self.keys[key] = LFUCache.counter
            LFUCache.counter += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # get  LRU
            counters = self.keys.values()
            for key, val in self.keys.items():
                if val == min(counters):
                    lr_key = key
            print(f"DISCARD: {lr_key}")
            del self.cache_data[lr_key]
            del self.keys[lr_key]

    def get(self, key):
        """return the item"""
        if key is None or key not in self.cache_data:
            return None
        else:
            self.keys[key] = LFUCache.counter
            LFUCache.counter += 1
            return self.cache_data[key]
