import os.path

from pandas import read_csv
from pathlib import Path

script_dir = os.path.dirname(os.path.abspath(__file__))


class SourceTable:

  @staticmethod
  def reference_table_reading(path):

    p = script_dir + path

    df = read_csv(p)
    return df
  