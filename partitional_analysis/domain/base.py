from .math_utils import bin_comb


def dn(p):
    '''Return the density-number of p.'''
    return sum(p)

def n_parts(p):
    '''Return the number of parts in p.'''
    return len(p)

def distinct(p):
    '''Return a list with the distinct parts in p.'''
    return list(set(p))

def repeated(p):
    '''Return the parts in p that appear more than once.'''
    return [b for b in distinct(p) if p.count(b)>1]

def single(p):
    '''Return the parts in p that appears only once.'''
    return [b for b in distinct(p) if p.count(b)==1]

def total_comb(p):
    '''Return the total number of binary combinations for the density-number of p.'''
    return bin_comb(dn(p)) 

def agg(p):
    '''Return the agglomeration index of p.'''
    return sum([bin_comb(b) for b in p])

def disp(p):
    '''Return the dispersion index of p.'''
    a = sum([b for b in p])**2
    b = sum([b**2 for b in p])
    return (a-b)/2

def n_muted(p):
    '''Return the number of children of p by the mute operation.'''
    return len(set(p))

def n_joint(p):
    '''Return the number of children of p by the join operation.'''
    u = len(distinct(p))
    r = len(repeated(p))
    return bin_comb(u)+r

def exponential_form(p):
    '''Return p on its exponential form.'''
    return [(b, p.count(b)) for b in distinct(p)]

def map_form(p):
    '''Return p on its map form.'''
    return {b : p.count(b) for b in distinct(p)}

def as_str(p):
    '''Return p as a string.'''
    return '.'.join([str(b) for b in p])