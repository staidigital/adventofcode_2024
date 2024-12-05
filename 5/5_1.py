import os
from math import *
path = os.getcwd()
data = open(path + "/5/data.txt").readlines()
data = [elem.strip("\n") for elem in data]

raw_rules = []
updates = []
for i in range(len(data)):
    if data[i] == "":
        raw_rules = data[0:i]
        updates = data[i+1:]
        break

rules = [[] for i in range(100)]
for i, elem in enumerate(raw_rules):
    new_rule = elem.split("|")
    rules[int(new_rule[0])].append(new_rule[1])

def weird_sort(num_list):
    for i, num in enumerate(num_list):
        for j, prev_num in enumerate(num_list[0:i]):
            if prev_num in rules[int(num)]:
                num_list.pop(i)
                num_list.insert(j,num)
                break
    return num_list

total_median = 0
for update in updates:
    update_list = update.split(",")
    sorted_update_list = [elem for elem in update_list]
    sorted_update_list = weird_sort(sorted_update_list)
    if update_list == sorted_update_list:
        total_median += int(update_list[floor(len(update_list)/2)])

print(total_median)