class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))

class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node: 
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    @staticmethod
    def _size(node):
        return node.size if node else 0

    #Adding _removemin
    def _removemin(self,node):
        #Ending Recursive Call
        if node.left is None:
            return node.right
        #rercusively going back to _removemin
        node.left = self._removemin(node.left)
        #updating size
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    #Adding remove Mode
    def remove(self, key):
        self._root = self._remove(self._root, key)
    
    #Adding find min node to make _remove easier
    def _getmin(self,node):
        if node.left is None:
            return node
        node.left = self._min(node.left)

    def _remove(self, node, key):
        #determining recursive stop
        if node is None:
            return None
        #checking if key is smaller
        if key < node.key:
            node.left = self._remove(node.left,key)
        #checkign if key is bigger
        elif key> node.key:
            node.right = self._remove(node.right,key)
        #checking if key is same
        if key == node.key:
            if node.right is None:
                return node.left
            if node.left is  None:
                return node.right
            #making a copy of node
            new_node=node
            #getting smallest
            node=self._getmin(node.right)
            node.right = self._removemin(new_node.right)
            node.left = new_node.left
            node.size = 1 + self._size(node.left) + self._size(node.right)

        else:
            raise KeyError(f'The \'{key}\' key does match.')

        return node

from enum import Enum

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.tree=tree
        self.traversalType=traversalType
        self.values = []
        self.index = 0

        if self.traversalType == DFSTraversalTypes.INORDER:
            self.inorder(self.tree)
        elif self.traversalType == DFSTraversalTypes.PREORDER:
            self.preorder(self.tree)
        elif self.traversalType == DFSTraversalTypes.POSTORDER:
            self.postorder(self.tree)
        else:
            raise Exception('unknown traversal type') 

    def __iter__(self):
        return self
        
    def __next__(self):
        try:
            self.index+=1
            return self.values[self.index-1]

        except IndexError:
            raise StopIteration()

    def inorder(self, bst: BSTTable):
        self._inorder(bst._root)

    #adding hidden in order function to perform inorder (I COULDN'T FIGURE OUT HOW TO DO IT WITHOUT)
    def _inorder(self, node):
        if node is None:
            return None
        self._inorder(node.left)
        self.values.append(node)
        self._inorder(node.right)
        
    def preorder(self, bst: BSTTable):
        node = bst._root
        #check stopping condition
        if node is None:
            return None
        #append the node from the beginng
        self.values.append(node)
        self.preorder(node.left)
        self.preoder(node.right)

    def postorder(self, bst: BSTTable):
        node = bst._root
        #check stopping condition
        if node is None:
            return None
        #checking left
        self._postorder(node.left)
        #checking right
        self._postoder(node.right)
        #adding to list
        self.values.append(node)    