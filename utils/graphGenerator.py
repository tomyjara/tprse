from graphviz import Digraph

dot = Digraph(comment='The Round Table', format='png')

dot.node('A', 'Susceptible')
dot.node('B', 'Incubando')
dot.node('C', 'Inf. Leve')
dot.node('D', 'Inf. Grave')
dot.node('E', 'Muerto')
dot.node('F', 'Recuperado')


dot.edges(['AB', 'BC', 'BD', 'DE', 'DF', 'CF', 'FA'])

styles = {
    'graph': {
        'label': '',
        'fontsize': '16',
        'fontcolor': 'black',
        'bgcolor': '#ffffff',
        'rankdir': 'BT',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'hexagon',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#006699',
    },
    'edges': {
        'style': 'dashed',
        'color': 'black',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'white',
    }
}

def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph

dot = apply_styles(dot, styles)
dot.render(filename='estados_sirs', view=True)