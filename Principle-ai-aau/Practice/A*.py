#!/usr/bin/env python3
from traveling_sales_man import traveling_sales_man as tsp

visited = set()
rec_path = []
def dfs(at):
    if at in visited:
        return
    visited.add(at)
    rec_path.append(at)
    for node in tsp.get(at):
        if node not in visited:
            dfs(node)


dfs("Addis Ababa")
print(rec_path)
