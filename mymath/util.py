import numpy as np
import pandas as pd

def square_root(v):
    return v * 2

def to_knudsen(v):
    return (v * (1.805 / 1.80655)) + 0.0

def average_vector(vector):
    return np.mean(vector)

def calc_cell_center_depth(blanking, cell_size, sensor_depth, velocity):
    velocity = np.array(velocity)
    velocity = [
        sensor_depth
        + blanking
        + (cell_size / 2)
        + (c * cell_size)
        for c in range(len(velocity))
    ]
    return velocity
