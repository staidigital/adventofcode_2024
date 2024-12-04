import os
path = os.getcwd()
data = open("test.txt").readlines()
data = [elem.strip("\n") for elem in data]

#comming soon