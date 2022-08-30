import math
import itertools

def angle(point):
    vec = [point[0]-origin[0], point[1]-origin[1]]
    lenvec = math.hypot(vec[0], vec[1])
    if lenvec == 0:
        return -math.pi, 0
    normal = [vec[0]/lenvec, vec[1]/lenvec]
    dotprod  = normal[0]*refvec[0] + normal[1]*refvec[1]
    diffprod = refvec[1]*normal[0] - refvec[0]*normal[1]
    angle = math.atan2(diffprod, dotprod)
    if angle < 0:
        return 2*math.pi+angle, lenvec
    return angle, lenvec

def Area(coord):
    n = len(coord)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += coord[i][0] * coord[j][1]
        area -= coord[j][0] * coord[i][1]
    area = abs(area) / 2.0
    return area


N=int(input())
points = []
for _ in range(N):
    a,b = map(int,input().split())
    points.append((a,b))

origin = points[0]
refvec = [0, 1]
init_set_size = 3
max_set_size = len(points)+1
area_list = []

for i in range(init_set_size, max_set_size, 1):
    comb = list(itertools.combinations(points, i))
    for n in comb:
        coord = sorted(n, key=angle)
        area_list.append(Area(coord))

area_list.sort(reverse=True)
print(int(area_list[0]))