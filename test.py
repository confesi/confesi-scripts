def build_tree(data, current_node):
    children = []
    for node_name, parents in data.items():
        if current_node in parents:
            node = {'name': node_name, 'children': build_tree(data, node_name)}
            children.append(node)
    return children

data = {
    'A': [],
    'B': ['A'],
    'C': ['A'],
    'D': ['A'],
    'E': ['A', 'B'],
    'F': ['A', 'B'],
    'G': ['A', 'C'],
    'H': ['A', 'D'],
    'I': ['A', 'D', 'H']
}

tree = {'name': 'A', 'children': build_tree(data, 'A')}

print(tree)