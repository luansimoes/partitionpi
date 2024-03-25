from math import factorial, prod

def bin_comb(n):
    return choose(n, 2)

def choose(n, k):
    '''Return the number of k-subsets of a set with n elements.'''
    if not 0 <= k <= n:
        return 0
    
    a, b = sorted([n-k, k])
    product = prod(range(n, a, -1))
    return product/factorial(b)
    
