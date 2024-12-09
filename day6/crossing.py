def count_asterisk_crossings(matrix):
    # Convert the matrix into a list of lists
    grid = [list(row) for row in matrix]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    crossings = 0

    # Iterate through the matrix
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == '#':
                # Check adjacent positions
                if (grid[i - 1][j] == '#' and grid[i + 1][j] == '#' and  # Vertical
                        grid[i][j - 1] == '#' and grid[i][j + 1] == '#'):  # Horizontal
                    crossings += 1

    return crossings

def generate_cross_matrix(matrix):
    """
    Generate a new matrix with crossings of '#' added to the original.
    """
    grid = [list(row) for row in matrix]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (grid[i - 1][j] == '#' and grid[i + 1][j] == '#' and  # Vertical
                    grid[i][j - 1] == '#' and grid[i][j + 1] == '#'):
                grid[i][j] = '#'  # Mark the center as a crossing

    return ["".join(row) for row in grid]

# Input matrix
data = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]

# Generate a new matrix with crossings and count them
cross_matrix = generate_cross_matrix(data)
print(cross_matrix)
result = count_asterisk_crossings(cross_matrix)

# Print the resulting matrix and the count
print("Matrix with crossings:")
for row in cross_matrix:
    print(row)

print("Number of asterisk crossings:", result)