from itertools import permutations

def is_solution_valid(words, solution):
    num_words = len(words)
    int_words = []

    for word in words:
        int_word = 0
        for letter in word:
            int_word = int_word * 10 + solution[letter]
        int_words.append(int_word)

    return sum(int_words[:-1]) == int_words[-1]

def solve_cryptarithmetic(words):
    unique_letters = set("".join(words))
    
    if len(unique_letters) > 10:
        return "Solution is not possible with more than 10 unique letters."

    for perm in permutations(range(10), len(unique_letters)):
        solution = dict(zip(unique_letters, perm))
        
        if any(solution[word[0]] == 0 for word in words):
            continue
        
        if is_solution_valid(words, solution):
            return solution
    
    return "No solution found."

if __name__ == "__main__":
    words = ["SEND", "MORE", "MONEY"]
    solution = solve_cryptarithmetic(words)

    if isinstance(solution, dict):
        print("Solution found:")
        for letter, digit in solution.items():
            print(f"{letter} = {digit}")
    else:
        print(solution)