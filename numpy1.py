#Task
#You are given a 2-D array with dimensions X. 
#Your task is to perform the min function over axis 1 and then find the max of that.

#Input Format
#The first line of input contains the space separated values of n and m. 
#The next n lines contains m space separated integers.

#Output Format
#Compute the min along axis 1 and then print the max of that result.

#Sample Input
#4 2
#2 5
#3 7
#1 3
#4 0

#Sample Output
#3
#-------------------------------------------------SOLUTION--------------------------------------------------------------

import numpy as np
n,m= map(int,input().split(" "))
minineach_row=[]

for i in range(n):
    x=[int(x) for x in input().split(" ")]
    minineach_row.append(np.min(x))

y=np.max(minineach_row)
print(y)



