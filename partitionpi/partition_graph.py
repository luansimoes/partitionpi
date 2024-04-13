from .domain import all_muted, all_joint, as_tex_str, agg, disp
import networkx as nx
import matplotlib.pyplot as plt

def graph_complex(p):
    '''Return a networkx graph modelling the partitional complex of p.'''
    g = nx.Graph()

    complex = [p]
    i = 0

    while i < len(complex):

        partition = complex[i]

        muted = all_muted(partition)
        joint = all_joint(partition)

        for desc in muted:
            if not desc in complex:
                complex.append(desc)
            g.add_edge(tuple(partition), tuple(desc), kinship = 'M')
        
        for desc in joint:
            if not desc in complex:
                complex.append(desc)
            g.add_edge(tuple(partition), tuple(desc), kinship = 'J')
        
        i += 1

        g.nodes[tuple(partition)]['pos'] = (agg(partition), disp(partition))
        g.nodes[tuple(partition)]['label'] = as_tex_str(partition)
        
    return g


def draw_complex(obj_to_draw, 
                 colors = {'M':'red', 'J':'black'}, 
                 styles = {'M':'solid', 'J':'solid'}):
    '''Plot the partitional complex of the object with custom colors and edge styles.'''

    fig, ax = plt.subplots()

    if isinstance(obj_to_draw, list):
        obj_to_draw = graph_complex(obj_to_draw)
    
    assert isinstance(obj_to_draw, nx.Graph), 'Object must be a networkx.Graph or a partition.'

    pos = nx.get_node_attributes(obj_to_draw, 'pos')
    node_labels = {node : as_tex_str(node) for node in obj_to_draw.nodes}

    edges = {'M':[], 'J':[]}
    [edges[obj_to_draw[e[0]][e[1]]['kinship']].append(e) for e in obj_to_draw.edges()]



    if obj_to_draw.number_of_nodes() < 25:
        nx.draw_networkx_nodes(obj_to_draw,
                               pos=pos,
                               ax=ax,
                               node_shape='o',
                               node_color='white',
                               node_size=300)
        nx.draw_networkx_labels(obj_to_draw,
                                pos=pos,
                                labels=node_labels,
                                ax=ax,
                                font_size=8)
        nx.draw_networkx_edges(obj_to_draw,
                               pos=pos,
                               edgelist=edges['M'],
                               style=styles['M'],
                               edge_color=colors['M'],
                               ax=ax)
        nx.draw_networkx_edges(obj_to_draw,
                               pos=pos,
                               edgelist=edges['J'],
                               style=styles['J'],
                               edge_color=colors['J'],
                               ax=ax)
    else:
        nx.draw_networkx_nodes(obj_to_draw,
                               pos=pos,
                               ax=ax,
                               node_shape='.',
                               node_color='green',
                               node_size=100)
        nx.draw_networkx_edges(obj_to_draw,
                               pos=pos,
                               edgelist=edges['M'],
                               style=styles['M'],
                               edge_color=colors['M'],
                               ax=ax)
        nx.draw_networkx_edges(obj_to_draw,
                               pos=pos,
                               edgelist=edges['J'],
                               style=styles['J'],
                               edge_color=colors['J'],
                               ax=ax)

    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    ax.set_xlabel('Agglomeration')
    ax.set_ylabel('Dispersion')
    ax.set_axis_on()

    plt.show()