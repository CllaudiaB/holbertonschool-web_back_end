#!/usr/bin/python3
"""LRU Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        self.od = OrderedDict()

    def put(self, key, item):
        if key is None and item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.od.move_to_end(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_use = next(iter(self.od))
            self.cache_data.pop(last_use)
            self.od.pop(last_use)
            print(f"DISCARD: {last_use}")
        self.cache_data[key] = item
        self.od[key] = item
        return self.cache_data

    def get(self, key):
        """ Get an item by key
        """
        if key not in self.cache_data or key is None:
            return
        self.od.move_to_end(key)
        return self.cache_data[key]