"""
BFS and DFS algorithms for graph
"""

from collections import deque
import networkx as nx
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

def dfs(g, start) -> list[str]:
    """
    Let's generate traversal order based on DFS algorithm
    """
    visited = { node: False for node in g.nodes() }
    result = []
    stack = deque()
    stack.append(start)
    while len(stack) > 0:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            stack.extend(nx.neighbors(g, current))
            result.append(current)
    return result

def dfs_postorder(g, start, visited = None) -> list[str]:
    """
    Let's generate postorder traversal order based on DFS algorithm
    Recursive implementation
    """
    if not visited:
        visited = { node: False for node in g.nodes() }
    result = []
    if not visited[start]:
        visited[start] = True
        for next_node in nx.neighbors(g, start):
            if not visited[next_node]:
                result.extend(dfs_postorder(g,next_node,visited))
        result.append(start)
    return result

print("BFS traversal order: ")
print(bfs(tasks, "start"))
print("DFS traversal order: ")
print(dfs(tasks, "start"))
print("DFS postorder traversal order inversed becomes task execution plan: ")
print((dfs_postorder(tasks, "start")[::-1]))
