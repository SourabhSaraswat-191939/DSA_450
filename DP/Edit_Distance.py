class Solution:
    def editDistance(self, s, t):
		# Code here
        dp = {}
        def findMinOp(st,t,i,j):
            # if st==t:
            #     return 0
            if i==len(st):
                return len(t)-j
            if j==len(t):
                return len(st)-i-1    
            
            # if len(st)==0:
            #     return len(t)
            if (i,j) in dp:
                return dp[(i,j)]
            
            if st[i]==t[j]:
                dp[(i,j)] = findMinOp(st,t,i+1,j+1)
            else:
                dp[(i,j)] = 1+min(findMinOp(st,t,i,j+1), findMinOp(st,t,i+1,j+1),findMinOp(st,t,i+1,j))
            
            return dp[(i,j)]
            
        return findMinOp(s,t,0,0)
    #{ 
 # Driver Code Starts
if __name__ == '__main__':
	# T=int(input())
	# for i in range(T):
    s, t = input().split()
    ob = Solution()
    ans = ob.editDistance(s, t)
    print(ans)
# } Driver Code Ends