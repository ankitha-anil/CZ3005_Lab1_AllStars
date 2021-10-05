import math
import json



##    open_set = set(start) 
##    closed_set = set()
##    g = {} #store distance from starting node
##    parents = {}# parents contains an adjacency map of all nodes
## 
##    #ditance of starting node from itself is zero
##    g[start_] = 0
##    #start_node is root node i.e it has no parent nodes
##    #so start_node is set to its own parent node
##    parents[start] = start
##         
##         
##    while len(open_set) > 0:
##        n = None
## 
##        #node with lowest f() is found
##        for v in open_set:
##            if n == None or g[v] + h_cost(v,end) < g[n] + h_cost(n,end):
##                n = v
##             
##                     
##        if n == end or graph.edges[n] == None:
##            pass
##        else:
##            for (m, weight) in graph.edges(n):
##                #nodes 'm' not in first and last set are added to first
##                #n is set its parent
##                if m not in open_set and m not in closed_set:
##                    open_set.add(m)
##                    parents[m] = n
##                    g[m] = g[n] + graph.weight[m,n][0]
##                         
##     
##                #for each node m,compare its distance from start i.e g(m) to the
##                #from start through n node
##                else:
##                    if g[m] > g[n] + graph.weight[m,n][0]:
##                        #update g(m)
##                        g[m] = g[n] + graph.weight[m,n][0]
##                        #change parent of m to n
##                        parents[m] = n
##                             
##                        #if m in closed set,remove and add to open
##                        if m in closed_set:
##                            closed_set.remove(m)
##                            open_set.add(m)
## 
##        if n == None:
##            print('Path does not exist!')
##            return None
## 
##            # if the current node is the stop_node
##            # then we begin reconstructin the path from it to the start_node
##        if n == end:
##            path = []
## 
##            while parents[n] != n:
##                path.append(n)
##                n = parents[n]
## 
##            path.append(start)
## 
##            path.reverse()
## 
##            print('Path found: {}'.format(path))
##            return path
## 
## 
##            # remove n from the open_list, and add it to closed_list
##            # because all of his neighbors were inspected
##            open_set.remove(n)
##            closed_set.add(n)
## 
##        print('Path does not exist!')
##        return None
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)

def A_Star(graph, start, end, budget):    
    shortest_paths = {start: (None, [0, 0, 0, 0])}#[weight, energy, h_cost, combined cost]
    energybudget = budget
    current_node = start
    visited = set()
    totalenergy = 0
    distance = 0
    weight = 0
    combined_cost = 0 

    with open("content/coord.json", "r") as coord_file:
        coorddata = json.load(coord_file)
        i=0
        h_cost = {}
        while(i<len(coorddata)):
            h_cost[str(i+1)]= math.sqrt((math.pow((coorddata[str(i+1)][0] - coorddata[end][0]),2) + math.pow((coorddata[str(i+1)][1] - coorddata[end][1]),2)))
            i+=1


    print(h_cost[start])
    print(h_cost[end])
    print(h_cost['1219'])


    
    while current_node != end:
        
        visited.add(current_node)
        destinations = graph.edges[current_node]

        weight_to_current_node = shortest_paths[current_node][1][0] 
        energy_to_current_node = shortest_paths[current_node][1][1]
##        print("weight before for loop:",weight)


        for next_node in destinations:

##            print("weight_to_current_node:",weight_to_current_node)
            weight = graph.weights[(current_node, next_node)][0] + weight_to_current_node 
##            print("weight during for loop:",weight)
            energy = graph.weights[(current_node, next_node)][1] + energy_to_current_node
            
            if energy > energybudget:
                continue
            print("next node:",next_node)
            if next_node not in shortest_paths:
                print("current node",current_node)
                combined_cost = weight + h_cost[current_node]
                shortest_paths[next_node] = (current_node, [weight, energy, h_cost[str(current_node)], combined_cost])
            else:
                temp = shortest_paths[next_node]
                current_shortest_weight = temp[1][0]
                current_shortest_energy = temp[1][1]
                current_combined_cost = temp[1][2]+ current_shortest_weight
                if (current_combined_cost > weight + h_cost[str(current_node)]):
##                    print("current shortest weight",current_shortest_weight)
##                    print("weight",weight)
                    shortest_paths[next_node] = (current_node, [weight, energy, h_cost[str(current_node)], current_combined_cost])


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
        print("shortest_paths[current_node]:",shortest_paths[current_node])
        print(current_node, next_node)

        if next_node is not None:
            totalenergy += graph.weights[(current_node, next_node)][1]
            distance += graph.weights[(current_node, next_node)][0]

        current_node = next_node

    # Reverse path
    path = path[::-1]
    print('Total Energy: ', totalenergy)
    print("Total Distance: ", distance)
    print(*path, sep=' -> ')
