#!/usr/bin/env python3
"""Defines a class LRUCache that inherits from
BaseCaching and implements a Least Recently Used (LRU) caching system.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class for a Least Recently Used caching system."""

    def __init__(self):
        """Initialize the cache and the list to track usage."""
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {}'.format(discard))

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The item stored in the cache, or None if the key does not exist.
        """
        if key is not None and key in self.cache_data:
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None

