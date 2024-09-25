from collections import deque

# Define the initial state and the goal state
initial_state = (3, 3, 1) 
goal_state = (0, 0, 0)  

# Define possible boat moves
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def is_valid(state):
    m, c, b = state
    m_right = 3 - m
    c_right = 3 - c
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if (m < c and m > 0) or (m_right < c_right and m_right > 0):
        return False
    return True

def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [goal_state]

        m, c, b = current_state
        for move in moves:
            if b == 1:  # Boat is on the left side
                new_state = (m - move[0], c - move[1], 0)
            else:       # Boat is on the right side
                new_state = (m + move[0], c + move[1], 1)

            if is_valid(new_state) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [current_state]))

    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        for step in solution:
            print(step)

if __name__ == "__main__":
    solution = bfs(initial_state, goal_state)
    print_solution(solution)
