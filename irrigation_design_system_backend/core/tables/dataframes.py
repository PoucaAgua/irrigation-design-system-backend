import os
import pandas as pd

tables_dir = os.path.dirname(os.path.abspath(__file__))


class Dataframes:
    PATH = "files"

    def __init__(self):
        file_names = [
            os.path.splitext(file_name)[0]
            for file_name in os.listdir(os.path.join(tables_dir, self.PATH))
        ]

        for file_name in file_names:
            setattr(self, f"{file_name}", self._load_data(file_name))

    def _load_data(self, file_name):
        file_path = os.path.join(tables_dir, os.path.join(self.PATH, f"{file_name}.csv"))
        return pd.read_csv(os.path.join(tables_dir, file_path), encoding="utf-8")


dataframes = Dataframes()
