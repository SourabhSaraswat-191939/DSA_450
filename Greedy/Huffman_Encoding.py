# import queue

# class Node:
#     def __init__(self,key):
#         self.left = None
#         self.right = None
#         self.data = key

# class Solution:
#     def huffmanCodes(self,S,f,N):
#         # Code here
#         q = queue.PriorityQueue()
#         # creating min-heap
#         count=0
#         for i in range(N):
#             node = Node(f[i])
#             q.put([f[i],count,node])
#             count+=1
        
#         root = None
        
#         while not q.empty():
#             left = q.get()
#             right = q.get()
#             parent = Node(left[2].data+right[2].data)
#             parent.left = left[2]
#             parent.right = right[2]
#             if q.empty():
#                 root=parent
#                 break
#             q.put([parent.data,count,parent])
#             count+=1
        
#         result = []
#         def preOrder(root, ans):
#             if root is None:
#                 return result.append(ans[:-1])
#             preOrder(root.left,ans+'0')
#             if root.left is not None:
#                 preOrder(root.right,ans+'1')
        
#         preOrder(root,'')
#         return result
# #{ 
# #  Driver Code Starts
# #Initial Template for Python 3


# if __name__ == '__main__':
# 	t=int(input())
# 	for i in range(t):
# 		S= input()
# 		N= len(S);
# 		f= [int(x) for x in input().split()]
# 		ob = Solution()
# 		ans = ob.huffmanCodes(S,f,N)
# 		for i in ans:
# 		    print(i, end = " ")
#         # print()
# # } Driver Code Ends



# a="qwertyuiopasdfghjklzxcvbn"
# r= list(map(int,input().split()))
# # 8 9 14 19 20 21 21 25 33 45 50 50 66 68 70 73 74 75 76 82 85 90 94 97 100
# result = ''
# for i in range(len(r)):
#     for j in range(r[i]):
#         result+=a[i]

# print(result)