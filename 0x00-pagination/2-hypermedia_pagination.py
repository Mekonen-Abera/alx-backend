#!/usr/bin/env python3
"""
Implements the `get_hyper` method in the `Server` class for enhanced pagination.
"""
import csv
from typing import Dict, List, Tuple, Union

class Server:
    """Server class to manage and paginate a dataset of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def load_dataset(self) -> List[List]:
        """Loads and caches the dataset from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    @staticmethod
    def calculate_index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Calculates the start and end index for a given `page` and `page_size`.
        
        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.
        
        Returns:
            Tuple[int, int]: A tuple containing the start and end index.
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves items for the specified page number.
        
        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.
        
        Returns:
            List[List]: A list of rows for the specified page if inputs are valid,
                         otherwise an empty list.
        """
        assert isinstance(page, int) and isinstance(page_size, int), "page and page_size must be integers."
        assert page > 0 and page_size > 0, "page and page_size must be greater than zero."
        
        start_index, end_index = self.calculate_index_range(page, page_size)
        return self.load_dataset()[start_index:end_index]

    def get_hyper(self, page: int, page_size: int) -> Dict[str, Union[int, List[List], None]]:
        """
        Retrieves paginated data along with pagination details.
        
        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.
        
        Returns:
            Dict[str, Union[int, List[List], None]]: A dictionary containing pagination details:
                - page_size: Number of items on the current page
                - page: Current page number
                - data: List of items on the current page
                - next_page: Next page number or None if there is no next page
                - prev_page: Previous page number or None if there is no previous page
                - total_pages: Total number of pages available
        """
        data = self.get_page(page, page_size)
        total_rows = len(self.load_dataset())
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if self.calculate_index_range(page, page_size)[1] < total_rows else None
        total_pages = (total_rows + page_size - 1) // page_size  # Ceiling division
        
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

