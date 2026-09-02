from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean = np.mean(x)
    med = np.median(x)

    
    

    c = Counter(x)
    max_freq = max(c.values())
    mod = min(num for num,freq in c.items() if freq == max_freq )

    return {
    "mean": float(mean),
    "median": float(med),
    "mode": float(mod)
}
        
    pass