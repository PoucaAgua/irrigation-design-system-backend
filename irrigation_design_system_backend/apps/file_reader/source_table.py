from pandas import read_csv

class SourceTable:

  def reference_table_reading(path):
    df = read_csv(path)
    return df
  