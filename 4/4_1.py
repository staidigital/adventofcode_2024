import os
path = os.getcwd()
data = open(path + "/4/data.txt").readlines()
data = [elem.strip("\n") for elem in data]

def is_xmas(text):
    return True if text == "XMAS" else False

def check_horizontal(text):
    xmas_count = 0
    reverse_text = text[::-1]
    for i, char in enumerate(text):
        if i < len(text) - 3:
            if is_xmas(text[i:i+4]):
                xmas_count += 1
            if is_xmas(reverse_text[i:i+4]):
                xmas_count += 1
    return xmas_count

def check_vertical(l):
    xmas_count = 0
    transposed_list = transpose_list(l)
    for text in transposed_list:
        xmas_count += check_horizontal(text)
    return xmas_count

def transpose_list(l):
    transposed_list = ["" for i in range(len(l))]
    for i, elem in enumerate(l):
        for j, char in enumerate(elem):
            transposed_list[j] += char
    return transposed_list
def reverse_list(l):
    reversed_list = [elem[::-1] for elem in l]
    return reversed_list

def check_diagonally(l):
    diag_xmas_count = 0
    transposed_list, reversed_list, transposed_reversed_list = [elem for elem in l], [elem for elem in l], [elem for elem in l]
    transposed_list = transpose_list(transposed_list)
    reversed_list = reverse_list(reversed_list)
    transposed_reversed_list = transpose_list(reverse_list(transposed_reversed_list))
    all_diags_list = []
    all_diags_list += horizontalize_list(l)
    horizontalized_transposed_list = horizontalize_list(transposed_list)
    horizontalized_transposed_list.pop(0)
    all_diags_list += horizontalized_transposed_list
    all_diags_list += horizontalize_list(reversed_list)
    horizontalized_transposed_reversed_list = horizontalize_list(transposed_reversed_list)
    horizontalized_transposed_reversed_list.pop(0)
    all_diags_list += horizontalized_transposed_reversed_list
    for text in all_diags_list:
        diag_xmas_count += check_horizontal(text)
    return diag_xmas_count

def horizontalize_list(l):
    horizontalized_list = ["" for i in range(len(l[0]))]
    for i, text in enumerate(l):
        for j, char in enumerate(text):
            if j+i == len(text):
                break
            horizontalized_list[j]+=text[j+i]
    return horizontalized_list

total_xmas_count = 0
for text in data:
    total_xmas_count += check_horizontal(text)
total_xmas_count += check_vertical(data)
total_xmas_count += check_diagonally(data)
print(total_xmas_count)