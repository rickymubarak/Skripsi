"""
Yearly University of Alabama enrollments from 1971 to 1992.
"""

from pyFTS.data import common
import pandas as pd
import numpy as np


def get_data():
    """
    Get a simple univariate time series data.
    :return: numpy array
    """
    dat = get_dataframe()
    dat = np.array(dat["manual"])
    return dat


def get_dataframe():
    dat = common.get_dataframe('manual.csv',
                               'https://github.com/rickymubarak/Skripsi/blob/master/manual.csv',
                               sep=";")
    return dat