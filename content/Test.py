import sys
import json
import math
from queue import Queue




def dijkstra(graph, start, goal):
    shortest_distance = {}
    cost = {}
    track_predecessor = {}
    unseenNodes = graph
    inf = 9999999
    energy_budget = 287932
    te = {}
    track_path = []

    for node in unseenNodes:
        shortest_distance[node] = inf
        te[node] = inf
    shortest_distance[start] = 0
    te[start] = 0

    while unseenNodes:

        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node

            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        #print(path_options)

        for child_node, weight in path_options:
            if weight[1] + te[min_distance_node] > energy_budget:
                continue
            ##          if weight[1] + te[min_distance_node] <= energy_budget:
            ##                print("Total value within budget!")
            if weight[0] + shortest_distance[min_distance_node] < shortest_distance[child_node]:

                #print("Total Energy: ", te[child_node])
                #if te[child_node] <= energy_budget:
                shortest_distance[child_node] = weight[0] + shortest_distance[min_distance_node]
                te[child_node] = weight[1] + te[min_distance_node]
                track_predecessor[child_node] = min_distance_node
                #else:
                    #change value for impossible to distance 999
                    #track_predecessor[child_node] = min_distance_node
                #elif te[child_node] > energy_budget:
                    #shortest_distance[child_node] = inf

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print("Path is not reachable")
            break

    track_path.insert(0, start)

    #if shortest_distance[goal] != inf:
    if True:
        print("Shortest distance is " + str(shortest_distance[goal]))
        print("Optimal path is " + str(track_path))
    else:
        print("Infinite Distance!!")




# graph = {
#     '0': {'1': [4, 4], '7': [8, 8]},
#     '1': {'0': [4, 4], '2': [8, 8], '7': [11, 11]},
#     '2': {'1': [8, 8], '8': [2, 2], '3': [7, 7], '5': [4, 4]},
#     '3': {'2': [7, 7], '4': [9, 1], '5': [14, 1]},
#     '4': {'3': [9, 1], '5': [10, 100]},
#     '5': {'2': [4, 4], '3': [14, 1], '4': [10, 100], '6': [2, 2]},
#     '6': {'5': [2, 2], '7': [1, 1], '8': [6, 6]},
#     '7': {'0': [8, 8], '1': [11, 11], '6': [1, 1], '8': [7, 7]},
#     '8': {'2': [2, 2], '6': [6, 6], '7': [7, 7]}
# }
# dijkstra(graph, '0', '4')

