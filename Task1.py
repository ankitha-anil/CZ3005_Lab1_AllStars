import json
from collections import defaultdict
import networkx as nx
import dijkstra


class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


with open("content/Dist.json", "r") as json_file:
    distdata = json.load(json_file)

    distlist = []
    for (key, values) in distdata.items():
        list1 = key.split(',')
        list1.append(values)
        distlist.append(tuple(list1))

with open("content/Cost.json", "r") as json_file:
    costdata = json.load(json_file)

    costlist = []
    for (key, values) in costdata.items():
        list1 = key.split(',')
        list1.append(values)
        costlist.append(tuple(list1))

distgraph = Graph()
for edge in distlist:
    distgraph.add_edge(*edge)

costgraph = Graph()
for edge in costlist:
    costgraph.add_edge(*edge)

choice = 0
while choice != "exit":
    print("1. Shortest Distance Path (No Constraints)")
    print("2. Shortest Cost Path (No Constraints)")
    choice = input()
    if choice == "1":
        print("Shortest Path based on Distance: ")
        dijkstra.dijsktra(distgraph, '1', '50')
    elif choice == "2":
        print("Shortest path based on cost:")
        dijkstra.dijsktra(costgraph, '1', '50')
