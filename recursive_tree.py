from node import Node

def build_tree_recursive(value, height):
    if height <= 0:
        return None
    node = Node(value)
    node.left = build_tree_recursive(value * 2, height - 1)
    node.right = build_tree_recursive(value * 2 + 1, height - 1)
    return node