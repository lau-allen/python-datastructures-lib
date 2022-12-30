#Linked List Code 

#Define Node object
class Node:
    '''
    A class for the node data structure. 

    Attributes
    -----
    data: value stored in each node
    next: pointer to the next node 
    '''
    def __init__(self, data): #default constructor for Node. Sets Node.next equal to None. 
        self.data = data
        self.next = None
    
#Define Linked List Class with associated functions
class linkedlist:
    '''
    A class for the linked list data structure. 

    Attributes
    ------
    head : reference to the first node or start of the linked list 
    tail : reference to the last node or end of the linked list 

    Methods 
    ------
    insertAtBack(data)
    insertAtFront(data)
    insertAtPos(data,position)
    printList()
    '''
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBack(self,data):
        '''
        Inserts a value to the back of the linkedlist object. 
        
            Parameters: 
                data: value to be inserted at back
        '''
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
        else:
            newNode = Node(data)
            self.tail.next = newNode
            self.tail = newNode
    
    def insertAtFront(self,data):
        '''
        Inserts a value to the front of the linkedlist object. 

            Parameters:
                data: value to be inserted at front 
        '''
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
    
    def insertAtPos(self,data,position):
        '''
        Inserts a value at a specific defined position in the linkedlist object. 

            Parameters:
                data: value to be inserted at position
                position: specific position, starting at the linkedlist head, where data should be inserted
        '''
        nextNode = self.head
        curPos = 1
        while(nextNode != None):
            if (position <= 0):
                self.insertAtFront(data)
                break
            elif (nextNode == self.tail or curPos > position):
                self.insertAtBack(data)
                break
            elif curPos == position:
                newNode = Node(data)
                newNode.next = nextNode.next
                nextNode.next = newNode
                break
            else:
                nextNode = nextNode.next
                curPos += 1

    def printList(self):
        '''
        Prints the contents of the linkedlist, starting at the head. 
        '''
        nextNode = self.head
        while(nextNode != None):
            print(nextNode.data)
            nextNode = nextNode.next