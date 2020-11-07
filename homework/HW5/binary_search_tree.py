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
        if node == None:
            return BSTNode(key,val)
        elif key > node.key:
            node.right = self._put(node.right, key,val)
            return node
        elif key < node.key:
            node.left = self._put(node.left, key,val) 
            return node
        else:
            node.val = val 
            return node
        node.size = self._size(node.right) +  self._size(node.left) + 1

    def _get(self, node, key):
        if node == None:
            raise KeyError(f"No match for {key}")
        elif key > node.key:
            val = self._get(node.right, key)
        elif key < node.key:
            val = self._get(node.left, key)
        else:
            val = node.val
            print(val)
        return val

    @staticmethod
    def _size(node):
        return node.size if node else 0

greektoroman = BSTTable()
greektoroman.put('Athena',    'Minerva')
greektoroman.put('Eros',    'Cupid')
greektoroman.put('Aphrodite',   'Venus')
greektoroman.put('Zeus',   'Jupyter')
greektoroman.put('Ares',   'Mars')
greektoroman.get('Zeus')
print(greektoroman)