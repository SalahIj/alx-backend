#!/usr/bin/env python3
"""Imported modules"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """The function definition"""
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
