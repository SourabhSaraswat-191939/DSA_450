import heapq
arr = list(map(int,input().split()))
k = int(input())
heapq.heapify(arr)
for i in range(k-1):
    heapq.heappop(arr)
    
print(heapq.heappop(arr))