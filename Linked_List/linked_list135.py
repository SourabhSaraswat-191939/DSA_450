# Reverse a Linked List in group of Given Size. [Very Imp]

"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self,head, k):
        # Code here
        newHead = None
        startF = None
        startS = None
        startBool = True
        prev = None
        nex = None
        count=0
        headCount = 1
        
        while head is not None:
            if headCount==k:
                newHead=head
            if count==0:
                if startBool:
                    startF=head
                    print("sf",startF.data)
        
                else:
                    startS=head
                    print("ss",startS.data)
                prev=None
                startBool= not startBool
                print("arrived",startBool)

                    
            nex = head.next
            head.next = prev
            prev = head
            head = nex
            count+=1
            headCount+=1
            if count==k:
                if startBool and startF!=None:
                    startF.next = prev
                elif not startBool and startS!=None:
                    startS.next = prev
                count=0
        
        if startBool and startF!=None:
            startF.next = prev
        elif not startBool and startS!=None:
            startS.next = prev
        
        return newHead

#{ 
#  Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    llist = LinkedList()
    n = input()
    values = list(map(int, input().split()))
    for i in reversed(values):
        llist.push(i)
    k = int(input())
    new_head = LinkedList()
    ob=Solution()
    new_head = ob.reverse(llist.head, k)
    llist.head = new_head
    llist.printList()
    

# 8
# 1 2 2 4 5 6 7 8
# 4


# } Driver Code Ends