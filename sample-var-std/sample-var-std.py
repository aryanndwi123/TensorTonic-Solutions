import numpy as np
import math as mt

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x = np.array(x)

    center = x - np.mean(x)
    vari = np.sum(center**2) / (x.size - 1)
    stdev = mt.sqrt(vari)
    

    
    
    return {
        "variance": float(vari),
        "standard_deviation": float(stdev)
    }
    pass