import pandas as pd
import numpy as np

def has_docstring(func):
  """Check to see if the function 
  `func` has a docstring.

  Args:
    func (callable): A function.

  Returns:
    bool
  """
  return func.__doc__ is not None


def load_and_plot_data(filename):
  """Load a data frame and plot each column.
  
  Args:
    filename (str): Path to a CSV file of data.
  
  Returns:
    pandas.DataFrame
  """
  df = pd.load_csv(filename, index_col=0)
  df.hist()
  return df


def as_2D(arr):
  """Reshape an array to 2 dimensions"""
  return np.array(arr).reshape(1, -1)

def log_product(arr):
  return np.exp(np.sum(np.log(arr)))