#Queue code 

#Define Node object
class Node:
    '''
    A class for the node data structure. 

    Attributes
    -----
    data: value stored in each node
    next: pointer to the next node 
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

    
#Define Stack Class, implemented using Linked Lists
class queue:
    '''
    A class for the queue data structure, based on linked lists. 

    Attributes
    ------
    front : reference to the front of the queue 
    back : reference to the bottom of the queue
    size : int
        number of elements in the queue 

    Methods 
    ------
    enqueue(data)
    dequeue(data)
    printQueue()
    peek()
    getSize()
    '''

    def __init__(self): #default constructor for queue 
        self.front = None
        self.back = None
        self.size = 0
    
    def is_empty(self):
        '''
        Returns True if the queue is empty. Returns False if the queue contains elements.
        '''
        if (self.front == None):
            return True
        else:
            return False 
    
    def enqueue(self,data):
        '''
        Adds defined data to the back of the queue. 

            Parameters:
                data: value to be enqueued in the queue. 
        '''
        if(self.is_empty()):
            self.front = Node(data)
            self.back = self.front
            self.size +=1
        else:
            newNode = Node(data)
            self.back.next = newNode
            self.back = newNode
            self.size += 1

    def printQueue(self):
        '''
        Prints the contents of the queue. 
        '''
        nextNode = self.front
        while(nextNode != None):
            print(nextNode.data)
            nextNode = nextNode.next

    def dequeue(self):
        '''
        Removes the element at the front of the queue. Throws an exception if dequeue is used on an empty queue. 

            Parameters:
                data: value to be dequeued in the queue.        
        '''
        if(self.is_empty()):
            raise Exception("Queue is empty. You cannot dequeue.")
        else:
            if(self.front == self.back):
                tNode = self.front
                self.front = None
                self.back = None
                self.size -= 1
                return tNode
            else:
                tNode = self.front
                nextNode = self.front.next
                self.front = None
                self.front = nextNode
                self.size -= 1
                return tNode

    def peek(self):
        '''
        Returns a reference to the front of the queue. Throws an exception if peek is used on an empty queue. 
        '''
        if(self.is_empty()):
            raise Exception("Queue is empty. You cannot peek.")
        else:
            return self.front

    def getSize(self):
        return self.size