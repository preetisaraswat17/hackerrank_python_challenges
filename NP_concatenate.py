#Task
#You are given two integer arrays of size N X P and M X P (N & M are rows, and P is the column). Your task is to concatenate the arrays 
#along axis 0.

#Input Format
#The first line contains space separated integers N,M  and P. 
#The next N lines contains the space separated elements of the P columns. 
#After that, the next M lines contains the space separated elements of the P columns.

#Sample Input
#4 3 2
#1 2
#1 2 
#1 2
#1 2
#3 4
#3 4
#3 4 

#Sample Output
#[[1 2]
#[1 2]
#[1 2]
#[1 2]
#[3 4]
# [3 4]
 #[3 4]] 

#--------------------------------------------SOLUTION-------------------------------------------------------------------------------
import numpy as np
n, m, p = map(int, input().strip().split())
l1=list()
l2=list()
for _ in range(n):
    x,y=map(int, input().strip().split())
    l1.append((x,y))
for _ in range(m):
     x,y=map(int, input().strip().split())
     l2.append((x,y))
array1=np.array(l1)
array2=np.array(l2)
finalarray=np.concatenate((array1,array2))
print(finalarray)
               



