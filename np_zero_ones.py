#Task
#You are given the shape of the array in the form of space-separated integers, each integer representing the size of different 
#dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

#Input Format
A single line containing the space-separated integers.

#Sample Input 0
#3 3 3

#Sample Output 0

#[[[0 0 0]
# [0 0 0]
# [0 0 0]]
#
# [[0 0 0]
# [0 0 0]
#  [0 0 0]]

#[[0 0 0]
# [0 0 0]
# [0 0 0]]]
#[[[1 1 1]
# [1 1 1]
#  [1 1 1]]

 #[[1 1 1]
 # [1 1 1]
 # [1 1 1]]

 #[[1 1 1]
 #[1 1 1]
 # [1 1 1]]]


#------------------------------------------------Solution---------------------------------------------------------------------------
import numpy as np

n=list(map(int,input().strip().split(" ")))
#Default type is float
#Output : [[ 0.  0.]] 
#print numpy.zeros((1,2), dtype = numpy.int) Type changes to int
#Output : [[0 0]]
print(np.zeros(n, dtype=np.int))  #n is a list so whatever are the dimensions..2,3 or 2,3,4 etc..will be printed
print(np.ones(n, dtype=np.int))


