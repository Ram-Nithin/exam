def is_valid(graph, vertex, color, colors):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True

def csp_backtracking(graph, colors, assigned_colors, vertex=0):
    if vertex == len(graph):
        return True

    for color in colors:
        if is_valid(graph, vertex, color, assigned_colors):
            assigned_colors[vertex] = color
            if csp_backtracking(graph, colors, assigned_colors, vertex + 1):
                return True
            assigned_colors[vertex] = None
    
    return False

def map_coloring(graph, colors):
    assigned_colors = [None] * len(graph)
    if csp_backtracking(graph, colors, assigned_colors):
        return assigned_colors
    else:
        return None


graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 3],
        3: [0, 2]
    }
    
colors = ['Red', 'Green', 'Blue']
    
solution = map_coloring(graph, colors)
if solution:
        print("Solution exists: Following are the assigned colors")
        for vertex, color in enumerate(solution):
            print(f"Vertex {vertex} --->  {color}")
else:
        print("No solution exists")
