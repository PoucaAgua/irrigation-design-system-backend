import os

from core.tables.read_file import read_file


def df_test_table():
    dir_name = os.path.dirname(__file__)
    path = os.path.join(dir_name, "file", "test.csv")
    return read_file(path)
