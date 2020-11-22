import P3
import matplotlib.pyplot as plt
import numpy as np

naive_queue =P3.timeit(pqclass=P3.NaivePriorityQueue)
my_queue=P3.timeit(pqclass=P3.HeapPriorityQueue)
python_queue=P3.timeit(pqclass=P3.PythonHeapPriorityQueue)

ns= (10, 20, 50, 100, 200, 500)
plt.figure()

plt.plot(ns,naive_queue,label='Naive Queue', c = 'r')
plt.plot(ns,my_queue,label='My Heap Queue', c= 'g')
plt.plot(ns,python_queue,label='Python Heap Queue',c = 'b')
plt.title('Comparing Elapsed time for Different Priority Queue implementations')
plt.xlabel('Number of Lists Merged')
plt.ylabel(' Elapsed time in seconds')
plt.legend(loc = 'upper center')
plt.show()