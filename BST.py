class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        
    def insertNode(self,data,node):
        if data < node.data:
            if node.leftChild : 
                self.insertNode(data,node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild = Node(data)
    
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insertNode(data,self.root)
    
    def getMin(self,node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        else:
            return node.data
            
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
        else:
            return 0
        
    def getMax(self,node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        else:
            return node.data
        
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
        else:
            return 0
    
    def traverse(self):
        answer = int(input("Please type 1 for InOrder \nPlease type 2 for PostOrder \nPlease type 3 for PreOrder\n"))
        if self.root:
            if answer == 1:
                self.InOrder(self.root)
            elif answer == 2:
                self.PostOrder(self.root)
            elif answer == 3:
                self.PreOrder(self.root)
        else:
            print("No root!\n")
    
    def InOrder(self,node):
        if node.leftChild:
            self.InOrder(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.InOrder(node.rightChild)
            
    def PreOrder(self,node):
        print(node.data)
        if node.leftChild:
            self.PreOrder(node.leftChild)
        if node.rightChild:
            self.PreOrder(node.rightChild)
            
    def PostOrder(self,node):
        if node.leftChild:
            self.PostOrder(node.leftChild)
        if node.rightChild:
            self.PostOrder(node.rightChild)
        print(node.data)
        
    def remove(self,data):
        if self.root is None:
            return None
        else:
            self.root = self.remove_node(data,self.root)
            
    def remove_node(self,data,node):
        if node is None:
            return node
        if data < node.data:
            node.leftChild = self.remove_node(data,node.leftChild)
            return node
        elif data > node.data:
            node.rightChild = self.remove_node(data,node.rightChild)
            return node
        else:
            if node.leftChild is None and node.rightChild is None:
                print("Removing node which has no left and right Child....")
                del node
                return None
            elif node.leftChild is None:
                print("Removing node which has no left Child...")
                tempNode = node.rightChild
                del node
                return tempNode
            elif node.rightChild is None:
                print("Removing node which has no right Child...")
                tempNode = node.leftChild
                del node
                return tempNode
            print("Removing a node which has both left and right Child...")
            print("Getting the predecessor...")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.remove_node(tempNode.data,node.leftChild)
            return node
            
    def getPredecessor(self,node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node
        
        
                
    
BST = BinarySearchTree()

BST.insert(4)
BST.insert(2)
BST.insert(1)
BST.insert(3)
BST.insert(6)
BST.insert(5)
BST.insert(7)

BST.remove(4)

BST.traverse()
    
        
    
           