import sys
sys.setrecursionlimit(40000)
import os
path = os.getcwd()
data = open(path + "/6/data.txt")
data = [row.strip("\n") for row in data]

guard = {
    "row": 0,
    "col": 0, 
    "direction": "up",
    "visited": []}
for r,row in enumerate(data):
    for c,char in enumerate(row):
        if char == "^":
            guard["row"] = r
            guard["col"] = c

def solve_path(guard, data):
    current_position_string = str(guard["row"]) + " " + str(guard["col"])
    guard["visited"].append(current_position_string)
    if guard["direction"] == "up":
        if data[guard["row"]-1][guard["col"]] == ".":
            row_above = list(data[guard["row"]-1])
            current_row = list(data[guard["row"]])
            row_above[guard["col"]] = "^"
            current_row[guard["col"]] = "."
            data[guard["row"]-1] = "".join(row_above)
            data[guard["row"]] = "".join(current_row)
            guard["row"] -= 1
            if guard["row"] == 0:
                current_position_string = str(guard["row"]) + " " + str(guard["col"])
                guard["visited"].append(current_position_string)
                return guard
            elif data[guard["row"]-1][guard["col"]] == "#":
                guard["direction"] = "right"

    elif guard["direction"] == "right":
        if data[guard["row"]][guard["col"]+1] == ".":
            current_row = list(data[guard["row"]])
            current_row[guard["col"]] = "."
            current_row[guard["col"]+1] = "^"
            data[guard["row"]] = "".join(current_row)
            guard["col"] += 1
            if guard["col"] == len(data[0])-1:
                current_position_string = str(guard["row"]) + " " + str(guard["col"])
                guard["visited"].append(current_position_string)
                return guard
            if data[guard["row"]][guard["col"]+1] == "#":
                guard["direction"] = "down"

    elif guard["direction"] == "down":
        if data[guard["row"]+1][guard["col"]] == ".":
            row_below = list(data[guard["row"]+1])
            current_row = list(data[guard["row"]])
            row_below[guard["col"]] = "^"
            current_row[guard["col"]] = "."
            data[guard["row"]+1] = "".join(row_below)
            data[guard["row"]] = "".join(current_row)
            guard["row"] += 1
            if guard["row"] == len(data)-1:
                current_position_string = str(guard["row"]) + " " + str(guard["col"])
                guard["visited"].append(current_position_string)
                return guard
            if data[guard["row"]+1][guard["col"]] == "#":
                guard["direction"] = "left"
    
    elif guard["direction"] == "left":
        if data[guard["row"]][guard["col"]-1] == ".":
            current_row = list(data[guard["row"]])
            current_row[guard["col"]] = "."
            current_row[guard["col"]-1] = "^"
            data[guard["row"]] = "".join(current_row)
            guard["col"] -= 1
            if guard["col"] == 0:
                current_position_string = str(guard["row"]) + " " + str(guard["col"])
                guard["visited"].append(current_position_string)
                return guard
            if data[guard["row"]][guard["col"]-1] == "#":
                guard["direction"] = "up"
                
    return solve_path(guard, data)

fin_gaurd = solve_path(guard,data)
print(len(set(fin_gaurd["visited"])))



