#Task
#You are given a space separated list of numbers. Your task is to print a reversed NumPy array with the element type float.

#Input Format
#A single line of input containing space separated numbers.

#Output Format
#Print the reverse NumPy array with type float.

#-----------------------------------------------SOLUTION------------------------------

import numpy

# split get a list based in the delimiter and strip() method removes the white spaces at the end and beginning of a string
arr = input().strip().split(' ') 
result = arrays(arr)
print(result)

def arrays(arr):
    #convert list elements into float
     x= list(map(float, arr))
    #reverse the list
     rev=x[::-1]
    #convert to numpy array
     new=numpy.array(rev)
     return (new)
    
