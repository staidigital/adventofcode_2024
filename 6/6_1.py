import os
path = os.getcwd()

with open(path + "/6/data.txt", "r") as file:
    grid = file.readlines()
    grid = [row.strip("\n") for row in grid]

grid = [list(x) for x in grid]

def get_start():
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "^":
                return (r, c)

num_rows = len(grid)
num_cols = len(grid[0])

r, c = get_start()
row_change, col_change = -1, 0
visited = set()

while True:
    visited.add((r, c))
    if not (0 <= r + row_change < num_rows and 0 <= c + col_change < num_cols):
        break
    if grid[r + row_change][c + col_change] == "#":
        col_change, row_change = -row_change, col_change
    else:
        r += row_change
        c += col_change

print(f"Part 1: {len(visited)}")