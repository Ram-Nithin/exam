class VacuumCleanerState:
    def __init__(self, location, dirt):
        self.location = location  # 'A' or 'B'
        self.dirt = dirt          # {'A': True, 'B': True} or {'A': False, 'B': False}
    
    def is_goal(self):
        return not self.dirt['A'] and not self.dirt['B']
    
    def __str__(self):
        return f"Location: {self.location}, Dirt: {self.dirt}"

def actions(state):
    if state.location == 'A':
        return ['clean', 'move_to_B']
    else:
        return ['clean', 'move_to_A']

def result(state, action):
    new_location = state.location
    new_dirt = state.dirt.copy()
    
    if action == 'clean':
        new_dirt[state.location] = False
    elif action == 'move_to_B':
        new_location = 'B'
    elif action == 'move_to_A':
        new_location = 'A'
    
    return VacuumCleanerState(new_location, new_dirt)

def search():
    initial_state = VacuumCleanerState('A', {'A': True, 'B': True})
    frontier = [(initial_state, [])]
    visited = set()
    
    while frontier:
        state, path = frontier.pop(0)
        
        if state.is_goal():
            return path
        
        visited.add((state.location, tuple(state.dirt.items())))
        
        for action in actions(state):
            new_state = result(state, action)
            if (new_state.location, tuple(new_state.dirt.items())) not in visited:
                frontier.append((new_state, path + [action]))
    
    return None

def solve_vacuum_cleaner_problem():
    solution = search()
    if solution:
        print("Solution found:")
        for step in solution:
            print(step)
    else:
        print("No solution exists")

if __name__ == "__main__":
    solve_vacuum_cleaner_problem()
      