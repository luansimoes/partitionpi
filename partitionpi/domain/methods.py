from .base import dn, n_parts,  distinct
from .operators import mute, join, diff, intersection, concat, union

def joint_parents(p):
    '''Return the parents of p from the join operation.'''
    result = []
    for b in distinct(p):
        for i in range(int(b/2)):
            p_copy = [c for c in p]
            p_copy.remove(b)
            result.append(sorted(p_copy + [i+1, b-(i+1)]))
    return result

def muted_parents(p, max_dn=None):
    '''Return the parents of p from the mute operation.'''
    if not max_dn:
        max_dn = dn(p)+1
    
    rem_voices = max_dn - dn(p)

    result = []
    copy = [b for b in p]
    for i in range(rem_voices):
        result.append(sorted(copy+[i+1]))
    return result

def all_ancestors(p, max_dn=None):
    '''Return all the ancestors of p with a maximum density-number'''
    if not max_dn:
        max_dn = dn(p)+1

    result = [p]
    parents = muted_parents(p, max_dn) + joint_parents(p)
    while len(parents)>0:
        new_parents = []
        for par in parents:
            if par not in result:
                result.append(par)
                new_parents += muted_parents(par, max_dn) + joint_parents(par)

        parents = new_parents
    
    return result

def all_muted(p):
    '''Return the children of p obtained by the mute operation.'''
    if n_parts(p)==1: 
        return []
    return [mute(p, b) for b in distinct(p)][::-1]

def all_joint(p):
    '''Return the children of p obtained by the join operation.'''
    result = []
    d = distinct(p)
    for i, b1 in enumerate(d):
        for b2 in d[i:]:
            if b1!=b2 or p.count(b1)>1:
                result.append(join(p, b1, b2))
    return result[::-1]
    
def partitional_complex(p):
    '''Return the partitional complex of p.'''
    complex = [p]

    muted = all_muted(p)
    joint = all_joint(p)
    children = muted + joint

    while len(children)>0:
        new_muted = []
        new_joint = []
        for partition in children:
            if partition not in complex:
                complex.append(partition)
                muted = all_muted(partition)
                joint = all_joint(partition)
                new_muted += muted 
                new_joint += joint

        children = new_muted + new_joint
        
    return complex

def partitions_of(n, k=1):
    '''Yield all the partitions with density-number n where all parts are at least k. '''
    if n==0:
        yield []
    elif n==1:
        yield [1]
    else:
        for i in range(k, int(n/2)+1):
            for p in partitions_of(n-i, max(k, i)):
                yield [i] + p
        yield [n]

def partitions_at_most(n):
    '''Return a list of all partitions with density-number at most n.'''
    result = []
    for i in range(1, n+1):
        result += list(partitions_of(i))
    return result

def common_muted_ancestor(p1, p2):
    '''Return the common ancestor between p1 and p2 only by the mute operation.'''
    
    return union(p1, p2)

def common_joint_parents(p1, p2):
    '''Return the common parent of p1 and p2 by the join operation.'''
    if dn(p1)!=dn(p2):
        return []
    p1_parents = joint_parents(p1)
    p2_parents = joint_parents(p2)
    return [p for p in p1_parents if p in p2_parents]

def common_parents(p1, p2):
    '''Return common parents between p1 and p2 by both mute and join operations.'''
    max_dn = dn(diff(p1,p2))+dn(diff(p2,p1))+dn(intersection(p1, p2))
    p1_par = muted_parents(p1, max_dn) + joint_parents(p1)
    p2_par = muted_parents(p2, max_dn) + joint_parents(p2)
    return [p for p in p1_par if p in p2_par]

def ref_partition(partitions, max_dn=None):
    '''Return a list with possible referential partitions for a list of partitions.'''
    if max_dn==None:
        max_dn = max([dn(p) for p in partitions])

    p_refs = []
    for p in partitions:
        p_comp = all_ancestors(p, max_dn)
        if len(p_refs)==0:
            p_refs = p_comp
        else:
            p_refs = [x for x in p_refs if x in p_comp]
    
    return p_refs