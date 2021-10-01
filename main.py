import json
from collections import defaultdict
import networkx as nx
import content.Test
import dijkstra
import dijkstra_budget


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

    def add_edge(self, from_node, to_node, distance):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = distance
        self.weights[(to_node, from_node)] = distance

    # def add_edge(self, from_node, to_node, weight):
    #     # Note: assumes edges are bi-directional
    #     self.edges[from_node].append(to_node)
    #     self.edges[to_node].append(from_node)
    #     self.weights[(from_node, to_node)] = weight
    #     self.weights[(to_node, from_node)] = weight


# with open("content/Dist.json", "r") as json_file:
#     distdata = json.load(json_file)
#
#     distlist = []
#     for (key, values) in distdata.items():
#         list1 = key.split(',')
#         list1.append(values)
#         distlist.append(tuple(list1))
#     # print(distlist)
#
# with open("content/Cost.json", "r") as json_file:
#     costdata = json.load(json_file)
#
#     costlist = []
#     for (key, values) in costdata.items():
#         list1 = key.split(',')
#         list1.append(values)
#         costlist.append(tuple(list1))
#     # print(costlist)
#
# with open("content/Dist.json", "r") as dist_file, \
#         open("content/Cost.json", "r") as cost_file, \
#         open("content/G.json", "r") as g_file:
#     distdata = json.load(dist_file)
#     costdata = json.load(cost_file)
#     graphjson = json.load(g_file)
#     mainlist = {}
#     for key, value in graphjson.items():
#         key_value = {}
#         for node in value:
#             key_value[node] = [distdata[key + "," + node], costdata[key + "," + node]]
#         mainlist[key] = key_value
#
#     first5pairs_mainlist = {i: mainlist[i] for i in list(mainlist)[:5]}
#     print(first5pairs_mainlist)

with open("content/Dist.json","r") as dist_file:
    with open("content/Cost.json","r") as cost_file:
        distdata = json.load(dist_file)
        costdata = json.load(cost_file)
        combinedlist = []
        for (key, values) in distdata.items():
            cost = costdata[key]
            combined = [values,cost]
            list1 = key.split(',')
            list1.append(combined)
            #print(list1)
            combinedlist.append(tuple(list1))
    #print(combinedlist)



# distgraph = Graph()
# for edge in distlist:
#     distgraph.add_edge(*edge)
#
# costgraph = Graph()
# for edge in costlist:
#     costgraph.add_edge(*edge)

combinedgraph = Graph()
for edge in combinedlist:
    combinedgraph.add_edge(*edge)

choice = 0
while choice != "exit":
    print("What do you want to do?")
    print("1. Shortest Distance Path (No Constraints)")
    print("2. Shortest Cost Path (No Constraints)")
    print("exit")
    choice = input()
    if choice == "1":
        print("Shortest Path based on Distance: ")
        #dijkstra.dijsktra(distgraph, '1', '50')
    elif choice == "2":
        print("Shortest path based on cost:")
       # dijkstra.dijsktra(costgraph, '1', '50')
    elif choice =="3":
        dijkstra_budget.dijsktra(combinedgraph,'1','50')

