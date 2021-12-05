"""Contains the absolute Path"""
from pathlib import Path


def absolute_path(filepath):
    """gets absolute path from relative path"""
    relative = Path(filepath)
    return relative.absolute()
