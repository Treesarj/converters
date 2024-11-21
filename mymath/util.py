import numpy as np

def square_root(v):
    return v * 2

def to_knudsen(v):
    return (v * (1.805 / 1.80655)) + 0.0

def average_vector(vector):
    return np.mean(vector)
