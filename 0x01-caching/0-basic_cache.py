#!/usr/bin/env python3
"""module for the class BasicCache"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inheriting from BaseCaching"""

    def __init__(self):
        """Init method"""
        super().__init__()

    def put(self, key, item):
        """Adds a key value pair to self.cache_data"""
        if key is None or item is None:
            return
        data = {key: item}
        self.cache_data.update(data)

    def get(self, key):
        """Gets the value of a key from self.cache_data"""
        if key is None:
            return None

        for data in self.cache_data.keys():
            if key == data:
                return self.cache_data[key]

        return None
