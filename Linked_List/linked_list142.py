#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        arr = []
        while head:
            arr.append(head)
            if head.next==None:
                break
            head = head.next
        
        valToInc = head
        valToInc.data+=1
        n=len(arr)-1
        newHead = None
        while valToInc.data>9:
            valToInc.data=0
            if n==0:
                newHead = Node(1)
                newHead.next = arr[0]
                break
            
            n-=1
            valToInc = arr[n]
            valToInc.data +=1
        
        if newHead!=None:
            check = newHead
            return check
        return arr[0]


        # # Solution 2 (Recursive) => Space (O(1)) and time (O(n))    
        # # can have recursive depth limit issue.
        # def addRecursive(head):
        #     if head==None:
        #         return 1
                
        #     result = head.data + addRecursive(head.next)
        #     head.data = int(result%10)
            
        #     return int(result/10)
        
        # carry = addRecursive(head)
        # if carry!=0:
        #     newHead = Node(carry)
        #     newHead.next = head
        #     head = newHead
        
        # return head
            
            
        #{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends