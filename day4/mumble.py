import numpy as np

def search_word(grid, word):
    n, m = grid.shape
    word_len = len(word)
    count = 0

    # Helper to check bounds and match word
    def match(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx, ny] != word[i]:
                return False
        return True

    # Directions: (dx, dy)
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]

    # Iterate through each cell and search in all directions
    for x in range(n):
        for y in range(m):
            for dx, dy in directions:
                if match(x, y, dx, dy):
                    count += 1

    return count


def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(e)
        mapp.append(tmp)

    return mapp

f = open("input.txt", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

matrix = create_matrix(l)
grid = np.array(matrix)

word = "XMAS"
result = search_word(grid, list(word))
print(f"Occurrences of the word '{word}': {result}")