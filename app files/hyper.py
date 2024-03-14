import pantab
import pandas as pd
import os

def dataframe_to_hyper(df: pd.DataFrame, filename: str, table_name: str = "data_table") -> str:
  """
  Writes a pandas DataFrame to a Tableau Hyper extract file and returns the file path.

  Args:
      df (pd.DataFrame): The DataFrame to write to the Hyper file.
      filename (str): The name of the Hyper file to create.
      table_name (str, optional): The name of the table to create within the Hyper file. Defaults to "data_table".

  Returns:
      str: The path to the created Hyper file.
  """

  try:
    pantab.frame_to_hyper(df, filename, table = table_name)
    return (filename)
  except Exception as e:
    print(f"An error occurred during conversion: {e}")
    return None  # Indicate failure
