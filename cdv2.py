from itertools import combinations as c
def colinear(points):
  a1 = points[0][0]
  a2 = points[1][0]
  a3 = points[2][0]
  b1 = points[0][1]
  b2 = points[1][1]
  b3 = points[2][1]
  disc = a1*(b2-b3)-a2*(b1-b3)+a3*(b1-b2)
  print(disc)
  if(disc == 0): 
    return True
  return False

n = int(input())
i=0
pts = []
while i<n:
  point= list(map(int,input().split()))
  pts.append(point)
  i+=1
  
NoOfSides = 0
l = list(c(pts,3))
for i in l:
    if(colinear(i)):NoOfSides+=1
    # print(NoOfSides)
print(n-NoOfSides)