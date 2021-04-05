def findProcessors(start,stop,n):
    count = 0;
    unfinished = []
    for x in range(n):
        if(x>0):
            prev = stop[x-1]
            if(prev > start[x]):
                unfinished.append(prev)
                count = count + 1
            elif(all(i >= start[x] for i in unfinished)):
                count=count-1    
        else:
            count = count + 1
    print(unfinished)
    return count
if __name__=='__main__':
    start = [900,940,950,1000,1500,1600]
    stop = [910,1020,1010,1015,1620,1700]
    n = len(start)  
    print("minimum number of processors required=",findProcessors(start,stop,n))  