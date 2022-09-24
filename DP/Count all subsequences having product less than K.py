def subsProdLTk(Arr, n, k):
    # code here
    def findCount(i, prod):
        if i==n:
            return 0
        take = 0
        if prod*Arr[i] < k:
            take = 1+findCount(i+1, prod*Arr[i])
        return findCount(i+1,prod)+take
        

    return findCount(0,1)


print(subsProdLTk([1, 2, 3, 4],4,10))
print(subsProdLTk([4,8,7,2],4,50))

