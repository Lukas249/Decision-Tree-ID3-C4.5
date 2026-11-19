import datetime

from build_decision_tree import build_decision_tree
from calculate_entropy import calculate_entropy
from get_all_occurrences_by_column import get_all_occurrences_by_column
from read_file import read_file

from tree_walk import tree_walk

def get_example_dataset():
    return read_file("test.txt", "r", "\n")

print("Loading dataset", datetime.datetime.now())
table = get_example_dataset()
print("Dataset loaded", datetime.datetime.now())
m = len(table)
n = len(table[0])

y_column_idx = n - 1

info = calculate_entropy(get_all_occurrences_by_column(table, y_column_idx))
print("Number of rows", len(table))
print("Building decision tree")

tree = build_decision_tree(table, info, y_column_idx)

print("Decision tree was built", datetime.datetime.now())

tree_walk(tree, 0)

