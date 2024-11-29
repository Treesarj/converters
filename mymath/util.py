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

def calc_cell_center_depth1111(blanking,cell_size,sensor_depth,velocity):  
    for df_ in [velocity]:
        df_.columns = [
            sensor_depth
            + blanking
            + (cell_size / 2)
            + (c * cell_size)
            for c in range(len(df_.columns))
        ]   
    return velocity
