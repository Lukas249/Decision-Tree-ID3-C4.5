from Node import Node


def tree_walk(tree: Node, depth: int = 0) -> None:
    if not tree.children:
        return

    for column_value, child in tree.children.items():
        if not child.children:
            print(" " * depth + f"Column {tree.column_idx + 1}: {column_value} -> {child.table[0][-1]}")
        else:
            print(" " * depth + f"Column {tree.column_idx + 1}: {column_value}")

        tree_walk(child, depth + 1)