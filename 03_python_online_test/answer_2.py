def findElementIndex(arr, size) : 
    right_sum, left_sum = 0, 0
    
    for i in range(1, size) :
        right_sum += arr[i]
    i, j = 0, 1
 
    while j < size :
        right_sum -= arr[j]
        left_sum += arr[i]
        if left_sum == right_sum :
            return [i + 2]
        j += 1
        i += 1
    return -1
 
if __name__ == "__main__" :
    arr = [1,2,3,10,6]
    n = len(arr)
    print(findElement(arr, n))