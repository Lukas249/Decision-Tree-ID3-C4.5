from typing import List


def read_file(file_name: str, mode: str, newline: str) -> List[List[str]]:
    file = open(file_name, mode, newline=newline)

    line = file.readline()

    table = []

    while line:
        line = line.strip()
        row = line.split(",")
        table.append(row)
        line = file.readline()

    file.close()

    return table