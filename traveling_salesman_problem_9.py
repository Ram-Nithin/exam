import itertools

def calculate_distance(graph, path):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    distance += graph[path[-1]][path[0]]  # return to the starting point
    return distance

def traveling_salesman(graph):
    vertices = list(graph.keys())
    min_path = None
    min_distance = float('inf')

    for perm in itertools.permutations(vertices):
        current_distance = calculate_distance(graph, perm)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = perm

    return min_path, min_distance

# Example usage
if __name__ == "__main__":
    graph = {
        0: {1: 10, 2: 15, 3: 20},
        1: {0: 10, 2: 35, 3: 25},
        2: {0: 15, 1: 35, 3: 30},
        3: {0: 20, 1: 25, 2: 30},
    }

    path, distance = traveling_salesman(graph)
    print("Shortest path:", path)
    print("Minimum distance:", distance)
