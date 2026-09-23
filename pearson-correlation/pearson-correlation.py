import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.array(X,dtype = float)
    centered = X - np.mean(X,axis = 0)
    
    cov = (centered.T @ centered)/(X.shape[0] -1)
    sd = np.sqrt(np.diag(cov))
    deno = np.outer(sd, sd)
    with np.errstate(divide="ignore", invalid="ignore"):
        return cov / deno
    
    pass