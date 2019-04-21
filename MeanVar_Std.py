'''
Task

You are given a 2-D array of size X. 
Your task is to find:
The mean along axis 1 
The var along axis 0
The std along axis none

Input Format:
The first line contains the space separated values of N and M . 
The next N lines contains M space separated integers.

Output Format:
First, print the mean. 
Second, print the var. 
Third, print the std.

'''



import numpy
my_array=[]
rows, cols=input().split(" ")
for i in range(int(rows)):
        num=input()
        x,y=num.split(" ")
        my_array.append([float(x),float(y)]) 
        #numpy array cannot append so make a list and then convert it to np array
my_array=numpy.array(my_array)
#numpy.set_printoptions(legacy='1.13')
numpy.set_printoptions(sign=' ')
print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))
print(round((numpy.std(my_array)),12))



