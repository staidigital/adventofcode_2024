import os, copy
path = os.getcwd()
data = open(path + "/1/data.txt").readlines()
data = [elem.strip("\n") for elem in data]

l1 = [int(elem[0:5]) for elem in data]
l2 = [int(elem[8:13]) for elem in data]
total_score = 0
for elem in l1:
    score = 0
    for num in l2:
        if elem == num:
            score += elem
    total_score += score

print(total_score)