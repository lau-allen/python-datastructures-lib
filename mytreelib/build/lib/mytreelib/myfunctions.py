# Trees Code

#Define Node object
class Node:
    '''
    A class for the node data structure. 

    Attributes
    -----
    data: value stored in each node
    left: pointer to the left child node
    right: pointer to the right child node 
    '''
    def __init__(self, data): #default constructor. sets data to data, and the left/right nodes to None 
        self.data = data
        self.left = None
        self.right = None

class BST:
    '''
    A class for the binary search tree data structure.

    Attributes
    ------
    root : reference to the root node of the binary search tree
    size : int
        number of elements in the binary search tree 

    Methods 
    ------
    is_empty()
    add_node(node, data)
    getSize()
    traverse_in_order(node)
    height(node)
    '''   

    def __init__(self): #default constructor. sets the root node equal to none, and the size 0. 
        self.root = None
        self.size = 0

    def is_empty(self):
        '''
        Returns True if the tree is empty. Returns False if the tree contains elements. 
        '''
        if(self.root == None):
            return True
        else:
            return False
    
    def add_node(self,node,data):
        '''
        Adds elements to the binary search tree, ensuring the left children nodes are less than its parent, and right children nodes are more than its parent. 
        
            Parameters:
                node: root node of the tree 
                data: value to be added to the tree
        
        '''
        if (self.is_empty()):
            self.root = Node(data)
            self.size += 1
            return
        
        if (data < node.data):
            if (node.left == None):
                node.left = Node(data)
                self.size += 1
            else:
                self.add_node(node.left,data)
        else:
            if (node.right == None):
                node.right = Node(data)
                self.size += 1
            else:
                self.add_node(node.right,data)
    
    def getSize(self):
        '''
        Returns the size of the tree. 
        '''
        return self.size

    def traverse_in_order(self,node):
        '''
        Prints the elements of the tree in order. 

            Parameters:
                node: root node of the tree. 
        '''
        if (node != None):
            self.traverse_in_order(node.left)
            print(node.data)
            self.traverse_in_order(node.right)
    
    def height(self,node):
        '''
        Returns the height of the tree. 

            Parameters:
                node: root node of the tree

            Return:
                height (int)
        '''
        if (node == None):
            return 0
        else:
            hL = self.height(node.left) + 1
            hR = self.height(node.right) + 1
            if (hL > hR):
                return hL
            else:
                return hR