"""
Let's create a task dependency tree.
Task description is in "tasks.json" file.
"""

import json
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs_assign_layers(g, start):
    """
    Let's assign nodes in graph their layer in layered layout
    """
    visited = { node: False for node in g.nodes() }
    queue = deque()
    queue.append(start)
    for node in g.nodes:
        g.nodes[node]["layer"] = 1000
    while len(queue) > 0:
        current = queue.popleft()
        if not visited[current]:
            visited[current] = True
            for next_node in nx.neighbors(g, current):
                queue.append(next_node)
                g.nodes[next_node]["layer"] = min(g.nodes[current]["layer"] - 5, g.nodes[next_node]["layer"])

# Let's load tasks description from json file
with open("tasks.json", "r", encoding = "utf-8") as f:
    tasks_loaded = json.load(f)

# Creating directed graph
tasks = nx.DiGraph()
# Creating nodes
tasks.add_nodes_from(["start", "end"])
tasks.nodes["start"]["estimate"] = 0
tasks.nodes["end"]["estimate"] = 0
for task in tasks_loaded["tasks"]:
    tasks.add_node(task["id"], title = task["title"], estimate = int(task["estimate"]))
# Creating edges
# The weight of edge is estimate time for dependency node
for task in tasks_loaded["tasks"]:
    if not task["dependency"]:
        tasks.add_edge("start", task["id"], weight = 0)
    else:
        for dep in task["dependency"]:
            tasks.add_edge(dep, task["id"], weight = tasks.nodes[dep]["estimate"])

for node in tasks.nodes():
    if tasks.out_degree(node) == 0 and node != "end":
        tasks.add_edge(node, "end", weight = tasks.nodes[node]["estimate"])

if __name__ == "__main__":
    bfs_assign_layers(tasks, "start")
    print("Let's display some graph properties.")
    print("General characteristics: ", tasks)
    betweenness_centrality = nx.betweenness_centrality(tasks)
    print("Nodes properties: ")
    for node in tasks.nodes:
        print(node," -> ",tasks.nodes[node])
        print("   node degre: ", nx.degree(tasks, node))
        print("   betweenness centrality: ", betweenness_centrality[node])
    print("Edges properties: ")
    for edge in tasks.edges:
        print(edge," -> ",tasks.edges[edge])

    # Let's visualize graph
    nx.draw(tasks,
            nx.multipartite_layout(tasks, 
                                   subset_key = 'layer', 
                                   align = "horizontal", 
                                   scale = 100),
            with_labels = True,
            width = 1,
            arrows = True,
            node_size = 2000,
            node_color = "lightblue",
            edge_color = "grey"
            )
    plt.title(tasks_loaded["description"])
    plt.show()

