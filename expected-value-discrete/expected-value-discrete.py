import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)
    rum  = np.sum(x*p)
    return float(rum)
    pass