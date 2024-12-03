import os
path = os.getcwd()
data = open(path + "/3/data.txt").readlines()
data = [elem.strip("\n") for elem in data]

legalvals = "0123456789,"

def find_mul(l):
    mul_total = 0
    for i in range(len(l)-3):
        if l[i:i+4] == "mul(":
            for j in range(20):
                if ")" in l[i:i+j]:
                    possible_mul = l[i:i+j]
                    possible_vals = l[i+4:i+j-1]
                    perform_mul = True
                    for char in possible_vals:
                        if (char not in legalvals):
                            perform_mul = False
                        if "," not in possible_vals:
                            perform_mul = False
                    if perform_mul:
                        nums = possible_vals.split(",")
                        mul_total += int(nums[0])*int(nums[1])
                        break
    return mul_total

mul_total = 0
for l in data:
    mul_total += find_mul(l)
print(mul_total)