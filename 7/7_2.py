import itertools
import os
import re
path = os.getcwd()
data = open(path + "/7/data.txt").readlines()
data = [row.strip("\n") for row in data]

def check_solvability(row):
    operators = ["+", "*", "||"]
    answer, numbers = row.split(":")
    answer = int(answer)
    numbers = numbers[1:].split(" ")
    expressions = generate_expressions(numbers,operators)
    for expression in expressions:
        if evaluate_left_to_right(expression) == answer:
            return answer
    return 0

def generate_expressions(numbers, operators):
    results = []
    for ops in itertools.product(operators, repeat=len(numbers) - 1):
        expression = str(numbers[0])
        for i, op in enumerate(ops):
            expression += f" {op} {numbers[i+1]}"
        results.append(expression)
    return results

def evaluate_left_to_right(expression):
    tokens = re.split(r'(\s[\+\-\*/]|\|\|\s)', expression)
    tokens = [token.strip() for token in tokens]
    result = int(tokens[0])
    i = 1
    while i < len(tokens) - 1:
        operator = tokens[i]
        next_number = int(tokens[i+1])

        if operator == '+':
            result += next_number
        elif operator == '*':
            result *= next_number
        elif operator == '||':
            result = int(str(result) + str(next_number))

        i += 2
    
    return result
    

def find_calibration_sum(lst):
    sum = 0
    for row in lst:
        sum += check_solvability(row)
    return sum
print(check_solvability(data[8]))
print(find_calibration_sum(data))