import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def a_star(graph, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (cost, vertex)
    came_from = {}
    g_score = {vertex: float('inf') for vertex in graph}
    g_score[start] = 0
    f_score = {vertex: float('inf') for vertex in graph}
    f_score[start] = heuristic(start, goal)
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in [i[1] for i in open_list]:
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None  # No path found

# Example usage
if __name__ == "__main__":
    graph = {
        (0, 0): {(1, 0): 1, (0, 1): 1},
        (1, 0): {(1, 1): 1, (0, 0): 1},
        (0, 1): {(1, 1): 1, (0, 0): 1},
        (1, 1): {}
    }
    
    start = (0, 0)
    goal = (1, 1)
    
    path = a_star(graph, start, goal)
    print("Path:", path)
