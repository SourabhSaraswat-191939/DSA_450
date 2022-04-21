#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        if first==None:
            return second
        if second==None:
            return first
        def reverse(head):
            prev=None
            count = 1
            while head.next!=None:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
                count+=1
            head.next=prev
            return head,count
            
        first,fc = reverse(first)
        second,sc = reverse(second)
        carry=0
    
        final = first if fc>=sc else second
        result = final
        for _ in range(min(fc,sc)):
            res = first.data+second.data+carry
            carry = int(res/10)
            final.data = int(res%10)
            first=first.next
            second=second.next
            if (final.next==None) and carry:
                final.next = Node(carry)
                carry=0

            final=final.next
        
        # printList(result)        
        if carry:
            res = (final.data+carry)
            final.data = res%10
            while int(res/10):
                if final.next==None:
                    # print("yes",final.data)
                    res = (final.data+int(res/10))
                    # final.data = res%10
                    # print("yes",final.data,res)
                    if res:
                        final.next = Node(int(res))
                        break
                        
                final=final.next
                res = (final.data+int(res/10))
                final.data = res%10
                
                

        result,rc = reverse(result)
        
                
        return result
            
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends