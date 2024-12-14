import os
path = os.getcwd()
from itertools import combinations

with open(path + "/8/data.txt", "r") as file:
    grid = file.readlines()
    grid = [row.strip("\n") for row in grid]

grid = [list(row) for row in grid]
max_rows = len(grid)
max_cols = len(grid[0])

def find_signals(grid):
    signals = []
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col != ".":
                signals.append([col, r, c])
    return signals

def sort_signals(signals):
    onetypelist = [[] for s in signals]
    used_signals = ""
    for s, signal in enumerate(signals):
        if s == len(signals) - 1:
            return [lst for lst in onetypelist if len(lst)!=0]
        current_signal = signal[0]
        if current_signal in used_signals:
            continue
        else:
            onetypelist[s].append(signal)
        for i in range(s+1, len(signals)):
            if signals[i][0] == current_signal:
                onetypelist[s].append(signals[i])
                used_signals += current_signal
    return [lst for lst in onetypelist if len(lst)!=0]

def get_antinodes(sorted_signals):
    antinodes = set()

    for lst in sorted_signals:
        for (char1, row1, col1), (char2, row2, col2) in combinations(lst, 2):
            dx = col2 - col1
            dy = row2 - row1
            
            antinodes.add((row1, col1))
            antinodes.add((row2, col2))

            temp_row, temp_col = row1, col1
            while 0 <= temp_row - dy < max_rows and 0 <= temp_col - dx < max_cols:
                temp_row -= dy
                temp_col -= dx
                antinodes.add((temp_row, temp_col))
            
            temp_row, temp_col = row2, col2
            while 0 <= temp_row + dy < max_rows and 0 <= temp_col + dx < max_cols:
                temp_row += dy
                temp_col += dx
                antinodes.add((temp_row, temp_col))

    return antinodes

signals = find_signals(grid)
sorted_signals = sort_signals(signals)

antinodes = get_antinodes(sorted_signals)

legal_antinodes = {(r, c) for r, c in antinodes if 0 <= r < max_rows and 0 <= c < max_cols}

print(f"Part 2: There are {len(legal_antinodes)} unique antinode locations")