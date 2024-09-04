#!/usr/bin/env python3
"""Least Frequently Used (LFU) caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class for a Least Frequently Used caching system."""

    def __init__(self):
        """Initialize the cache and the list to track usage frequency."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """Reorder the items in the cache based on the most recently used item.

        Args:
            mru_key (str): The key of the most recently used item.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif not max_positions:
                max_positions.append(i)
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] >= mru_freq:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The item stored in the cache, or None if the key does not exist.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)

