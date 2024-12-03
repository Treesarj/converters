import numpy as np
import pandas as pd

def square_root(v):
    return v * 2
    
def multiply(x,y):
    return x*y
    
def to_knudsen(v):
    return (v * (1.805 / 1.80655)) + 0.0

def average_vector(vector):
    return np.mean(vector)

def str_to_float(vector):
    return  vector.astype(float).tolist()

def calc_cell_center_depth(blanking,cell_size,sensor_depth,velocity):  
    print(blanking)
    print(cell_size)
    print(sensor_depth)
    print(velocity)
    for df_ in [velocity]:
        df_.columns = [
            sensor_depth
            + blanking
            + (cell_size / 2)
            + (c * cell_size)
            for c in range(len(df_.columns))
        ]   
    return velocity

def cell_center_depth(blanking,cell_size,sensor_depth,velocity):
    new_column_names = [
        sensor_depth
        + blanking
        + (cell_size / 2)
        + (c * cell_size)
        for c in range(len(velocity.columns))
    ]
    return new_column_names

def create_dataframe(*columns):
    """
    This function takes multiple columns as separate parameters and returns a DataFrame by concatenating them.

    Parameters:
    *columns: Variable length argument list of pandas Series or DataFrame objects

    Returns:
    pd.DataFrame: A DataFrame created by concatenating the input columns
    """
    # Concatenate the columns along axis=1 (columns)
    df = pd.concat(columns, axis=1)

    return df
