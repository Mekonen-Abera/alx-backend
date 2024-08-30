#!/usr/bin/env python3
"""
Implements deletion-resilient hypermedia pagination.
"""

import csv
from typing import Dict, List

class Server:
    """Server class to manage and paginate a dataset of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def load_dataset(self) -> List[List]:
        """Loads and caches the dataset from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Creates an indexed dataset for efficient pagination.
        
        Returns:
            Dict[int, List]: A dictionary mapping indices to dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.load_dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a page of items, ensuring that deleted rows do not affect pagination.
        
        Args:
            index (int): Start index of the current page.
            page_size (int): Number of items required for the current page.
        
        Returns:
            Dict: A dictionary containing:
                - index: The starting index for the current page
                - data: The list of items for the current page
                - page_size: The number of items returned
                - next_index: The index for the next page or None if no more pages exist
        """
        focus = []
        dataset = self.indexed_dataset()
        index = 0 if index is None else index
        keys = sorted(dataset.keys())
        assert index >= 0 and index <= keys[-1], "Index is out of range."
        
        # Collect valid indices for the requested page
        for key in keys:
            if key >= index and len(focus) < page_size:
                focus.append(key)

        data = [dataset[v] for v in focus[:-1]]  # Exclude the last element for data
        next_index = focus[-1] if len(focus) == page_size else None
        
        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }

