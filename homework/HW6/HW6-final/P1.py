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

    #removing smalles node
    def _removemin(self, node):
        if node.left == None:
            return node.right
        #recursivelt checking to remove
        node.left = self._removemin(node.left)
        #updating the saize
        node.size = node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    #adding the provided remove function
    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        #check recursive break
        if node == None:
            return None
        #check left
        if key < node.key:
            node.left =  self._remove(node.left, key)
        #check right
        elif key > node.key:
            node.right =  self._remove(node.left, key)
        #check match!
        if key == node.key:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right

            t_new = node
            node.right = self._removemin(t_new.right)
            node.left = t_new.left

            node.size = node.size = 1 + self._size(node.left) + self._size(node.right)
        else:
            raise KeyError(f'{key} was not found')

        return node
        
        

    @staticmethod
    def _size(node):
        return node.size if node else 0

t = BSTTable()
t.put(5, 'a')
t.put(1, 'b')
t.put(2, 'c')
t.put(0, 'd')
#print(t._remove(t._root, 5))
print(t._remove(t._remove(t._root, 5), 1))
#print(t._remove(t._root, 10))