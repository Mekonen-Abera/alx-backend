#!/usr/bin/env python3
"""Defines a class LIFOCache that inherits from
BaseCaching and implements a LIFO caching system.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class for a Last-In, First-Out caching system."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Remove the last item in the dictionary
                last_key, _ = self.cache_data.popitem()
                print("DISCARD: {}".format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The item stored in the cache, or None if the key does not exist.
        """
        return self.cache_data.get(key, None)

