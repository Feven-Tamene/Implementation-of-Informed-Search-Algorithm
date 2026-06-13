from gbfs import greedy_best_first_search
from astar import astar_search
from graph import graph, heuristic_good

def main():
    start = "Arad"
    goal = "Bucharest"

    print("\n   GBFS RESULT")
    gbfs_result = greedy_best_first_search(graph, heuristic_good, start, goal)
    print(gbfs_result)

    print("\n   A* RESULT")
    astar_result = astar_search(graph, heuristic_good, start, goal)
    print(astar_result)

if __name__ == "__main__":
    main()
