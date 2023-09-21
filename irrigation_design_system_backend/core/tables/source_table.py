import os.path
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))


class SourceTable:
    @staticmethod
    def reference_table_reading(path: str, delimiter: str = ",", decimal: str = "."):
        full_path = script_dir + path
        return pd.read_csv(full_path, delimiter=delimiter, decimal=decimal, encoding="utf-8")
