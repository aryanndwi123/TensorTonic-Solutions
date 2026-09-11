import numpy as np


def norm1(matrix,axis = None):
    matrix = np.array(matrix)
    total = np.sum(np.abs(matrix), axis=axis, keepdims=True)
    total = np.where(total == 0, 1.0, total)

    return matrix / total

def norm2(matrix,axis = None):
    matrix = np.array(matrix)
    total = np.sqrt(np.sum(matrix ** 2, axis=axis, keepdims=True))
    total = np.where(total == 0, 1.0, total)

    return matrix / total

def normmax(matrix,axis = None):
    matrix = np.array(matrix)
    total = np.max(np.abs(matrix), axis=axis, keepdims=True)
    total = np.where(total == 0, 1.0, total)

    return matrix / total
    

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:

    x = np.array(matrix)

    if norm_type == "l1":
        return norm1(x, axis)

    elif norm_type == "l2":
        return norm2(x, axis)

    elif norm_type == "max":
        return normmax(x, axis)

    else:
        raise ValueError("norm_type must be 'l1', 'l2', or 'max'")