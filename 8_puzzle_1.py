import heapq

class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board        # Current board configuration
        self.parent = parent      # Parent state
        self.move = move          # Move made to reach this state
        self.depth = depth        # Depth (g-cost)
        self.cost = cost          # Total cost (f-cost)

    # For priority queue comparison
    def __lt__(self, other):
        return self.cost < other.cost

def manhattan_distance(board, goal):
    distance = 0
    for i in range(1, 9):
        xi, yi = divmod(board.index(i), 3)
        xg, yg = divmod(goal.index(i), 3)
        distance += abs(xi - xg) + abs(yi - yg)
    return distance

def get_neighbors(state):
    neighbors = []
    idx = state.board.index(0)  # Position of the empty space (0)
    x, y = divmod(idx, 3)
    moves = []

    # Possible moves: Up, Down, Left, Right
    if x > 0: moves.append(('Up', idx - 3))
    if x < 2: moves.append(('Down', idx + 3))
    if y > 0: moves.append(('Left', idx - 1))
    if y < 2: moves.append(('Right', idx + 1))

    for move_name, pos in moves:
        new_board = state.board.copy()
        new_board[idx], new_board[pos] = new_board[pos], new_board[idx]
        neighbors.append((move_name, new_board))

    return neighbors

def reconstruct_path(state):
    path = []
    while state.parent is not None:
        path.append(state.move)
        state = state.parent
    return path[::-1]  # Reverse the path

def solve_puzzle(start_board, goal_board):
    open_set = []
    closed_set = set()

    start_state = PuzzleState(
        board=start_board,
        parent=None,
        move=None,
        depth=0,
        cost=manhattan_distance(start_board, goal_board)
    )

    heapq.heappush(open_set, start_state)

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.board == goal_board:
            return reconstruct_path(current_state)

        closed_set.add(tuple(current_state.board))

        for move_name, neighbor_board in get_neighbors(current_state):
            if tuple(neighbor_board) in closed_set:
                continue

            neighbor_state = PuzzleState(
                board=neighbor_board,
                parent=current_state,
                move=move_name,
                depth=current_state.depth + 1,
                cost=current_state.depth + 1 + manhattan_distance(neighbor_board, goal_board)
            )

            heapq.heappush(open_set, neighbor_state)

    return None  # No solution found

def print_board(board):
    for i in range(0, 9, 3):
        print(' '.join(str(num) if num != 0 else ' ' for num in board[i:i+3]))
    print()

if __name__ == "__main__":
    # Define the start and goal states
    start_board = [
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    ]

    goal_board = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 0
    ]

    print("Starting Board:")
    print_board(start_board)

    solution = solve_puzzle(start_board, goal_board)

    if solution:
        print(f"Solution found in {len(solution)} moves:")
        for idx, move in enumerate(solution):
            print(f"Move {idx + 1}: {move}")
    else:
        print("No solution found.")
