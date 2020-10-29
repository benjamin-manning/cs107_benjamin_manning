class Fibonacci:
    def __init__(self, terms):
        self.terms = terms # length 
        self.fib_list = [1,2]
        for num in range(terms-2):
            self.fib_list.append(self.fib_list[num]+self.fib_list[num+1])
        
    def __iter__(self):
        return FibonacciIterator(self.fib_list)
        
    def __repr__(self):
        return 'Fibonacci(%s)' % reprlib.repr(self.terms)

class FibonacciIterator:
    def __init__(self, fib_list): 
        self.fib_list = fib_list
        self.index = 0

    def __next__(self): 
        try:
            terms = self.fib_list[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return terms

    def __iter__(self):
        return self # Allows iterators to be used where an iterable is expected

fib = Fibonacci(10)
list(iter(fib))