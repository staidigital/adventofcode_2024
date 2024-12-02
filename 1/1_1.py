import os, copy
path = os.getcwd()
data = open(path + "/1/data.txt").readlines()
data = [elem.strip("\n") for elem in data]

l1 = [int(elem[0:5]) for elem in data]
l1.sort()
l2 = [int(elem[8:13]) for elem in data]
l2.sort()
distance = 0
for count, elem in enumerate(l1):
    distance += abs(elem-l2[count])

print(distance)