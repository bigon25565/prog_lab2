from node import Node

def build_tree_non_recursive(value, height):
    if height <= 0:
        return None
    root = Node(value)
    queue = [(root, height - 1)]
    while queue:
        current, h = queue.pop(0)
        if h > 0:
            current.left = Node(current.value * 2)
            current.right = Node(current.value * 2 + 1)
            queue.append((current.left, h - 1))
            queue.append((current.right, h - 1))
    return root