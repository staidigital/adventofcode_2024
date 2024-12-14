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
    "visited": [],
    "loop_positions": 0}
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
            else:
                check_row = data[guard["row"]]
                for i in range(guard["col"]+1,len(check_row)):
                    if str(guard["row"]) + " " + str(i) in guard["visited"]:
                        if check_row[i+1] == "#":
                            guard["loop_positions"] += 1
                            break

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
            else:
                check_row = ""
                for i in range(len(data)):
                    check_row += data[i][guard["col"]]
                for i in range(guard["row"]+1,len(check_row)):
                    if str(i) + " " + str(guard["col"]) in guard["visited"]:
                        if check_row[i+1] == "#":
                            guard["loop_positions"] += 1
                            break

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
            else:
                check_row = data[guard["row"]]
                for i in range(guard["col"] - 1, 0, -1):
                    if str(guard["row"]) + " " + str(i) in guard["visited"]:
                        if check_row[i-1] == "#":
                            guard["loop_positions"] += 1
                            break
    
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
            else:
                check_row = ""
                for i in range(len(data)):
                    check_row += data[i][guard["col"]]
                for i in range(guard["row"]-1, 0, -1):
                    if str(i) + " " + str(guard["col"]) in guard["visited"]:
                        if check_row[i-1] == "#":
                            guard["loop_positions"] += 1
                            break
                
    return solve_path(guard, data)

fin_guard = solve_path(guard,data)
print("Part 1: " + str(len(set(guard["visited"]))))
print("Part 2: " + str(guard["loop_positions"]))


