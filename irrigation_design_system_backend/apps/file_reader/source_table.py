from pandas import read_csv
from pathlib import Path

class SourceTable:

  def reference_table_reading(path):

    p = Path(path)

    df = read_csv(p)
    return df
  