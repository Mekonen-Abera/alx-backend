#!/usr/bin/env python3
"""
A function should return a tuple of size two containing 
a start index and an end index
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for a given pagination.
    """
    return ((page_size * (page - 1)), page_size * page)
