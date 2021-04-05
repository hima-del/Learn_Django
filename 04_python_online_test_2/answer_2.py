import random
string1 = str(input("enter s1 : "))
string2 = str(input("enter s2 : "))
letter = ["e","f"]
item1 = random.randint(0,1)
item2 = random.randint(0,1)
result1 = string1.find("#")
result2 = string2.find("#")
string1 = string1[:result1]+letter[item1]+string1[result1+1:] 
string2 = string2[:result2]+letter[item2]+string2[result2+1:] 
#print(string1)
#print(string2)
def swap(str):
    if len(str) <= 1:
        return str
 
    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]

def match_function(string1):    
    swappped_value = swap(string1)
    return swappped_value
for i in range(len(string1)):    
    swappped_value = match_function(string1)    
if swappped_value == string2:
    print("MATCH")
else:
    print("DIFFERENT")    

