import numpy as np
import math as mt

def dot(a: list, b:list ) -> float:
    sum = 0.0
    for i in range(len(a)):
        sum += a[i]*b[i]


    return sum

def eucnorm(a:list,b:list):
    x = 0.0
    for i in range(len(a)):
        x+= a[i]*a[i]

    y = 0.0
    for i in range(len(a)):
        y+= b[i]*b[i]
    print(x,y)

    ans = mt.sqrt(x)*mt.sqrt(y)

    return ans
        

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    x = dot(a,b)
    y = eucnorm(a,b)

    print(x,y)

    return 0.0 if y == 0 else x / y
    pass