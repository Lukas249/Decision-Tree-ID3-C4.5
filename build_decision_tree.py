from typing import List

from Node import Node
from calculate_entropy import calculate_entropy
from divide_table_by_column_values import divide_table_by_column_values
from find_best_column_to_divide import find_best_column_to_divide
from get_all_occurrences_by_column import get_all_occurrences_by_column

def build_decision_tree(table: List[List[str]], info: float, y_column_idx: int) -> Node:
    best_column_idx = find_best_column_to_divide(table, info, y_column_idx)

    if best_column_idx == -1:
        return Node(table, None, -1)

    table_children = divide_table_by_column_values(table, best_column_idx)

    children = {}

    for value, table_child in table_children.items():
        entropy = calculate_entropy(get_all_occurrences_by_column(table_child, y_column_idx))
        children[value] = build_decision_tree(table_child, entropy, y_column_idx)

    node = Node(table, children, best_column_idx)

    return node