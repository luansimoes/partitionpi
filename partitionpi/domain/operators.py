import itertools

def concat(*partitions):
    '''Return the concatenation of all partitions.'''
    return sorted(list(itertools.chain(*partitions)))

def diff(p1, p2):
    '''Return a partition formed by the parts of p1 that are not in p2.'''
    result = [b for b in p1]
    for c in p2:
        if c in result:
            result.remove(c)
    return result

def intersection(p1, p2):
    '''Return a partition formed by the parts that are in both p1 and p2.'''
    p2_copy = [b for b in p2]
    result = []
    for c in p1:
        if c in p2_copy:
            p2_copy.remove(c)
            result.append(c)
    return result

def union(p1, p2):
    '''Return a partition formed by the parts that are in p1 or in p2.'''
    p2_copy = [b for b in p2]
    result = []
    for c in p1:
        if c in p2_copy:
            p2_copy.remove(c)
        result.append(c)
    result += p2_copy
    return sorted(result)

def mute(p, block):
    '''Return p without the specified block.'''
    result = [b for b in p]
    if block in p:
        result.remove(block)
    return result

def join(p, b1, b2):
    '''Return p with blocks b1 and b2 joined.'''
    result = [b for b in p]
    if b1 in result:
        joint = b1
        result.remove(b1)
        if b2 in result:
            joint += b2
            result.remove(b2)    
    result.append(joint)

    return sorted(result)