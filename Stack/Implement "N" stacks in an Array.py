class stack:
    def __init__(self,k,n) -> None:
        self.k = k  # number of stack
        self.n = n  # size of array
        self.arr = [None]*self.n
        self.top = [-1]*self.k
        self.next = [i+1 for i in range(self.n)]
        self.free = 0
    
    def isFull(self):
        return self.free==-1
    def isEmpty(self,stack):
        return self.top[stack]==-1

    def push(self,val,stack):
        if self.isFull():
            print("Stack Overflow")
            return

        insert_at = self.free
        self.free = self.next[self.free]
        self.arr[insert_at] = val
        self.next[insert_at] = self.top[stack]
        self.top[stack] = insert_at

    def pop(self,stack):
        pop_at = self.top[stack]
        popped = self.arr[pop_at]
        self.top[stack] = self.next[pop_at]
        self.next[pop_at] = self.free
        self.free = pop_at
        return popped


 
# Driver Code
if __name__ == "__main__":
     
    # Create 3 stacks using an
    # array of size 10.
    kstacks = stack(3, 10)
 
    # Push some items onto stack number 2.
    kstacks.push(15, 2)
    kstacks.push(45, 2)
 
    # Push some items onto stack number 1.
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)
 
    # Push some items onto stack number 0.
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)
 
    print("Popped element from stack 2 is " +
                         str(kstacks.pop(2)))
    print("Popped element from stack 1 is " +
                         str(kstacks.pop(1)))
    print("Popped element from stack 0 is " +
                         str(kstacks.pop(0)))
 
    # kstacks.printstack(0)
 
# This code is contributed by Varun Patil
    