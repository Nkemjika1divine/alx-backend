#!/usr/bin/env python3
"""module for the class BasicCache"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """BasicCache inheriting from BaseCaching"""

    def __init__(self):
        """Init method"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Adds a key value pair to self.cache_data"""
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if key not in self.keys:
                    self.keys.append(key)
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.keys[0])
                    print('DISCARD:', self.keys[0])
                    self.keys.pop(0)

    def get(self, key):
        """Gets the value of a key from self.cache_data"""
        if key is None:
            return None

        for data in self.cache_data.keys():
            if key == data:
                value = self.cache_data[key]
                self.keys.remove(key)
                self.keys.append(key)
                return value

        return None
