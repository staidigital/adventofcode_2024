import os
path = os.getcwd()
from itertools import combinations

with open(path + "/8/example.txt", "r") as file:
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

def get_antenna_locations(sorted_signals):
    antennas = []
    for l, lst in enumerate(sorted_signals):
        for (char1, row1, col1), (char2, row2, col2) in combinations(lst, 2):
            if char1 == char2:  
                dx = col2 - col1 
                dy = row2 - row1 
                antenna_one = str(row1-dy) + " " + str(col1-dx)
                antennas.append(antenna_one)
                antenna_two = str(row2 + dy) + " " + str(col2 + dx)
                antennas.append(antenna_two)
    return list(set(antennas))

signals = find_signals(grid)
sorted_signals = sort_signals(signals)
antennas = get_antenna_locations(sorted_signals)
print(antennas)
legal_antenna_locations = 0
legal_antennas = []
for a, antenna in enumerate(antennas):
    ant = antenna.split(" ")
    if 0 <= int(ant[0]) < max_rows and 0 <= int(ant[1]) < max_cols:
        legal_antenna_locations += 1
        legal_antennas.append(antenna)
print(legal_antennas)
print(f"Part 1: There are {legal_antenna_locations} unique antenna locations")