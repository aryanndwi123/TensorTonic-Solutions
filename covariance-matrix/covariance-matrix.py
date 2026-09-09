import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """

    X = np.array(X)

    cen = X - np.mean(X, axis=0)

    ans = (cen.T @ cen) / (X.shape[0] - 1)

    return ans

    
    
    
    pass