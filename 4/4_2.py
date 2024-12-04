import os
path = os.getcwd()
data = open(path + "/4/data.txt").readlines()
data = [elem.strip("\n") for elem in data]

#comming soon
def is_xmas(matrix):
    diag1 = matrix[0][0]+matrix[1][1]+matrix[2][2]
    diag2 = matrix[2][2]+matrix[1][1]+matrix[0][0]
    diag3 = matrix[0][2]+matrix[1][1]+matrix[2][0]
    diag4 = matrix[2][0]+matrix[1][1]+matrix[0][2]
    diags = [diag1, diag2, diag3, diag4]
    mas_count = 0
    for text in diags:
        if text == "MAS":
            mas_count += 1
    if mas_count == 2:
        return True
    else: 
        return False
    
def traverse_data(data):
    xmas_count = 0
    for i in range(1,len(data)-1):
        for j in range(1, len(data[0])-1):
            if data[i][j] == "A":
                matrix = [data[i-1][j-1:j+2],data[i][j-1:j+2],data[i+1][j-1:j+2]]
                if is_xmas(matrix):
                    xmas_count+=1
    return xmas_count
print(traverse_data(data))
