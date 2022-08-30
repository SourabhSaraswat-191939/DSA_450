#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r):
        L = arr[l:m]
        R = arr[m:r]
        i=j=k=0
        while i<len(L) and j<len(R):
            if arr[i]>arr[j]:
                arr[k]=arr[j]
                i+=1
            else:
                arr[k]=arr[i]
                j+=1
            k+=1
            
        while i<len(L):
            arr[k]=arr[i]
            k+=1
            i+=1
        while j<len(R):
            arr[k]=arr[j]
            k+=1
            j+=1
        
        # code here
    def mergeSort(self,arr, l, r):
        #code here
        print(l,r)
        if (r-l)>1:
            m = (r-l)//2
            print("arrived",l,m,r)
            self.mergeSort(arr,l,m)
            self.mergeSort(arr,m,r)
             
            self.merge(arr,l,m,r)


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends