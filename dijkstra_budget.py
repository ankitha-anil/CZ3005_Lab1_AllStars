def dijsktra(graph, start, end, budget):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {start: (None, [0, 0])}
    energybudget = budget
    current_node = start
    visited = set()
    totalenergy = 0
    distance = 0

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1][0]
        energy_to_current_node = shortest_paths[current_node][1][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)][0] + weight_to_current_node
            energy = graph.weights[(current_node, next_node)][1] + energy_to_current_node
            if energy > energybudget:
                continue
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, [weight, energy])

            else:
                temp = shortest_paths[next_node]
                current_shortest_weight = temp[1][0]
                current_shortest_energy = temp[1][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, [weight, energy])

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"

        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

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
    print(*path, sep=' -> ')
