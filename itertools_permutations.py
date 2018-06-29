#This returns r length permutations of elements in an iterable.
#If r is not specified or is None, then  defaults to the length of the iterable, 
#and all possible full length permutations are generated.
#So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
#itertools.permutations(iterable[, r])

#import permulation module
from itertools import permutations

#split string
word, permsize=[x for x in input().split()]

#another way
#mystr= [x for x in input().split()]
#word=mystr[0]
#permsize=int(mystr[1])

#create permutation for sorted word
x=list(permutations(sorted(word), int(permsize)))

#print all individual combinations
[print(*i,sep="") for i in x]

