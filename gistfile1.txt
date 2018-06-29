#This tool computes the cartesian product of input iterables(list,tuples). 
#It is equivalent to nested for-loops. 
#For example, product(A, B)returns the same as ((x,y) for x in A for y in B).

#import itertools.product
from itertools import product

#split lists into numbers
A= [int(x) for x in input().split()]
B= [int(y) for y in input().split()]

#calculate product
x= (list(product(A,B)))

#split the list again
for i in range(len(x)):
    print(x[i],end=" ")


