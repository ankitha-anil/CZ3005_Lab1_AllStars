import A_Star
import dijkstra
import dijkstra_Budget
import load_Data

print("Loading information...")

#Graph for Task 1 and Task 2
distgraph = load_Data.loadDistGraph()

# Graph for Task 3
combinedgraph = load_Data.loadCombinedGraph()

print("Completed loading.\n")

choice = 0
while choice != "exit":
    print("---------------------------------------------------------")
    print("|                        Menu                           |")
    print("--------------------------------------------------------|")
    print("|   1. Shortest Distance Path (No Constraints)          |")
    print("|   2. Shortest Distance with Constraints               |")
    print("|   3. Shortest Distance using A*Star w/ Constraints    |")
    print("|-------------------------------------------------------|")
    print("|   Energy Budget is : 287932                           |")
    print("---------------------------------------------------------")

    print("Enter choice : ")
    choice = input()

    # Task 1 - Shortest Distance Path (No Constraints)
    if choice == "1":
        start = str(input("Input Start Point: "))
        end = str(input("Input End Point: "))
        dijkstra.dijsktra(distgraph, start, end)

    # Task 2 - Shortest Distance with Constraints
    elif choice == "2":
        start = str(input("Input Start Point: "))
        end = str(input("Input End Point: "))
        budget = int(input("Input Budget of Path: "))
        dijkstra_Budget.dijsktra_Budget(combinedgraph, start, end, budget)

    # Task 3 - Shortest Distance using A*Star w/ Constraints
    elif choice == "3":
        start = str(input("Input Start Point: "))
        end = str(input("Input End Point: "))
        budget = int(input("Input Budget of Path: "))
        A_Star.A_Star(combinedgraph, start, end, budget)

    else:
        exit(0)


