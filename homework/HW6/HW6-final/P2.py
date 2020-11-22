from math import floor
from typing import List
class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        #setting element to determine if min or max
        self.min_max='min'
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            # buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size

    def compare(self, a: int, b: int) -> bool:
       
        #if min
        if self.min_max == 'min':
            if a > b:
                return True
            else: 
                return False
        #if max
        else:
            if a < b:
                return True
            else: 
                return False
    

    def heapify(self, idx: int) -> None:
        #check the left side
        if self.left(idx)<self.size and self.compare(self.elements[idx],self.elements[self.left(idx)]):
                self.swap(idx,self.left(idx))
                self.heapify(self.left(idx))
        #check the right side
        if self.right(idx)<self.size and self.compare(self.elements[idx],self.elements[self.right(idx)]):
                self.swap(idx,self.right(idx))
                self.heapify(self.right(idx))

    def build_heap(self) -> None:
        for idx in range((self.size-1)//2,-1,-1):
            self.heapify(idx)

    def heappush(self, key: int) -> None:
        self.elements.append(key)
        self.size += 1
        size_n = self.size-1

        while self.compare(self.elements[self.parent(size_n)],self.elements[size_n]):
            if size_n < 1:
                return
            else:
                self.swap(self.parent(size_n),size_n)
                size_n = self.parent(size_n)


    def heappop(self) -> int:

        pop = self.elements[0]
        self.elements[0]=self.elements[self.size-1]
        self.size = self.size - 1
        self.heapify(0)
        return pop

class MinHeap(Heap):

    def __init__(self, array: List[int]):
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.min_max='min'
        self.build_heap()

class MaxHeap(Heap):

    def __init__(self, array: List[int]):
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.min_max='max'
        self.build_heap()