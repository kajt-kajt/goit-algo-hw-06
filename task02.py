"""
BFS and DFS algorithms for graph
"""

import networkx as nx
from collections import deque
# get graph from task01
from task01 import tasks

def bfs(g, start) -> list[str]:
    """
    Let's generate traversal order based on BFS algorithm
    """
    visited = { node: False for node in g.nodes() }
    result = []
    queue = deque()
    queue.append(start)
    while len(queue) > 0:
        current = queue.popleft()
        if not visited[current]:
            visited[current] = True
            result.append(current)
            queue.extend(nx.neighbors(g, current))
    return result

