#stack code 

#Define Node object
class Node:
    '''
    A class for the node data structure. 

    Attributes
    -----
    data: value stored in each node
    next: pointer to the next node 
    '''
    def __init__(self, data): #constructor node object to be used for the stack data structure
        self.data = data
        self.next = None

    
#Define Stack Class and functions 
class stack:
    '''
    A class for the stack data structure, based on linked lists. 

    Attributes
    ------
    top : reference to the top of the stack 
    bottom : reference to the bottom of the stack
    size : int
        number of elements in the stack 

    Methods 
    ------
    push(data)
    pop()
    peek()
    is_empty()
    getSize()
    printStack()
    '''
    def __init__(self): #default constructor for stack
        self.top = None
        self.bottom = None
        self.size = 0
    
    def push(self,data): 
        '''
        Adds defined data to the top of the stack.
            
            Parameters:
                data: value to be pushed on the top of the stack. 
        '''
        if(self.is_empty()):
            self.top = Node(data)
            self.bottom = self.top
            self.size += 1
        else:
            newNode = Node(data)
            newNode.next = self.top
            self.top = newNode
            self.size += 1

    def pop(self):
        '''
        Pops the element at the top of the stack, and returns that element. Throws an exception if popping from an empty stack. 
        '''
        if(self.is_empty()):
            raise Exception("Stack is empty. You cannot pop.")
        else:
            if(self.top == self.bottom):
                tNode = self.top
                self.top = None
                self.bottom = None
                self.size -= 1
                return tNode
            else:
                tNode = self.top
                nextNode = self.top.next
                self.top = None
                self.top = nextNode
                self.size -= 1
                return tNode

    def peek(self):
        '''
        Return a reference to the element at the top of the stack. Throws an exception if peeking an empty stack. 
        '''
        if(self.is_empty()):
            raise Exception("Stack is empty. You cannot peek.")
        else:
            return self.top

    def is_empty(self):
        '''
        Returns True if a stack is empty. Returns False if a stack contains elements. 
        '''
        if (self.top == None):
            return True
        else:
            return False 

    def getSize(self):
        '''
        Returns the number of elements in the stack. 
        '''
        return self.size


    def printStack(self):
        '''
        Prints the stack, starting from the top of the stack. 
        '''
        nextNode = self.top
        while(nextNode != None):
            print(nextNode.data)
            nextNode = nextNode.next

    