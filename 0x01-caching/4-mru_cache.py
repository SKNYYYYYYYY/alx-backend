#!/usr/bin/python3
"""MRU caching system"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """implements MRU caching policy"""
    counter = 0

    def __init__(self):
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """insert an item to cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item

            self.keys[key] = MRUCache.counter
            MRUCache.counter += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # find second last value
            values = sorted(list(self.keys.values()), reverse=True)
            mru_value = values[1]

            for key, val in self.keys.items():
                if val == mru_value:
                    mru_key = key
            print(f"DISCARD: {mru_key}")
            del self.cache_data[mru_key]
            del self.keys[mru_key]

    def get(self, key):
        """returns the key's item"""
        if key is None or key not in self.cache_data:
            return None
        else:
            self.keys[key] = MRUCache.counter
            MRUCache.counter += 1
            return self.cache_data[key]
