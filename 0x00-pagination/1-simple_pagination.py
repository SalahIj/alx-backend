#!/usr/bin/env python3
"""Imported modules"""
import csv
from typing import List, Tuple


class Server:
    """The class definition"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """The function definition"""
        nextPageStartIndex = page * page_size
        return nextPageStartIndex - page_size, nextPageStartIndex

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """The function definition"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndex, endIndex = self.index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]
