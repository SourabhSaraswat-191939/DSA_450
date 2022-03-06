arr = [2,3,4,5,6]

# method 1
def method1():
    dummy = []
    for i in range(len(arr)-1,-1,-1):
        dummy.append(arr[i])

    print(dummy)

# method 2
def method2():
    start = 0
    end = len(arr)-1
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1

    print(arr)

def method3():
    print(arr[::-1])

method1()
method3()
method2()