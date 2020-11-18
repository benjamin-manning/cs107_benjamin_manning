class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
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
        #end of recursion call
        if node == None:
            return BSTNode(key,val)
        #check if the key is to the right of the node
        elif key > node.key:
            node.right = self._put(node.right, key,val)
            return node
        #check if the key is to the left of the node
        elif key < node.key:
            node.left = self._put(node.left, key,val) 
            return node
        #check if the key is the same as the val
        else:
            #update the value of the node
            node.val = val 
            return node
        #adding to the node size
        node.size = self._size(node.right) +  self._size(node.left) + 1

    def _get(self, node, key):
        #end of recursion call
        if node == None:
            raise KeyError(f"No match for {key}")
        #check if the key is to the right of the node
        elif key > node.key:
            val = self._get(node.right, key)
        #check if the key is to the left of the node
        elif key < node.key:
            val = self._get(node.left, key)
         #check if the key is the same as the val
        else:
            val = node.val
            print(val)
        return val

    @staticmethod
    def _size(node):
        return node.size if node else 0