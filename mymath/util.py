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

def calc_cell_center_depth(blanking, cell_size, sensor_depth, velocity):
    # Ensure velocity is a list or array
    if isinstance(velocity, (np.ndarray, list)):
        # Calculate new velocity values
        velocity = [
            sensor_depth
            + blanking
            + (cell_size / 2)
            + (c * cell_size)
            for c in range(len(velocity))
        ]
    else:
        raise TypeError(f"Expected velocity to be a list or ndarray, got {type(velocity)} instead.")
    
    return velocity

def calc_cell_center_depth1(velocity):
    blanking = 1
    cell_size = 0.5
    sensor_depth = 5
    velocity = [
            sensor_depth
            + blanking
            + (cell_size / 2)
            + (c * cell_size)
            for c in range(len(velocity))
        ]    
    return velocity

def calc_cell_center_depth11(velocity):
    blanking = 1
    cell_size = 0.5
    sensor_depth = 5
    for df_ in [velocity]:
        df_.columns = [
            sensor_depth
            + blanking
            + (cell_size / 2)
            + (c * cell_size)
            for c in range(len(df_.columns))
        ]   
    return velocity

def calc_cell_center_depth111(blanking,cell_size,sensor_depth,velocity):
    blanking = 1
    cell_size = 0.5
    sensor_depth = 5
    for df_ in [velocity]:
        df_.columns = [
            sensor_depth
            + blanking
            + (cell_size / 2)
            + (c * cell_size)
            for c in range(len(df_.columns))
        ]   
    return velocity

def calc_cell_center_depth1111(blanking,cell_size,sensor_depth,velocity):
    blanking = blanking
    cell_size = cell_size
    sensor_depth = sensor_depth
    for df_ in [velocity]:
        df_.columns = [
            sensor_depth
            + blanking
            + (cell_size / 2)
            + (c * cell_size)
            for c in range(len(df_.columns))
        ]   
    return velocity

def calc_cell_center_depth11111(blanking,cell_size,sensor_depth,velocity):
    # blanking = blanking
    # cell_size = cell_size
    # sensor_depth = sensor_depth
    # for df_ in [velocity]:
    #     df_.columns = [
    #         sensor_depth
    #         + blanking
    #         + (cell_size / 2)
    #         + (c * cell_size)
    #         for c in range(len(df_.columns))
    #     ]   
    return velocity


