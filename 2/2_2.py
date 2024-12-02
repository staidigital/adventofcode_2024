import os
path = os.getcwd()
data = open(path + "/2/data.txt").readlines()
data = [elem.strip("\n") for elem in data]
safe_count = 0

def isSafe(l):
    safe = True
    for i, num in enumerate(l):
        if i < len(l)-1 and abs(l[i]-l[i+1]) > 3:
            safe = False
        elif i < len(l)-1 and l[i] == l[i+1]:
            safe = False
    l_sort = [elem for elem in l]
    l_sort.sort()
    l_reverse = [elem for elem in l_sort]
    l_reverse.reverse()
    
    if not (l == l_sort or l == l_reverse):
        safe = False

    if safe:
        return True
    else:
        return False
    
for elem in data:
    l = elem.split(" ")
    l = [int(elem) for elem in l]
    safe = False
    for i in range(len(l)):
        test_l = [elem for elem in l]
        test_l.pop(i)
        if isSafe(test_l):
            safe = True
    if safe:
        safe_count += 1

print(safe_count)