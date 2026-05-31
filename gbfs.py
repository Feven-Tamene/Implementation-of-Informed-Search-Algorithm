from queue import PriorityQueue

def greedy_best_first_search(graph, heuristic, start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], start))

    visited = set()
    parent = {}
    expansion_order = []

    while not pq.empty():
        _, current = pq.get()

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
                # set parent when first discovered (important for correct path)
                if neighbor not in parent:
                    parent[neighbor] = current

                pq.put((heuristic[neighbor], neighbor))

    # reconstruct path
    path = []

    if goal in visited:
        node = goal

        # if goal was never reached properly, avoid crash
        while node != start:
            path.append(node)
            node = parent.get(node)

            if node is None:
                return [], expansion_order  # safety fallback

        path.append(start)
        path.reverse()

    return path, expansion_order
