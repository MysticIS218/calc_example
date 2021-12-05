"""Writes to another CSV"""
# import time
import calc.calculations.csv_files.absolutepath as ap

class CSV_Writer: # pylint: disable=too-few-public-methods,consider-using-with
    """writing to another files"""

    @staticmethod
    def write_file(path: str, csv_content: str):
        """Write a string's content to a designated file path"""
        with open(ap.absolutepath(path), "w", encoding='utf-8') as file:
            file.write(csv_content)
            file.close()
