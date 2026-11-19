from typing import List


def divide_table_by_column_values(table: List[List[str]], column_idx: int) -> dict[str, List[List[str]]]:
    table_children: dict[str, List[List[str]]] = {}

    for row in table:
        val = row[column_idx]

        if val not in table_children:
            table_children[val] = []

        table_children[val].append(row)

    return table_children