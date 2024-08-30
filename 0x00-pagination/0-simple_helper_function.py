#!/usr/bin/env python3
"""
Defines a function named `calculate_index_range`
"""
from typing import Tuple

def calculate_index_range(current_page: int, items_per_page: int) -> Tuple[int, int]:
    """
    Computes the starting and ending index for a specific page in pagination.
    
    Args:
        current_page (int): The current page number (1-indexed).
        items_per_page (int): The number of items displayed on each page.
        
    Returns:
        Tuple[int, int]: A tuple containing the starting and ending index for the specified page.
    """
    start_index = (current_page - 1) * items_per_page
    end_index = start_index + items_per_page
    return start_index, end_index
