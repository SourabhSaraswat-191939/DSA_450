import itertools
from itertools import combinations, chain

n= int(input())
find = tuple(input().split(','))
groups = list(input().strip().split(','))
result = [()]
total = 0
for gr in groups:
    total += len(gr)

result = []
rank=0
count = 0
done =False
for i in range(1,total+1):
    if done:
        break
    output = list(itertools.combinations(groups,i))
    # print(output)
    try:
        rank = count+output.index(find)+1
        done=True
        
    except:
        count +=len(output)
    # print(result)
    output.clear()

# print(result)
# try:
#     rank = result.index(find)+2
# except:
#     rank = 1
print(rank+1)
