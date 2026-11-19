from typing import List


class Node:
    def __init__(self, table: List[List[str]], children: dict[str, 'Node'] | None, column_idx: int):
        self.table = table
        self.children = children
        self.column_idx = column_idx