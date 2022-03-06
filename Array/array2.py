arr = [2,5,7,3,4,9]

# method 1  (Linear Search)
def maxAndMin():  # time complexity -> O(n)
    max = arr[0]
    min = arr[0]
    for num in arr:
        if num>max:
            max = num
        if num<min:
            min = num

    print("Max -> ",max,"Min -> ",min)

# method 2 (Divide and Conquer)
def maxAndMin2(low,high,arr):  # time complexity -> O(n)
    arr_min = arr[low]
    arr_max = arr[high]
    if low==high:
        arr_max = arr[low]
        arr_min = arr[low]
    
    elif high==low+1:
        arr_max = max(arr[low],arr[high])
        arr_min = min(arr[low],arr[high])
    
    else:
        mid = int((low+high)/2)
        arr_max1, arr_min1 = maxAndMin2(low,mid,arr)
        arr_max2, arr_min2 = maxAndMin2(mid+1,high,arr)
        arr_max, arr_min = max(arr_max1,arr_max2), min(arr_min1,arr_min2)

    return (arr_max,arr_min)

maxAndMin()
print(maxAndMin2(0,len(arr)-1,arr))
