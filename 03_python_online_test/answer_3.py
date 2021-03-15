sentence = str(input("enter the sentence : "))
number = int(input("enter the number : "))
printable = ""
start =0
n = len(sentence)
while start < n :
    result = ""
    for i in sentence[0:number:1]:
        result = result + i
    printable = printable + "\n" + result
    sentence = sentence.replace(result, '')
    start=start+number
print(printable)