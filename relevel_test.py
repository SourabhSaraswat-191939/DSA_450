# n,m=map(int,input().split())
# p = list(map(int,input().split()))

# pSet = set(p)

# i=1
# while True:
#     if m-i not in pSet:
#         print(m-i)
#         break
#     if m+i not in pSet:
#         print(m+i)
#         break

#     i+=1


# print("python program by relevel")
# print("printing the even values")
# length = 10
# for i in range(length):
# \tif i%2==0:
# \t\tprint(i)
# print("program ends here")

# print("python program by relevel")
# print("Sum of the counting from 1 to 10")
# length = 10
# i=1
# sum=0
# while i<11:
# \tsum = sum+i
# \tprint("Sum after adding",i,"is",sum)
# \ti+=1

# print("program ends here")


# print("python program by relevel")
# print("Print value if element is present in dictionary.")
# dic = {}
# dic["first"] = 1
# dic["second"] = 2
# if "second" in dic:    
# \tprint("Yes, the element is present in dic")
# \tprint(dic["second"])
# print("program ends here")


# print("Program to find k-th smallest element")
# array = [12, 5, 4, 8, 19]
# N = len(array)
# K = 2
# s = set(array)
# for itr in s:
# \tif K == 1:
# \t\tK -= 1
# \t\tbreak
# \tprint(itr) 

# print("python program by relevel")
# print("Python program to filter list to a list which have no nested empty list inside.")
# list1 = [10, 21, [], 45, [], 93]
# ans = []
# \t\tans.append(val)
# \tif val != []:
# for val in list1:
# print(ans)
# print("python program by relevel ends here")



# print("Python program to replacing all occurrences of substring s1 with new string s2.")
# str="relevel"
# s1="el"
# s2="so"
# s=str.split(s1)
# new_str=""
# for i in s:
# \tif(i==""):
# \t\tnew_str+=i
# \telse:
# \t\tnew_str+=s2
# print(new_str)



# print("python program by relevel")
# print("Python program to copy all elements of one array into other.")
# array = [3,2,3,2,2,4]
# dic = {}
# for val in array:
# \tdic[val]+=1
# \t\tdic[val]=0
# \tif val not in dic:
# print(dic)


# print("python program by relevel")
# print("Python program to check if a value is a palindrome or not.")
# val1 = "level"
# val2 = val1[::-1]
# if val1 == val2:
# \tprint('Not a palindrome')
# else:
# \tprint('Yes, Palindrome')



s = [2,3]
def find(a,bo):    
    if bo:
        return 
    a.pop()
    print(s)
    print(a)
    find(a,True)

find(s,False)
print(s)