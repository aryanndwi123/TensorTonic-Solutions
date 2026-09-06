import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """

    res = np.array(x)

    pmf = np.where(res==1,p,1.0-p)
    
    mean = p
    vari = p*(1-p)
    
    
    return {
        "pmf": pmf,
        "mean": float(mean),
        "variance": float(vari)
    }
    
    pass