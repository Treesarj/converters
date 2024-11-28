import numpy as np

def square_root(v):
    return v * 2

def to_knudsen(v):
    return (v * (1.805 / 1.80655)) + 0.0

def average_vector(vector):
    return np.mean(vector)

def calc_cell_center_depth(blanking, cell_size, sensor_depth, df_north, df_east, df_w):
    for df_ in [df_north, df_east, df_w]:
        df_.columns = [
            sensor_depth
            + blanking
            + (cell_size / 2)
            + (c * cell_size)
            for c in df_.columns
        ]
    return {
        "df_north": df_north,
        "df_east": df_east,
        "df_w": df_w
    }

def calc_cell_center_depth1(blanking, cell_size, sensor_depth, df_north, df_east, df_w):
    for df_ in [df_north, df_east, df_w]:
        if isinstance(df_, pd.DataFrame):
            df_.columns = [
                sensor_depth
                + blanking
                + (cell_size / 2)
                + (c * cell_size)
                for c in range(len(df_.columns))
            ]
        else:
            raise TypeError(f"Expected DataFrame, got {type(df_)} instead.")
    
    return  df_north
