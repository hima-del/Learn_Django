# filter
ages = [5,12,17,18,45,67,33,86]

def myFunc(x):
    if x<18:
        return False
    else:
        return True

adults = filter(myFunc,ages)

for x in adults:
    print(x)