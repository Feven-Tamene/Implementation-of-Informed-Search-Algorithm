from queue import PriorityQueue
 
def astar_search(graph, heuristic, start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], 0, start))  # (f, g, node)
 
    visited = set()
    parent = {}
    g_cost = {start: 0}
    expansion_order = []
 
    while not pq.empty():
        _, g, current = pq.get()
 
        if current in visited:
            continue
 
        visited.add(current)
        expansion_order.append(current)
 
        # goal check
        if current == goal:
            break
 
        # explore neighbors
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g_cost[current] + cost
 
                if new_g < g_cost.get(neighbor, float('inf')):
                    g_cost[neighbor] = new_g
                    parent[neighbor] = current
                    f = new_g + heuristic[neighbor]
                    pq.put((f, new_g, neighbor))
 
    # reconstruct path
    path = []
 
    if goal in visited:
        node = goal
 
        while node != start:
            path.append(node)
            node = parent.get(node)
 
            if node is None:
                return [], expansion_order  
 
        path.append(start)
        path.reverse()
 
    return path, expansion_order