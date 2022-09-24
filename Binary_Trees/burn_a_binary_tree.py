#User function Template for python3
from collections import deque
class Solution:
    def ifNodeExists(self,node, key):
     
        if (node == None):
            return False
     
        if (node.data == key):
            return node
     
        """ then recur on left subtree """
        res1 = self.ifNodeExists(node.left, key)
        # node found, no need to look further
        if res1:
            return res1
     
        """ node is not found in left,
        so recur on right subtree """
        res2 = self.ifNodeExists(node.right, key)
     
        return res2
     
    def minTime(self, root,target):
        q = deque()
        visited = set()
        parent = {root:root}
        q.append(root)
        time = 0
        target = self.ifNodeExists(root,target)
        while len(q)!=0:
            pop = q.popleft()
            if pop.left is not None:
                parent[pop.left] = pop
                q.append(pop.left)
                
            if pop.right is not None:
                parent[pop.right] = pop
                q.append(pop.right)
                
        q = deque()
        
        # print(parent)
        q.append(target)
        while len(q)!=0:
            f = 0
            # print("yes")
            for i in range(len(q)):
                pop = q.popleft()
                # print(pop)
                if parent[pop] not in visited:
                    f = 1
                    visited.add(parent[pop])
                    q.append(parent[pop])
                if pop.left is not None and pop.left not in visited:
                    f = 1
                    visited.add(pop.left)
                    q.append(pop.left)
                if pop.right is not None and pop.right not in visited:
                    f = 1
                    visited.add(pop.right)
                    q.append(pop.right)
            if f:
                time+=1
        
        return time
                
                
                
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    line=input()
    target=int(input())
    root=buildTree(line)
    print(Solution().minTime(root,target))

# } Driver Code Ends