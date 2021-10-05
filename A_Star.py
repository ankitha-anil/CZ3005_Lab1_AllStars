import math
import json

def A_Star(graph, start, end, budget):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    with open("content/coord.json", "r") as coord_file:
        coorddata = json.load(coord_file)
        i=0
        h_cost = {}
        while(i<len(coorddata)):
            h_cost[str(i+1)]= math.sqrt((math.pow((coorddata[str(i+1)][0] - coorddata[end][0]), 2) + math.pow((coorddata[str(i+1)][1] - coorddata[end][1]),2)))
            i+=1

    shortest_paths = {start: (None, [0, 0, 0])} #Prev Node,[Distance,Energy, FCost]
    energybudget = budget
    current_node = start
    visited = set()
    loopcount = 0
    totalenergy = 0
    distance = 0




    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1][0]
        energy_to_current_node = shortest_paths[current_node][1][1]
        FCost_to_current_node = shortest_paths[current_node][1][2]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)][0] + weight_to_current_node
            energy = graph.weights[(current_node, next_node)][1] + energy_to_current_node
            finalcost = h_cost[str(next_node)] + weight

            if energy > energybudget:
                continue
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, [weight, energy, finalcost])

            else:
                temp = shortest_paths[next_node]
                current_shortest_weight = temp[1][0]
                current_shortest_energy = temp[1][1]
                shortest_hcost = temp[1][2]
                if shortest_hcost > finalcost:
                    shortest_paths[next_node] = (current_node, [weight, energy, finalcost])
            loopcount += 1
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"

        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1][2])

# mylist = [[7, 8], [1, 2, 3], [2, 5, 6]]
# list(map(lambda x: x[1], mylist)) returns [8, 2 ,5]
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        # print(current_node, next_node)

        if next_node is not None:
            totalenergy += graph.weights[(current_node, next_node)][1]
            distance += graph.weights[(current_node, next_node)][0]

        current_node = next_node

    # Reverse path
    path = path[::-1]
    print('Total Energy: ', totalenergy)
    print("Total Distance: ", distance)
    print("Loop Count: ", loopcount)
    print(*path, sep=' -> ')
