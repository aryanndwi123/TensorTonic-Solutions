import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    sum =0.0
    
    for i in range(len(y)):
        sum += x[i]*y[i]
        
        
        
    return sum    
    pass