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


def draw_complex(obj_to_draw, colors = {'M':'red', 'J':'black'}, png_file = None):
    '''Plot the partitional complex of the object, with option to save the figure.'''

    fig, ax = plt.subplots()

    if isinstance(obj_to_draw, list):
        obj_to_draw = graph_complex(obj_to_draw)
    
    assert isinstance(obj_to_draw, nx.Graph), 'Object must be a networkx.Graph or a partition.'

    pos = nx.get_node_attributes(obj_to_draw, 'pos')
    node_labels = {node : as_tex_str(node) for node in obj_to_draw.nodes}
    edge_colors = [colors[obj_to_draw[p1][p2]['kinship']] for p1,p2 in obj_to_draw.edges()]

    nx.draw(obj_to_draw, 
            pos=pos, 
            edge_color=edge_colors, 
            with_labels=True, 
            labels=node_labels,
            ax = ax,
            node_shape = 'o',
            node_color = 'white',
            node_size = 300,
            font_size = 8)

    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    ax.set_xlabel('Agglomeration')
    ax.set_ylabel('Dispersion')
    ax.set_axis_on()

    plt.show()