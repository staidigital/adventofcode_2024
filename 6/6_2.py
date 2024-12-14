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

start_r, start_c = get_start()

def check_for_loop():
    r, c = start_r, start_c
    dr, dc = -1, 0
    visited = set()

    while True:
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        if not (0 <= r + dr < num_rows and 0 <= c + dc < num_cols):
            return False
        if grid[r + dr][c + dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc

part2 = 0
for ro in range(num_rows):
    for co in range(num_cols):
        if grid[ro][co] != ".":
            continue
        grid[ro][co] = "#"
        if check_for_loop():
            part2 += 1
        grid[ro][co] = "."

print(f"Part 2: {part2}")
