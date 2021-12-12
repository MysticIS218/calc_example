import calculator.csv_files.absolute_path as ap
import pandas as pd
from calc.calculator import Calculator
from datetime import datetime
from calculator.csv_files.csv_writer import CSV_Writer

class CSV_Reader:
    # pylint: disable=too-few-public-methods,pointless-string-statement,consider-using-enumerate,line-too-long

    @staticmethod
    def get_csv_content(absPath: str):
        """return content found"""
        content = pd.get_csv_content(ap.absolute_path(absPath))
        content_data_frame = pd.DataFrame(content)
        return content_data_frame
    

    @staticmethod
    def csv_addition(get_csv_content):
        
