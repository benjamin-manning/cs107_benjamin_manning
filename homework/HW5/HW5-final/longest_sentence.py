from linked_list import LinkedList, Nil
import sys 
sys.setrecursionlimit(10**6) 


def get_list_of_sentences(chapter1='swansway-chapter1.txt'):
    def to_sentences(p):
            for delimiter in '.?!': p = p.replace(delimiter, '|')
            return [s.strip('\" ') for s in p.split('|')]
    with open(chapter1, 'r', encoding='UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)

    return list_of_sentences

 
def longest_sentence():
    list_of_sentences = get_list_of_sentences()
    #creating a splitting function
    def splitter(x):
        return len(x.split(' '))
    #count for each
    count = list_of_sentences.for_each(splitter)
    #reducer right for each one
    def reducer(x,y):
        return x if x>y else y
    #update and return the count
    count_update = count.reduce_right(reducer)
    return count_update