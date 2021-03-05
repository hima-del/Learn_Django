from functools import reduce

def add(x,y):
    return x+y

dataList = [2,4,7,3]
print(reduce(add,dataList))
