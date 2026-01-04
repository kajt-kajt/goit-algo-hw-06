import heapq
from math import inf
import networkx as nx
from task01 import tasks

def dijkstra(g, start) -> tuple[list[int], list[str]]:
    """
    Dijkstra shortest path search implementation
    """
    n = g.number_of_nodes()
    distances = { node:inf for node in g.nodes()}
    distances[start] = 0
    path = { node:None for node in g.nodes()}
    queue = [(0,start)]
    heapq.heapify(queue)
    while len(queue) > 0:
        curr_path, curr = heapq.heappop(queue)
        for next_node in nx.neighbors(g,curr):
            new_path = curr_path + g[curr][next_node]["weight"]
            if new_path < distances[next_node]:
                distances[next_node] = new_path
                path[next_node] = curr
                heapq.heappush(queue,(new_path,next_node))
    return (distances, path)

def dijkstra_modified(g, start) -> tuple[list[str]]:
    """
    Dijkstra algorithm modified to find longest path in acyclic graph
    """
    n = g.number_of_nodes()
    distances = { node:inf for node in g.nodes()}
    distances[start] = 0
    path = { node:None for node in g.nodes()}
    queue = [(0,start)]
    heapq.heapify(queue)
    while len(queue) > 0:
        curr_path, curr = heapq.heappop(queue)
        for next_node in nx.neighbors(g,curr):
            if g[curr][next_node]["weight"] == 0:
                path_metric = inf
            else:
                path_metric = 1/g[curr][next_node]["weight"]
            new_path = curr_path + path_metric
            if new_path <= distances[next_node]:
                distances[next_node] = new_path
                path[next_node] = curr
                heapq.heappush(queue,(new_path,next_node))
    return (path)

curr = "end"
dist, path = dijkstra(tasks, "start")
result = []
while curr!="start":
    dist_curr = dist[curr]
    curr = path[curr]
    result.append(f"Execute {curr} of duration {tasks.nodes[curr]["estimate"]}, total time spent {dist_curr}")
print("\n".join(result[-2::-1]))

print("-"*20)

curr = "end"
path = dijkstra_modified(tasks, "start")
time_spent = 0
result = []
while curr!="start":
    curr = path[curr]
    time_spent += tasks.nodes[curr]["estimate"]
    result.append(f"Execute {curr} of duration {tasks.nodes[curr]["estimate"]}")
print("\n".join(result[-2::-1]))
print(f"Total time spent: {time_spent}")
