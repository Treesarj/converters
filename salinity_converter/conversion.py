# salinity_converter/conversion.py

def knudsen_to_practical(s_knudsen):
    """
    Convert Knudsen salinity to Practical salinity.
    
    Parameters:
    s_knudsen (float): Knudsen salinity (parts per thousand)
    
    Returns:
    float: Practical salinity
    """
    return (s_knudsen - 0.03) * (1.80655 / 1.805)

def cox_to_practical(s_cox):
    """
    Convert Cox salinity to Practical salinity.
    
    Parameters:
    s_cox (float): Cox salinity (parts per thousand)
    
    Returns:
    float: Practical salinity
    """
    return s_cox  # Assuming Cox salinity is directly equivalent to Practical salinity

def practical_to_knudsen(v):
    """
    Convert Practical salinity to Knudsen salinity.
    
    Parameters:
    s_practical (float): Practical salinity
    
    Returns:
    float: Knudsen salinity (parts per thousand)
    """
    return (v * (1.805 / 1.80655)) + 0.03
r
def practical_to_cox(s_practical):
    """
    Convert Practical salinity to Cox salinity.
    
    Parameters:
    s_practical (float): Practical salinity
    
    Returns:
    float: Cox salinity (parts per thousand)
    """
    return s_practical  # Assuming Practical salinity is directly equivalent to Cox salinity
