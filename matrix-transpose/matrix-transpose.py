import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    ans  = []
    for j in range(len(A[0])): # 3
        v = []
        for i in range(len(A)): #2
             # append A[j][i]
             v.append(A[i][j])
        
        ans.append(v)

    return np.array(ans)
    pass
