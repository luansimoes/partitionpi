# Partition&pi;
Partition&pi; is a Python library to handle integer partitions as lists and compute partitional analysis metrics. 

## Instalation
```
pip install partitionpi
```

## Get started
We are dealing with integer partitions as lists, for example:

```Python
import partitionpi as pp

p = [1,1,1,2,3]
```

### Computing main metrics
We provide methods to compute the main metrics related to partitional_analysis, such as the indices of agglomeration and dispersion, number of children obtained by the operations of mute and join, translation between the list form and the exponential form (via tuple or latex string)... Examples of usage of such functions:

```Python
# Compute the dispertion and agglomeration of p, that can be used for plotting.
x = pp.disp(p)
y = pp.agg(p)

# Compute the number of children by each operation.
nr_of_muted_children = pp.n_muted(p)
nr_of_joint_children = pp.n_joint(p)

# Translate p to both exponential and tex string form. 
exp = pp.exponential_form(p)
tex = pp.as_tex_str(p)
```

### Operations
Also, our library furnishes operations between partitions, such as union, intersection, concatenation/sum, difference and the operators *mute* and *join*. Union, intersection, sum and difference are computed like the multiset operators.

```Python
p1 = [1,1,2]
p2 = [1,2,3]

# p1 + p2 = [1,1,1,2,2,3]
p_sum = pp.concat(p1, p2)

# p1 - p2 = [1]
p_diff = pp.diff(p1, p2)

# p1 intersection p2 = [1,2]
p_inter = pp.intersection(p1, p2)

# p1 union p2 = [1,1,2,3]
p_union = pp.union(p1, p2)

# join(p1, 1, 1) = [2,2,3]
p_join = pp.join(p1, 1, 1)

# mute(p1, 3) = [1,1,2]
p_mute = pp.mute(p1, 3)
```

### Methods
Partition&pi; gives some methods to enumerate objects, such as:

- All partitions with a limited density-number.
- All ancestors or children of a given partition.
- The partitional complex of a given partition. 

Also, we furnish methods to compute the common parents of two partitions and the list of possible referential partitions of a set of partitions.

```Python
# Compute the ancestors with density number at most 7
ancestors = pp.all_ancestors(p, max_dn=7)

# Parents of p by each operation
mparents = pp.muted_parents(p, max_dn=7)
jparents = pp.joint_parents(p)

# Partitions with dn = 7 and with dn <= 7
p_eq_7 = partitions_of(7)
p_leq_7 = partitions_at_most(7)

# Partitional complex of p
comp = pp.partitional_complex(p)

# Common parents of p1 and p2
parents = pp.common_parents(p1, p2)

# List of possible referential partitions of [p, p1, p2]
ref = pp.referential_partition([p, p1, p2])
```


### Graph and Diagram
Finally, we furnish tools for generating a networkx graph of the partitional complex with labelled nodes and edges, and to plot its diagram. In the graph, each node has an attribute *pos*, which gives the pair *(agg, disp)* of each partition, and an attribute *label*, with the tex-style form of the partition. Each edge has the attribute *kinship*, that tells if it represents a mute (*M*) or a join (*J*) relation. 

```Python
# A nx.Graph modelling the partitional complex of g.
g = graph_complex(p)

# Plot diagram (can be called with the graph g or the partition p).
# Mute edges will be painted red and Join edges will be painted black.
draw_complex(g, {'M' : 'red', 'J' : 'black'})
```
Diagram for *p*:

![Diagram from draw_complex.](/img/example2.png)

Diagram for *p2*:

![Diagram from draw_complex.](/img/example.png)


## References
If you want to know more about Partitional Analysis, we refer to Pauxy Gentil-Nunes [webpage](https://pauxy.net/partitional-analysis-publications/) and [github](https://github.com/Pauxygnunes) page, where you can find publications, books and software about it.


