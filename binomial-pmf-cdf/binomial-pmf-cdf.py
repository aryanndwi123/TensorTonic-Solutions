import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here


    pmf = (p**k)*((1-p)**(n-k))
    sum = 0

    for i in range(k+1):
        sum += math.comb(n,i)*(p**i)*((1-p)**(n-i))

    pmf = math.comb(n,k)*pmf
    
    return {
        "pmf": float(pmf),
        "cdf": float(sum)
    }
    
    
    
    pass