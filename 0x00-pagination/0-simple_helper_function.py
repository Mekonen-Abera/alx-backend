#!/usr/bin/env python3
"""
Helper function for pagination
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for a given pagination.
    """
    if page < 1 or page_size <= 0:
        raise ValueError("Page must be >= 1 and page_size must be > 0")
    
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return (start_index, end_index)

