# Find the Union and Intersection of the two sorted arrays.

def doUnion(a,n,b,m):
    result = set(a)
    return len(result.union(b))

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
doUnion(a,n,b,m)