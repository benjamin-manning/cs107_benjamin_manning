from random import sample
from time import time
from P2 import MinHeap
import heapq as h

class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError # TODO

    def get(self):
        raise NotImplementedError # TODO

    def peek(self):
        raise NotImplementedError # TODO

def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists): 
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i)) 

    return merged

def generatelists(n, length=20, dictionary_path='words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed


class NaivePriorityQueue(PriorityQueue):

    def put(self,val):
        #If the queue is full
        if len(self.elements) is self.max_size: raise IndexError('Priority Queue is full')
        #Otherwise add it to the list
        self.elements.append(val)

    def get(self):
        count =- 1
        smallest = None
        if len(self.elements) is 0: raise IndexError('Priority Queue is empty')

        for item in self.elements:
            count+=1
            if (smallest == None):
                smallest = item
                tracker = count
            elif item < smallest:
                smallest = item
                tracker = count
        #delete last element
        del self.elements[tracker]
        return smallest

    def peek(self):
        smallest = None
        if len(self.elements) is 0: raise IndexError('Priority Queue is empty')
        
        for item in self.elements:
            if (smallest is None): 
                smallest = item
            elif item < smallest:
                smallest = item
        return smallest      

class HeapPriorityQueue(PriorityQueue):
    def __init__(self,max_size):
        self.elements = MinHeap([])
        self.max_size = max_size

    def put(self, val):
        if self.elements.size is self.max_size: raise IndexError('Priority Queue is empty')
        #adding the element
        self.elements.heappush(val)

    def get(self):
        if self.elements.size is 0: raise IndexError('Priority Queue is empty')
        #deletes and returns smallest element
        return self.elements.heappop()

    def peek(self):
        if self.elements.size is 0: raise IndexError('Priority Queue is empty')
        #returning smallest element
        return self.elements.elements[0]

#inherit priortiy queue for python
class PythonHeapPriorityQueue(PriorityQueue):
    def __init__(self,max_size):
        self.elements=[]
        self.max_size = max_size

    def put(self, val):
        if len(self.elements) is self.max_size: raise IndexError('Priority Queue is empty')
        #adding value
        h.heappush(self.elements,val)

    def get(self):
        if len(self.elements) is 0: raise IndexError('Empty priority queue')
        #returning and deleting min
        return h.heappop(self.elements)

    def peek(self):
        if len(self.elements) is 0: raise IndexError('Priority Queue is empty')
        #returning min
        return h.nsmallest(1,self.elements)[0]
