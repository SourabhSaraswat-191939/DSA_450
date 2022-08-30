import functools

C,N = map(int,input().split())
seats = list(map(int,input().split()))
students = []
for i in range(N):
    students.append(list(input().split(',')))
    students[i][1] = float(students[i][1])

def compare(a,b):
    return a[1] > b[1]

def compare2(a,b):
    if a[1]==b[1]:
        return a[0]<b[0]
    return a[1]>b[1]

print(sorted(students, key = lambda x: (-x[0], x[1])))
students.sort(key=functools.cmp_to_key(compare))
students.sort(key=functools.cmp_to_key(compare2))
print(students)
# students.sort(key=lambda x:x[0])
# students.sort(key=lambda x:x[1],reverse=True)

result = []
for i in range(len(students)):
    if seats[int(students[i][2][-1])-1]>0:
        seats[int(students[i][2][-1])-1] -=1
        result.append([students[i][0],students[i][2]])
    elif seats[int(students[i][3][-1])-1]>0:
        seats[int(students[i][3][-1])-1] -=1
        result.append([students[i][0],students[i][3]])
    elif seats[int(students[i][4][-1])-1]>0:
        seats[int(students[i][4][-1])-1] -=1
        result.append([students[i][0],students[i][4]])
    else:
        pass
    
for name in result:
    print(name[0]+' '+name[1])


