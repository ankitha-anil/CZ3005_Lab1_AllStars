from collections import defaultdict
import json


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


def loadDistGraph():
    with open("content/Dist.json", "r") as json_file:
        distdata = json.load(json_file)

        distlist = []
        for (key, values) in distdata.items():
            list1 = key.split(',')
            list1.append(values)
            distlist.append(tuple(list1))

    distgraph = Graph()
    for edge in distlist:
        distgraph.add_edge(*edge)

    return distgraph


def loadCombinedGraph():
    with open("content/Dist.json", "r") as dist_file:
        with open("content/Cost.json", "r") as cost_file:
            distdata = json.load(dist_file)
            costdata = json.load(cost_file)
            combinedlist = []
            for (key, values) in distdata.items():
                cost = costdata[key]
                combined = [values, cost]
                list1 = key.split(',')
                list1.append(combined)
                combinedlist.append(tuple(list1))

    combinedgraph = Graph()
    for edge in combinedlist:
        combinedgraph.add_edge(*edge)

    return combinedgraph
